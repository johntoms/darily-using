# screen

> linux 技巧：使用 screen 管理你的远程会话

[TOC]

## 为什么要用 screen？

你是不是经常需要 SSH 或者 telent 远程登录到 Linux 服务器？你是不是经常为一些长时间运行的任务而头疼，比如系统备份、ftp 传输等等。通常情况下我们都是为每一个这样的任务开一个远程终端窗口，因为他们执行的时间太长了。必须等待它执行完毕，在此期间可不能关掉窗口或者断开连接，否则这个任务就会被杀掉，一切半途而废了。

## 原理

> ## SIGHUP 信号

让我们来看看为什么关掉窗口/断开连接会使得正在运行的程序死掉。

在Linux/Unix中，有这样几个概念：

- 进程组（process group）：一个或多个进程的集合，每一个进程组有唯一一个进程组ID，即进程组长进程的ID。
- 会话期（session）：一个或多个进程组的集合，有唯一一个会话期首进程（session leader）。会话期ID为首进程的ID。
- 会话期可以有一个单独的控制终端（controlling terminal）。与控制终端连接的会话期首进程叫做控制进程（controlling process）。当前与终端交互的进程称为前台进程组。其余进程组称为后台进程组。

根据POSIX.1定义：

- 挂断信号（SIGHUP）默认的动作是终止程序。
- 当终端接口检测到网络连接断开，将挂断信号发送给控制进程（会话期首进程）。
- 如果会话期首进程终止，则该信号发送到该会话期前台进程组。
- 一个进程退出导致一个孤儿进程组中产生时，如果任意一个孤儿进程组进程处于STOP状态，发送SIGHUP和SIGCONT信号到该进程组中所有进程。

因此当网络断开或终端窗口关闭后，控制进程收到SIGHUP信号退出，会导致该会话期内其他进程退出。

我们来看一个例子。打开两个SSH终端窗口，在其中一个运行top命令。

```
`[root@tivf09 root]# top`
```

在另一个终端窗口，找到top的进程ID为5180，其父进程ID为5128，即登录shell。

```
`[root@tivf09 root]# ps -ef|grep top``root      5180  5128  0 01:03 pts/0    00:00:02 top``root      5857  3672  0 01:12 pts/2    00:00:00 grep top`
```

使用pstree命令可以更清楚地看到这个关系：

```
`[root@tivf09 root]# pstree -H 5180|grep top``|-sshd-+-sshd---bash---top`
```

使用ps-xj命令可以看到，登录shell（PID 5128）和top在同一个会话期，shell为会话期首进程，所在进程组PGID为5128，top所在进程组PGID为5180，为前台进程组。

```
`[root@tivf09 root]# ps -xj|grep 5128`` ``5126  5128  5128  5128 pts/0     5180 S        0   0:00 -bash`` ``5128  5180  5180  5128 pts/0     5180 S        0   0:50 top`` ``3672 18095 18094  3672 pts/2    18094 S        0   0:00 grep 5128`
```

关闭第一个SSH窗口，在另一个窗口中可以看到top也被杀掉了。

```
`[root@tivf09 root]# ps -ef|grep 5128``root     18699  3672  0 04:35 pts/2    00:00:00 grep 5128`
```

如果我们可以忽略SIGHUP信号，关掉窗口应该就不会影响程序的运行了。nohup命令可以达到这个目的，如果程序的标准输出/标准错误是终端，nohup默认将其重定向到nohup.out文件。值得注意的是nohup命令只是使得程序忽略SIGHUP信号，还需要使用标记**&**把它放在后台运行。

```
`nohup <``command``> [argument…] &`
```

虽然nohup很容易使用，但还是比较“简陋”的，对于简单的命令能够应付过来，对于复杂的需要人机交互的任务就麻烦了。

其实我们可以使用一个更为强大的实用程序screen。流行的Linux发行版（例如Red Hat Enterprise Linux 4）通常会自带screen实用程序，如果没有的话，可以从GNU screen的官方网站下载。

```bash
`[root@tivf06 ~]# rpm -qa|grep screen``xscreensaver-4.18-5.rhel4.11``screen-4.0.2-5`
```

## 如何使用 screen

简单来说，Screen是一个可以在多个进程之间多路复用一个物理终端的窗口管理器。Screen中有会话的概念，用户可以在一个screen会话中创建多个screen窗口，在每一个screen窗口中就像操作一个真实的telnet/SSH连接窗口那样。在screen中创建一个新的窗口有这样几种方式：

1．直接在命令行键入screen命令

```bash
`[root@tivf06 ~]# screen`
```

Screen将创建一个执行shell的全屏窗口。你可以执行任意shell程序，就像在ssh窗口中那样。在该窗口中键入exit退出该窗口，如果这是该screen会话的唯一窗口，该screen会话退出，否则screen自动切换到前一个窗口。

2．Screen命令后跟你要执行的程序。

```bash
[root@tivf06 ~]# screen vi test.c
```

Screen创建一个执行vi test.c的单窗口会话，退出vi将退出该窗口/会话。

3．以上两种方式都创建新的screen会话。我们还可以在一个已有screen会话中创建新的窗口。在当前screen窗口中键入`C-a c`，即`Ctrl`键+`a`键，之后再按下`c`键，screen 在该会话内生成一个新的窗口并切换到该窗口。

screen还有更高级的功能。你可以不中断screen窗口中程序的运行而暂时断开（detach）screen会话，并在随后时间重新连接（attach）该会话，重新控制各窗口中运行的程序。例如，我们打开一个screen窗口编辑/tmp/abc文件：

```bash
`[root@tivf06 ~]# screen vi /tmp/abc`
```

之后我们想暂时退出做点别的事情，比如出去散散步，那么在screen窗口键入`C-a d`，Screen会给出detached提示：暂时中断会话

```bash
[root@johntoms ~]# screen vim test.py
[detached from 10489.pts-2.johntoms]
[root@johntoms ~]# screen -ls
There are screens on:
	10489.pts-2.johntoms	(Detached)
	6506.pts-0.VM_0_2_centos	(Detached)
