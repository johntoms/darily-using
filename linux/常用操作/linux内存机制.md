linux内存机制

[TOC]

#一、如何查看linux内存

## 　2.1. CentOS6及以前

 

　　在CentOS6及以前的版本中，free命令输出是这样的：

```
$free -m
 
             total           used      free    shared    buffers     cached
Mem:         1002            769       233       0         62         421
-/+ buffers/cache:           286       716
Swap:         1153           0         1153
```




|      第一行：系统内存概况       |      第二行      | 第三行：swap |
| :-------------------: | :-----------: | :------: |
|     total（系统总内存）      |       /       |    /     |
|     used（程序已使用内存）     | used（系统已使用内存） |    /     |
|      free（空闲内存）       | free（系统可用内存）  |    /     |
| buffers（buffer cache） |       /       |    /     |
|  cached（Page cache）   |       /       |    /     |

换算关系：

**total=used（第一行：程序已使用内存）+free（第一行：空闲内存**

**used（第一行：程序已使用内存）=buffers + cached+used（第二行：系统已使用内存）**

说明：buffers和cached是算在used（第一行：程序已使用内存）里的，但是它知识分配给了应用程序，并未被应用程序真正使用；used（第二行：系统已使用内存）是应用程序真正在使用的内存。



**total=used（第二行：系统已使用内存）+free（第二行：系统可用内存)**

**used（第二行：系统已使用内存）=total-free（第二行：系统可用内存) **

**free（第二行：系统可用内存） = free（第一行：空闲内存） + buffers + cached **



shared为程序共享的内存空间，往往为0。

第三行是swap内存交换空间使用情况。

 

## 2.2. CentOS7及以后

　　CentOS7及以后free命令的输出如下：

```shell
# free -m
              total        used        free      shared  buff/cache   available
Mem:            991          60          72           0         858         763
Swap:             0           0           0
```

 

变化：

* buffer和cached被合成一组，加入了一个available
* used：应用程序实际使用的内存

换算关系：

**available = free + buffer/cache - 不可被回收内存(共享内存段、tmpfs、ramfs等)**

**total=used+free+buff/cache**

说明：

free：空闲内存（不含buffer、cache）

avaible：系统可用内存，章节1说过buffer和cache在必要时可以被系统回收，系统可用内存=free（第一行：空闲内存）+buffer+cache，这种说法其实并不准确，因为并不是所有的buffer/cache空间都可以被回收。

因此在CentOS7之后，用户不需要去计算buffer/cache，即可以看到还有多少内存可用，更加简单直观。

 

#三、案例

好了，让我们来看个案例吧

##3.1. 报错



```shell
Java HotSpot(TM) 64-Bit Server VM warning: INFO: os::commit_memory(0x0000000080000000, 697892864, 0) failed; error='Cannot allocate memory' (errno=12)
#
# There is insufficient memory for the Java Runtime Environment to continue.
# Native memory allocation (mmap) failed to map 697892864 bytes for committing reserved memory.
# An error report file with more information is saved as:
# /app/logstash-6.4.0/config/hs_err_pid24934.log
```



## 3.2 排查

根据报错信息”commit_memory(0x0000000080000000, 697892864, 0) failed; error='Cannot allocate memory' (errno=12)
There is insufficient memory for the Java Runtime Environment to continue.
Native memory allocation (mmap) failed to map 697892864 bytes for committing reserved memory.“
首先查看服务器内存使用情况：

```shell
# free 
     total    used    free   shared  buff/cache   available
Mem: 16267196 6404952 8859812 404    1002432      9552720
Swap: 0 0 0
```

单位：KB

available可用内存9552720KB

再看报错信息，客户java程序要分配的内存为697892864 bytes=681536KB<available=9552720KB

 内存够用啊，那为什么系统会报错内存分配失败呢？这就和内存overcommit机制有关系了

#四、理解LINUX的MEMORY OVERCOMMIT

##4.1. 理解Memory Overcommit机制

Memory Overcommit的意思是操作系统承诺给进程的内存大小超过了实际可用的内存。一个保守的操作系统不会允许memory overcommit，有多少就分配多少，再申请就没有了，这其实有些浪费内存，因为进程实际使用到的内存往往比申请的内存要少，比如某个进程malloc()了200MB内存，但实际上只用到了100MB，按照UNIX/Linux的算法，物理内存页的分配发生在使用的瞬间，而不是在申请的瞬间，也就是说未用到的100MB内存根本就没有分配，这100MB内存就闲置了。下面这个概念很重要，是理解memory overcommit的关键：commit(或overcommit)针对的是内存申请，内存申请不等于内存分配，内存只在实际用到的时候才分配。

