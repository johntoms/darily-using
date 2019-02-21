# 更改 liunx 主机名

## 查看当前主机的主机名

- `hostname`

- `hostnamectl`

```bash
[root@johntoms ~]# vim /etc/host.conf
[root@johntoms ~]# hostnamectl
   Static hostname: johntoms
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 8d13a50988cc5c4972347415eddf7d47
           Boot ID: 553b9373bec6431db3294d904c9e0499
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-514.21.1.el7.x86_64
      Architecture: x86-64
[root@johntoms ~]# hostname
johntoms
```

## 永久修改主机名

1. 主机名保存在**/etc/hostname**文件里，所以我们可以打开这个文件，手动编辑主机名。

  ```bash
  sudo vi /etc/hostname
  ```

  将当前的主机名删除，然后输入一个新的主机名，再保存文件。现在使用**hostname**或  **hostnamectl**命令就会发现主机名已经更改了。如果现在打开一个新的终端窗口也会发现主  机名的更改。这种更改主机名的方法是持久性的，也就是说重启电脑后你会看到新的主机名。

2. 使用 `hostnamectl`命令修改主机名

   ```bash
   sudo hostnamectl set-hostname <newhostname>
   ```

### 更新/etc/hosts文件

> 重要操作

在更改主机名后我们需要更新**/etc/hosts**解析文件。

```
sudo vim /etc/hosts
```



把旧的主机名删除，替换为新的主机名，保存文件就行了。要注意大小写。

   ```bash
[root@johntoms ~]# cat /etc/hosts
127.0.0.1 johntoms johntoms
127.0.0.1 localhost.localdomain localhost
127.0.0.1 localhost4.localdomain4 localhost4

::1 johntoms johntoms
::1 localhost.localdomain localhost
::1 localhost6.localdomain6 localhost6
# 修改旧的主机名为新主机名
[root@johntoms ~]#

   ```

如果你不更新**/etc/hosts**文件，那么有的程序，如sudo，不知道如何解析新的主机名。

如果你在更改Linux服务器的主机名，那么新的主机名应该要解析为Linux服务器的公网IP。如果更改个人电脑的主机名，那么新的主机名应该解析为127.0.0.1，或者127.0.1.1。

127.0.1.1是Debian系Linux发行版解析本地主机的IP。Debian系统在安装时，如果计算机的IP是动态的，那么Debian安装程序会在**/etc/hosts**文件中创建**127.0.1.1 <主机名>**这一条目。127.0.1.1地址使用loopback网卡，实际上127.0.0.0/8 (127.0.0.0 ~ 127.255.255.255)都使用loopback网卡。



## 临时修改主机名

```bash
sudo hostname <new-hostname>
# 这条命令不会更改/etc/hostname文件中的静态主机名（static hostname），它更改的只是临时主机名（transient # hostname）。所以重启计算机后会回到旧的主机名。

# 静态主机名保存在/etc/hostname文件中。
```

