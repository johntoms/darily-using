# Linux 服务器上建立用户并分配权限

## 查看当前登陆的用户

> `who`
>
> 参数    说明
>
> -a  打印能打印的全部
> -d  打印死掉的进程
> -m  同am i,mom likes
> -q  打印当前登录用户数及用户名
> -u  打印当前登录用户登录信息
> -r  打印运行等级

- `whoami`
- `who am i`
- `who mom likes`

```bash

# 表示打开当前伪终端的用户的用户名
[root@johntoms /]# who am i
root     pts/0        2019-02-23 00:24 (112.64.60.29)
# 要查看当前登录用户的用户名
[root@johntoms /]# whoami
root
[root@johntoms /]# who mom like
root     pts/0        2019-02-23 00:24 (112.64.60.29)
[root@johntoms /]# who mom likes
root     pts/0        2019-02-23 00:24 (112.64.60.29)
[root@johntoms /]# who mom lik
root     pts/0        2019-02-23 00:24 (112.64.60.29)
[root@johntoms /]# who mom l
root     pts/0        2019-02-23 00:24 (112.64.60.29)
[root@johntoms /]# who mom s
root     pts/0        2019-02-23 00:24 (112.64.60.29)
[root@johntoms /]# who mom q
root     pts/0        2019-02-23 00:24 (112.64.60.29)
[root@johntoms /]# who -a
           system boot  2019-01-11 10:42
           run-level 3  2019-01-11 10:42
LOGIN      ttyS0        2019-01-11 10:42               655 id=tyS0
LOGIN      tty1         2019-01-11 10:42               656 id=tty1
root     + pts/0        2019-02-23 00:24   .         17320 (112.64.60.29)
           pts/1        2019-02-21 00:29             29377 id=ts/1  term=0 exit=0
           pts/2        2019-02-22 14:22             30394 id=ts/2  term=0 exit=0
           pts/3        2019-02-13 01:02              8333 id=ts/3  term=0 exit=0
           pts/1        2019-02-21 14:41              6507 id=/1    term=0 exit=0
           pts/3        2019-02-21 17:49             22955 id=/3    term=0 exit=0
           pts/0        2019-02-21 16:12             14442 id=/0    term=0 exit=0
```

## 新增用户

> 所用命令
>
> `useradd` or `adduser`

**注意：**`useradd`和`adduser`相同,但是`addgroup`是不存在的命令,所以建议使用`useradd`

```bash
[root@johntoms /]# useradd --help
[root@johntoms /]# useradd --help
用法：useradd [选项] 登录
      useradd -D
      useradd -D [选项]

选项：
  -b, --base-dir BASE_DIR       新账户的主目录的基目录
  -c, --comment COMMENT         新账户的 GECOS 字段
  -d, --home-dir HOME_DIR       新账户的主目录
  -D, --defaults                显示或更改默认的 useradd 配置
 -e, --expiredate EXPIRE_DATE  新账户的过期日期
  -f, --inactive INACTIVE       新账户的密码不活动期
  -g, --gid GROUP               新账户主组的名称或 ID
  -G, --groups GROUPS   新账户的附加组列表
  -h, --help                    显示此帮助信息并推出
  -k, --skel SKEL_DIR   使用此目录作为骨架目录
  -K, --key KEY=VALUE           不使用 /etc/login.defs 中的默认值
  -l, --no-log-init     不要将此用户添加到最近登录和登录失败数据库
  -m, --create-home     创建用户的主目录
  -M, --no-create-home          不创建用户的主目录
  -N, --no-user-group   不创建同名的组
  -o, --non-unique              允许使用重复的 UID 创建用户
  -p, --password PASSWORD               加密后的新账户密码
  -r, --system                  创建一个系统账户
  -R, --root CHROOT_DIR         chroot 到的目录
  -s, --shell SHELL             新账户的登录 shell
  -u, --uid UID                 新账户的用户 ID
  -U, --user-group              创建与用户同名的组
  -Z, --selinux-user SEUSER             为 SELinux 用户映射使用指定 SEUSER
```