Linux是允许memory overcommit的，只要你来申请内存我就给你，寄希望于进程实际上用不到那么多内存，但万一用到那么多了呢？那就会发生类似“银行挤兑”的危机，现金(内存)不足了。

Linux设计了一个OOM killer机制(OOM = out-of-memory)来处理这种危机：挑选一个进程出来杀死，以腾出部分内存，如果还不够就继续杀…也可通过设置内核参数 vm.panic_on_oom 使得发生OOM时自动重启系统。这都是有风险的机制，重启有可能造成业务中断，杀死进程也有可能导致业务中断，所以Linux 2.6之后允许通过内核参数 vm.overcommit_memory 禁止memory overcommit。

##4.2 内核参数vm.overcommit_memory

内核参数 vm.overcommit_memory接受三种取值， 默认值=0

```shell
# cat /proc/sys/vm/overcommit_memory
0
```

- 0 – Heuristic overcommit handling. 这是缺省值，它允许overcommit，但过于明目张胆的overcommit会被拒绝，比如malloc一次性申请的内存大小就超过了系统总内存。Heuristic的意思是“试探式的”，内核利用某种算法（单次申请的内存大小不能超过 【free memory + free swap + pagecache的大小 + SLAB中可回收的部分】，否则本次申请就会失败）猜测你的内存申请是否合理，它认为不合理就会拒绝overcommit。
- 1 – Always overcommit. 允许overcommit，对内存申请来者不拒。
- 2 – Don’t overcommit. 禁止overcommit。
  内核参数 vm.overcommit_memory 的值0，1，2对应的源代码如下，其中heuristic overcommit对应的是OVERCOMMIT_GUESS：

```
源文件：source/include/linux/mman.h 
#define OVERCOMMIT_GUESS                0
#define OVERCOMMIT_ALWAYS               1
#define OVERCOMMIT_NEVER                2
```
Heuristic overcommit算法在以下函数中实现，基本上可以这么理解：
。


## 4.2. 什么情况是overcommit？

关于禁止overcommit (vm.overcommit_memory=2) ，需要知道的是，怎样才算是overcommit呢？kernel设有一个阈值，申请的内存总数超过这个阈值就算overcommit，在/proc/meminfo中可以看到这个阈值的大小：

```shell
# grep -i commit /proc/meminfo
CommitLimit:      507704 kB
Committed_AS:     231612 kB
```

CommitLimit 就是overcommit的阈值，申请的内存总数超过CommitLimit的话就算是overcommit。
这个阈值是如何计算出来的呢？它既不是物理内存的大小，也不是free memory的大小，它是通过内核参数vm.overcommit_ratio或vm.overcommit_kbytes间接设置的，公式如下：
【CommitLimit = (Physical RAM * vm.overcommit_ratio / 100) + Swap】

注：
vm.overcommit_ratio 是内核参数，缺省值是50，表示物理内存的50%。如果你不想使用比率，也可以直接指定内存的字节数大小，通过另一个内核参数 vm.overcommit_kbytes 即可；
如果使用了huge pages，那么需要从物理内存中减去，公式变成：
CommitLimit = ([total RAM] – [total huge TLB RAM]) * vm.overcommit_ratio / 100 + swap
参见<https://access.redhat.com/solutions/665023>

/proc/meminfo中的 Committed_AS 表示所有进程已经申请的内存总大小，（注意是已经申请的，不是已经分配的），如果 Committed_AS 超过 CommitLimit 就表示发生了 overcommit，超出越多表示 overcommit 越严重。Committed_AS 的含义换一种说法就是，如果要绝对保证不发生OOM (out of memory) 需要多少物理内存。



##4.3. sar -r查看内存使用情况

“sar -r”是查看内存使用状况的常用工具，它的输出结果中有两个与overcommit有关，kbcommit 和 %commit：*
*kbcommit对应/proc/meminfo中的 Committed_AS；*
*%commit的计算公式并没有采用 CommitLimit作分母，而是Committed_AS/(MemTotal+SwapTotal)，意思是_内存申请_占_物理内存与交换区之和_的百分比。

```shell
# sar -r
11:40:01 AM kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit  kbactive .. 
11:50:01 AM     76340    939068     92.48    141092    661388    233816     23.03    489300 .. 
```









​                                                                                         