2 Sockets in /var/run/screen/S-root.

[root@johntoms ~]# screen -r 10489.pts-2.johntoms
[screen is terminating]
```

![screen打开后的图片](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/screen-1.jpeg)

你可能注意到给screen发送命令使用了特殊的键组合C-a。这是因为我们在键盘上键入的信息是直接发送给当前screen窗口，必须用其他方式向screen窗口管理器发出命令，默认情况下，screen接收以C-a开始的命令。这种命令形式在screen中叫做键绑定（key binding），C-a叫做命令字符（command character）。

![Screen常用选项](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/screen-2.jpeg)

## screen 常用选项

> `Crtl` + `a `  进入命令行模式后，常用的绑定键如下

| 键位          | 描述                                      |
| ------------- | ----------------------------------------- |
| ？            | 显示所有键绑定信息                        |
| w             | 显示所有窗口列表                          |
| d             | 暂时断开screen会话                        |
| `Crtl` + `a ` | 切换到之前显示的窗口                      |
| a             | 发送 C-a到当前窗口                        |
| k             | 杀掉当前窗口                              |
| [             | 进入拷贝/回滚模式                         |
| p             | 切换到前一个窗口(与C-a n相对)             |
| c             | 创建一个新的运行shell的窗口并切换到该窗口 |
| n             | 切换到下一个窗口                          |
| 0…9           | 切换到窗口0..9                            |

> 常用的命令参数

| 参数                            | 描述                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| -c file                         | 使用配置文件file，而不使用默认的$HOME/.screenrc              |
| -d\|-D [pid.tty.host]           | 不开启新的screen会话，而是断开其他正在运行的screen会话       |
| -h num                          | 指定历史回滚缓冲区大小为num行                                |
| -list\|-ls                      | 列出现有screen会话，格式为pid.tty.host                       |
| -d -m                           | 启动一个开始就处于断开模式的会话                             |
| -r sessionowner/ [pid.tty.host] | 重新连接一个断开的会话。多用户模式下连接到其他用户screen会话需要指定sessionowner，需要setuid-root权限 |
| -S sessionname                  | 创建screen会话时为会话指定一个名字                           |
| -v                              | 显示screen版本信息                                           |
| -wipe [match]                   | 同-list，但删掉那些无法连接的会话                            |

```bash
screen --help
Use: screen [-opts] [cmd [args]]
 or: screen -r [host.tty]

