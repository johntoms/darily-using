# linux设置selinux模式

临时关闭：

[root@localhost ~]# getenforce
Enforcing

[root@localhost ~]# setenforce 0
[root@localhost ~]# getenforce
Permissive



永久关闭：

[root@localhost ~]# vim /etc/sysconfig/selinux

SELINUX=enforcing 改为 SELINUX=disabled

重启服务reboot