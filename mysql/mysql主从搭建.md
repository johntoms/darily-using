复制问题

复制就是把某服务器上（称为主节点服务器或者简称为主节点即master）的所有变化克隆到另一个服务器（称为从节点服务器或者简称为从节点，即slave）。



复制原理

1，在主库上把数据更改记录到binlog日志中。

2，从库将主库的binlog日志复制到自己的中继日志relaylog中。

3，从库读取中继日志中的事件，将其重演到从库的数据库中。

![主从搭建原理图](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/mysql%E4%B8%BB%E4%BB%8E%E6%90%AD%E5%BB%BA%E5%8E%9F%E7%90%86.png)

 \# 主服务器   

1）修改配置文件  log‐bin server‐id=1（重启服务） 

  2）授权从机  grant replication slave on *.*  to slave@172.25.0.12 identified by ‘123456’；

  3）初始化数据一致  mysqldump‐‐‐》传输给从机器

  \# 从服务 

  1）install   

2）修改配置文件  server‐id=2   

3）初始化数据一致  导入全备数据   

4）> change master to master_host='172.25.0.11'       master_user='slave'       master_password='uplooking'       master_log_file=''       master_log_pos=''  

show master status；

——

 5)> start slave;   

6)> show slave status\G;



mysqldump -uroot  -p123456 --master-data=2 > all.sql

perconal会自动显示master-log-file信息

sed -n '22p' /tmp/all.sql    mariadb5.5在22行

确保防火墙关闭

system status firewalld 查看防火墙状态

iptables -F 关闭防火墙 

service iptables save 保存防火墙规则

scp /tmp/all.sql root@：192.168.213.129：/tmp   远程复制

help change master to   帮助命令

help show

重建主从关系    

| 操作步骤                   | 命令                                   |
| -------------------------- | -------------------------------------- |
| 停slave服务                | stop slave；                           |
| 清空change master to的配置 | reset slave all；（mysql5.1不用加all） |
| 重新配置                   | change master to 。。。。。。。        |



mysql5.7

gtid特性 无需手动获得日志位置

5.7自动获取事务一致

master

【mysqld】

server-id=1

log-bin=/var/lib/mysql-log/mastera

gtid_mode=on

enforce_gtid_consistency=1



slave

【mysqld】

server-id=2

gtid_mode=on

enforce_gtid_consistency=1



在mysql中也可以操作系统层面的东西

system ifconfig



binlog-format=row    /fixed混合模式

master_auto_position=1自动获取master位置

error_code:2005   log-bin日志有问题