Options:
-4            Resolve hostnames only to IPv4 addresses.
-6            Resolve hostnames only to IPv6 addresses.
-a            Force all capabilities into each window's termcap.
-A -[r|R]     Adapt all windows to the new display width & height.
-c file       Read configuration file instead of '.screenrc'.
-d (-r)       Detach the elsewhere running screen (and reattach here).
-dmS name     Start as daemon: Screen session in detached mode.
-D (-r)       Detach and logout remote (and reattach here).
-D -RR        Do whatever is needed to get a screen session.
-e xy         Change command characters.
-f            Flow control on, -fn = off, -fa = auto.
-h lines      Set the size of the scrollback history buffer.
-i            Interrupt output sooner when flow control is on.
-l            Login mode on (update /var/run/utmp), -ln = off.
-ls [match]   or
-list         Do nothing, just list our SockDir [on possible matches].
-L            Turn on output logging.
-m            ignore $STY variable, do create a new screen session.
-O            Choose optimal output rather than exact vt100 emulation.
-p window     Preselect the named window if it exists.
-q            Quiet startup. Exits with non-zero return code if unsuccessful.
-Q            Commands will send the response to the stdout of the querying process.
-r [session]  Reattach to a detached screen process.
-R            Reattach if possible, otherwise start a new session.
-s shell      Shell to execute rather than $SHELL.
-S sockname   Name this session <pid>.sockname instead of <pid>.<tty>.<host>.
-t title      Set title. (window's name).
-T term       Use term as $TERM for windows, rather than "screen".
-U            Tell screen to use UTF-8 encoding.
-v            Print "Screen version 4.01.00devel (GNU) 2-May-06".
-wipe [match] Do nothing, just clean up SockDir [on possible matches].
-x            Attach to a not detached screen. (Multi display mode).
-X            Execute <cmd> as a screen command in the specified session.
```

## 常见使用场景

### 清除异常会话

下例显示当前有两个处于detached状态的screen会话，你可以使用screen -r <screen_pid>重新连接上：

```bash
[root@johntoms ~]# screen -ls
There are screens on:
	13210.test	(Attached)
	6506.pts-0.VM_0_2_centos	(Detached)
2 Sockets in /var/run/screen/S-root.

[root@johntoms ~]# ps -ef |grep test
root     13209  6507  0 15:57 pts/1    00:00:00 screen -R test
root     13210 13209  0 15:57 ?        00:00:00 SCREEN -R test
root     13307  8785  0 15:58 pts/2    00:00:00 grep --color=auto test
[root@johntoms ~]# kill 13209
[root@johntoms ~]# ps -ef |grep test
root     13210     1  0 15:57 ?        00:00:00 SCREEN -R test
root     13337  8785  0 15:58 pts/2    00:00:00 grep --color=auto test
[root@johntoms ~]# kill -9 13210
[root@johntoms ~]# ps -ef |grep test
root     13368  8785  0 15:59 pts/2    00:00:00 grep --color=auto test
[root@johntoms ~]# screen -ls
There are screens on:
	13210.test	(Dead ???)
	6506.pts-0.VM_0_2_centos	(Detached)
Remove dead screens with 'screen -wipe'.
2 Sockets in /var/run/screen/S-root.

[root@johntoms ~]# screen -wipe
There are screens on:
	13210.test	(Removed)
	6506.pts-0.VM_0_2_centos	(Detached)
1 socket wiped out.
1 Socket in /var/run/screen/S-root.

[root@johntoms ~]# screen -list
There is a screen on:
	6506.pts-0.VM_0_2_centos	(Detached)
1 Socket in /var/run/screen/S-root.
```

### 开启一个后台会话 执行一个任务

> -d –m 选项是一对很有意思的搭档。他们启动一个开始就处于断开模式的会话。你可以在随后需要的时候连接上该会话。有时候这是一个很有用的功能，比如我们可以使用它调试后台程序。

该选项一个更常用的搭配是：-dmS sessionname启动一个初始状态断开的screen会话：

```bash
[root@johntoms ~]# screen -dmS update_data
[root@johntoms ~]# screen -ls
There are screens on:
	14441.update_data	(Detached)
	6506.pts-0.VM_0_2_centos	(Detached)
2 Sockets in /var/run/screen/S-root.

[root@johntoms ~]# screen -r 14441.update_data
[detached from 14441.update_data]
[root@johntoms ~]#
```

随后使用`screen -r screen_id `连接

## 更多Screen功能

Screen提供了丰富强大的定制功能。你可以在Screen的默认两级配置文件/etc/screenrc和$HOME/.screenrc中指定更多，例如设定screen选项，定制绑定键，设定screen会话自启动窗口，启用多用户模式，定制用户访问权限控制等等。如果你愿意的话，也可以自己指定screen配置文件。

以多用户功能为例，screen默认是以单用户模式运行的，你需要在配置文件中指定multiuser on 来打开多用户模式，通过acl*（acladd,acldel,aclchg...）命令，你可以灵活配置其他用户访问你的screen会话。更多配置文件内容请参考screen的man页。

## 参考资料

- “Advanced Programming in the UNIX® Environment: Second Edition” W. Richard Stevens, Stephen A. Rago 提供了更多关于Linux/Unix进程关系、信号的知识。
- GNU Screen的官方网站：<http://www.gnu.org/software/screen/>
- Screen的man page提供了最详细的信息：<http://www.slac.stanford.edu/comp/unix/package/epics/extensions/iocConsole/screen.1.html>

- IBM developerworks 原文地址<https://www.ibm.com/developerworks/cn/linux/l-cn-screen/>