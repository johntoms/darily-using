# Linux下如何查看硬件信息
> 我们在 Linux 下 进行开发时，有时也需要知道当前的硬件信息，
> 比如：CPU几核？使用情况？内存大小及使用情况？USB设备是否被识别？
> 等等类似此类问题。下面良许介绍一些常用的硬件查看命令。

## lshw
> lshw 这个命令是一个比较通用的工具，它可以详细的列出本机的硬件信息。
> 但这个命令并非所有的发行版都有，比如 `Fedora` `CentoS`
> 就默认没有，需要自己安装。

> lshw 可以从各个 /proc 文件中提取出硬件信息，比如：CPU、内存、usb
> 控制器、硬盘等。如果不带选项的话，列出的信息将很长，加上 -short
> 选项时，将只列出概要信息。

```
# 注意应使用 `root` 用户查看
[root@johntoms ~]# lshw -short
H/W path          Device      Class          Description
========================================================
                              system         Alibaba Cloud ECS
/0                            bus            Motherboard
/0/0                          memory         96KiB BIOS
/0/400                        processor      Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz
/0/1000                       memory         2GiB System Memory
/0/1000/0                     memory         2GiB DIMM RAM
/0/100                        bridge         440FX - 82441FX PMC [Natoma]
/0/100/1                      bridge         82371SB PIIX3 ISA [Natoma/Triton II]
/0/100/1.1        scsi1       storage        82371SB PIIX3 IDE [Natoma/Triton II]
/0/100/1.1/0.0.0  /dev/cdrom  disk           QEMU DVD-ROM
/0/100/1.2                    bus            82371SB PIIX3 USB [Natoma/Triton II]
/0/100/1.2/1      usb1        bus            UHCI Host Controller
/0/100/1.2/1/1                input          QEMU USB Tablet
/0/100/1.3                    bridge         82371AB/EB/MB PIIX4 ACPI
/0/100/2                      display        GD 5446
/0/100/3                      network        Virtio network device
/0/100/3/0        eth0        network        Ethernet interface
/0/100/4                      communication  Virtio console
/0/100/4/0                    generic        Virtual I/O device
/0/100/5                      storage        Virtio block device
/0/100/5/0        /dev/vda    disk           42GB Virtual I/O device
/0/100/5/0/1      /dev/vda1   volume         39GiB EXT4 volume
/0/100/6                      generic        Virtio memory balloon
/0/100/6/0                    generic        Virtual I/O device
/0/100/7                      generic        Red Hat, Inc
/0/100/7/0                    generic        Virtual I/O device
/0/1                          system         PnP device PNP0b00
/0/2                          input          PnP device PNP0303
/0/3                          input          PnP device PNP0f13
/0/4                          storage        PnP device PNP0700
/0/5                          communication  PnP device PNP0501
```

## lscpu
> lscpu 可以列出本机的 CPU 的相关信息，该命令没有任何选项及参数。 


``` 
[root@johntoms ~]$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Model name:            Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz
Stepping:              2
CPU MHz:               2494.224
BogoMIPS:              4988.44
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              30720K
NUMA node0 CPU(s):     0
```

## lsusb
> lsusb 列出与本机相连的所有 USB 设备的信息。默认情况下，只列出概要信息，使用 -v
> 选项可以列出每一个 USB 口的详细信息。 
```
# 对于云服务器而言，是没有的
[alvin@VM_0_16_centos ~]$ lsusb
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. SMC9514 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

```

## lsscsi
> lsscsi 可以列出诸如硬盘/光驱等 SCSI/SATA 设备信息。 

```
# 对于云服务器无效
[alvin@VM_0_16_centos ~]$ lsscsi
[0:0:1:0]    cd/dvd  QEMU     QEMU DVD-ROM     1.2.  /dev/sr0复制代码

```
## lspci
> lspci 列出所有 PCI 总线，以及与 PCI 总线相连的所有设备的详细信息，比如 VGA 适配器、显卡、网络适配器、usb 端口、SATA 控制器等。

```
[root@johntoms ~]# lspci
00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]
00:01.2 USB controller: Intel Corporation 82371SB PIIX3 USB [Natoma/Triton II] (rev 01)
00:01.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 03)
00:02.0 VGA compatible controller: Cirrus Logic GD 5446
00:03.0 Ethernet controller: Red Hat, Inc Virtio network device
00:04.0 Communication controller: Red Hat, Inc Virtio console
00:05.0 SCSI storage controller: Red Hat, Inc Virtio block device
00:06.0 Unclassified device [00ff]: Red Hat, Inc Virtio memory balloon
00:07.0 Unclassified device [00ff]: Red Hat, Inc Device 1014
```
## df
> df 命令可以列出不同分区的大小，使用情况，使用率， 挂载点等信息，加上 -h
> 选项可以以 k, M, G 等单位表示大小，否则默认是字节，不容易阅读。

```
[root@johntoms ~]# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        40G   19G   19G  51% /
devtmpfs        910M     0  910M   0% /dev
tmpfs           920M     0  920M   0% /dev/shm
tmpfs           920M  844K  919M   1% /run
tmpfs           920M     0  920M   0% /sys/fs/cgroup
tmpfs           184M     0  184M   0% /run/user/0
tmpfs           184M     0  184M   0% /run/user/1010
```

## free
> free命令可以查看系统中使用的、闲置的和 RAM 的总体数量，一般带上 -m 参数。

```
[root@johntoms ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:           1839         938         108           1         792         713
Swap:             0           0           0
```
