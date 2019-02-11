vim /etc/my.cnf

在mysqld下开启binlog日志，binlog日志单独存放，太重要了。

log-bin=/var/lib/mysql-log/mastera 最后必须指定mysql的文件开头名。

mysqlbinlog 查看二进制日志

数据库的binlog日志默认不打开，需要手动打开。

log-bin 日志存放路径

binlog日志记录的内容：DDL，DCL，DML 操作--写



binlog日志格式：3种

statement    sql语句模式   5.5                    日志量小（粗略）

row               行模式          5.6，5.7            日志量大（较细致）

mix               两者之间    

statement  不能进行全部恢复    



1.5.5 log_format=row

2.5.6 5.7 默认为row格式 