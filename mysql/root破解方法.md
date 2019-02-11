破解root密码：

**一般方法：**对服务器有影响

**高级方法：**不影响服务器





**一般方法：**

1.停服务 service mariadb stop

2.启服务 mysqld_safe --skip-grant-tables &

3.修改密码   update mysql.user set password=password('新密码') where  ps -ef|grep mysql[d]

​           mysqld_safe

​		   mysqld

​		   kill -9 [mysqld_safe的PID]

​		   kill -9 [mysqld的PID]

​		   service mariadb strart

4.停服务

5.启服务





**高级方法：**

**需求：有一个可以登录到数据库的用户，且有对某一个库有update权限。**



**1.**[root@localhost admin]# *mysql -upython -ppython123python*

mysql: [Warning] Using a password on the command line interface can be insecure.

ERROR 1045 (28000): Access denied for user 'python'@'localhost' (using password: YES)

[root@localhost admin]# mysql -upython -ppython@123python

mysql: [Warning] Using a password on the command line interface can be insecure.

ERROR 1045 (28000): Access denied for user 'python'@'localhost' (using password: YES)

[root@localhost admin]# ***mysql -upython -ppython123@python    -------确认用户可用***

mysql: [Warning] Using a password on the command line interface can be insecure.

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 9

Server version: 5.7.21-log MySQL Community Server (GPL)



Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.



mysql> \q

Bye

[root@localhost admin]# mysql -upython -ppython123@python

mysql: [Warning] Using a password on the command line interface can be insecure.

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 10

Server version: 5.7.21-log MySQL Community Server (GPL)



Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.



mysql> show databases;

+--------------------+

| Database           |

+--------------------+

| information_schema |

| reserve            |

+--------------------+

2 rows in set (0.00 sec)



mysql> \q

Bye

[root@localhost admin]# ***ll /var/lib/mysql/mysql/user.\*     -----查看user表***

-rw-r-----. 1 mysql mysql 10816 Jan 22 12:25 /var/lib/mysql/mysql/user.frm

-rw-r-----. 1 mysql mysql   508 Jan 22 15:16 /var/lib/mysql/mysql/user.MYD

-rw-r-----. 1 mysql mysql  4096 Jan 22 15:16 /var/lib/mysql/mysql/user.MYI

[root@localhost admin]# ***ll /var/lib/mysql/reserve/     ------查看低权限用户的库***

total 80 

-rw-r-----. 1 mysql mysql   8732 Jan 22 14:28 bookshop.frm

-rw-r-----. 1 mysql mysql 114688 Jan 22 14:02 bookshop.ibd

-rw-r-----. 1 mysql mysql     65 Jan 22 13:52 db.opt

[root@localhost admin]# ***cp /var/lib/mysql/mysql/user.\* /var/lib/mysql/reserve/   -----cp到低权限用户下进行操作***

[root@localhost admin]# **ll /var/lib/mysql/reserve/   -----检查复制后的权限**

total 100

-rw-r-----. 1 mysql mysql   8732 Jan 22 14:28 bookshop.frm

-rw-r-----. 1 mysql mysql 114688 Jan 22 14:02 bookshop.ibd

-rw-r-----. 1 mysql mysql     65 Jan 22 13:52 db.opt

-rw-r-----. 1 root  root   10816 Jan 22 15:41 user.frm

-rw-r-----. 1 root  root     508 Jan 22 15:41 user.MYD

-rw-r-----. 1 root  root    4096 Jan 22 15:41 user.MYI

[root@localhost admin]# ***chown -R mysql:mysql /var/lib/mysql/reserve/user.\*  ------修改权限，使数据库对此文件有操作权限***

[root@localhost admin]# ***ll /var/lib/mysql/reserve/     -----再次确认***

total 100

-rw-r-----. 1 mysql mysql   8732 Jan 22 14:28 bookshop.frm

-rw-r-----. 1 mysql mysql 114688 Jan 22 14:02 bookshop.ibd

-rw-r-----. 1 mysql mysql     65 Jan 22 13:52 db.opt

-rw-r-----. 1 mysql mysql  10816 Jan 22 15:41 user.frm

-rw-r-----. 1 mysql mysql    508 Jan 22 15:41 user.MYD

-rw-r-----. 1 mysql mysql   4096 Jan 22 15:41 user.MYI

[root@localhost admin]# **mysql -upython -ppython123@python    -----登陆低权限用户对user表进行操作**

mysql: [Warning] Using a password on the command line interface can be insecure.

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 11

Server version: 5.7.21-log MySQL Community Server (GPL)



Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.



mysql> ***use reserve;  -----使用此库***

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A



Database changed

mysql> show tables;

+-------------------+

| Tables_in_reserve |

+-------------------+

| bookshop          |

| user              |

+-------------------+

2 rows in set (0.00 sec)



mysql> ***select user,host,authentication_string from user;  -------查看user表***

***+---------------+-----------+-------------------------------------------+***

***| user          | host      | authentication_string                     |***

***+---------------+-----------+-------------------------------------------+***

***| root          | localhost | \*6BBB6C74D523421CDC35B476FA3B79732BDF2C67 |***

***| mysql.session | localhost | \*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |***

***| mysql.sys     | localhost | \*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |***

***| python        | localhost | \*464A061116F98ADFFCE39249AE4B81F00604D0F2 |***

***+---------------+-----------+-------------------------------------------+***

4 rows in set (0.00 sec)



mysql> ***update user set authentication_string=password('zyadmin123@cloudcare') where user='root';   -------最重要的一步，更改密码***

Query OK, 1 row affected, 1 warning (0.01 sec)

Rows matched: 1  Changed: 1  Warnings: 1



mysql> ***select user,host,authentication_string from user;   -----和之前的对比***

+---------------+-----------+-------------------------------------------+

| user          | host      | authentication_string                     |

+---------------+-----------+-------------------------------------------+

| root          | localhost | *292AC33B52F53C892392C915B7E8BD7518EC0C2B |

| mysql.session | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |

| mysql.sys     | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |

| python        | localhost | *464A061116F98ADFFCE39249AE4B81F00604D0F2 |

+---------------+-----------+-------------------------------------------+

4 rows in set (0.00 sec)



mysql> commit;

Query OK, 0 rows affected (0.00 sec)



mysql> \q

Bye

[root@localhost admin]***cp /var/lib/mysql/reserve/user.\* /var/lib/mysql/mysql/   -----复制到mysql.user下***

cp: overwrite `/var/lib/mysql/mysql/user.frm'? y

cp: overwrite `/var/lib/mysql/mysql/user.MYD'? y

cp: overwrite `/var/lib/mysql/mysql/user.MYI'? y

[root@localhost admin]# ***ll /var/lib/mysql/mysql/user.\*  -----检查权限***

-rw-r-----. 1 mysql mysql 10816 Jan 22 15:45 /var/lib/mysql/mysql/user.frm

-rw-r-----. 1 mysql mysql   508 Jan 22 15:45 /var/lib/mysql/mysql/user.MYD

-rw-r-----. 1 mysql mysql  4096 Jan 22 15:45 /var/lib/mysql/mysql/user.MYI

[root@localhost admin]# ***mysql -uroot -pzyadmin123@cloudcare     ----尝试登陆（肯定不行）***

mysql: [Warning] Using a password on the command line interface can be insecure.

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

[root@localhost admin]# ***pgrep -n mysqld     -----查找mysqld的pid***

***2123***

[root@localhost admin]# ***kill -SIGHUP 2123    -----不停服务向mysqld进程发送SIGHUP信号进行刷新授权***

[root@localhost admin]# ***mysql -uroot -pzyadmin123@cloudcare    ----再次登陆，成功！！！***

mysql: [Warning] Using a password on the command line interface can be insecure.

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 13

Server version: 5.7.21-log MySQL Community Server (GPL)



Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.



Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.



Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.



mysql> ***show databases;     -------测试***

+--------------------+

| Database           |

+--------------------+

| information_schema |

| mysql              |

| performance_schema |

| reserve            |

| sys                |

+--------------------+

5 rows in set (0.00 sec)



mysql> \q

Bye