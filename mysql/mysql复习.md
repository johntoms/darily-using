1.数据库（database）:有组织的数据的容器。
2.数据库管理系统（DBMS）：数据库管理系统，管理数据库的软件。
3.数据库分类：
  关系型数据库（oracle,DB2,microsoft sql server,microsoft access,mysql,mariadb|知名公司：alibaba，sina,youtube,google,网易等）
               (由二维表及其之间的联系组成的数据组织)
  键值数据库(Riak,Amazon's Dynamo,projiect Voldmort|知名公司：github（riak），twitter)
                （哈希表，查询，删除，添加更为方便）
  面向文档数据库（monggoDB|知名公司：SAP）
                （以文档为单位的储存的形式）
  列存储数据库（HBase|知名公司：yahoo，facebook，NASA）
               （将数据存储在列表中）  
  图数据库（Neo4J|知名公司：Adobe）
                 （以图片为单位储存）
				 
4.mysql定义：采用c/s(更安全，稳定)（b/s模型：浏览器/服务器（更方便））开放源码、关系型SQL数据库管理系统，多guo'jia操作平台，mysql AB发明，后被sun公司收购，后又被Oracle（percanel sql）收购，知名分支：mariadb

1.sudo service mysql start  检测是否有mysql程序

2.sudo apt-get install mysql-server msyql-client(ubuntu 下安装mysql)
sudo yum  -y install MariaDB-server MariaDB-client(redhat centos下安装mariadb)
配置yum
[MariaDB]
name=MariaDB
baseurl=http://yum.mariadb.org/10.0/centos6-amd64
gpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1

3.netstat -luntp|grep mysql/MariaDB (查看端口信息)
netstat -tap|grep mysql/MariaDB（查看端口信息）

yum list|grep mariadb(查找相关的安装包)

rpm -ql|mariadb-server (查看软件架构)

/var/lib/msyql/(存放数据的文件夹)
service mariadb start    systemctl start mariadb/mysql
daemon msyqld
/etc/my.cnf    /etc/my.cnf/*.cnf (配置文件)
/var/log/mariadb/mariadb.log/mariadb/mariadb(错误日志，启动日志)
/var/log/mysql.log  （日志文件）
端口：3306
ps -ef |grep mysqld  (查看守护进程)
/var/usr/local/mysql/bin/   （脚本文件目录）
MYSQL服务器和服务器启动脚本：
 Mysqld     MySQL服务器 
 mysqld_safe、mysql.server和mysqld_multi是服务器启动脚本 
 mysql_install_db  初始化数据目录和初始数据库
访问服务器的客户程序： 
mysql    是一个命令行客户程序，用于交互式或以批处理模式执行SQL语句 
mysqladmin    是用于管理功能的客户程序 
mysqlcheck    执行表维护操作 
mysqldump和mysqlhotcopy负责数据库备份 
mysqlimport    导入数据文件
 mysqlshow    显示信息数据库和表的相关信息
独立于服务器操作的工具程序： 
myisamchk    执行表维护操作
 myisampack    产生压缩、只读的表 
 mysqlbinlog    是处理二进制日志文件的实用工具 
 perror    显示错误代码的含义

4.chkconfig --level 35 mysql on(设置mysql自启)

5.mysqladmin -uroot -p 123456 password '123';(更改mysql root用户密码为123，若mysql为初始安装123456为空)

DCL数据库控制语言
-----------------------
6.grant <priv权限> on <dbname>.<tbname> to <username>@'%'('192.168.1.'%'') idenified by 'password'; 添加用户
权限：insert，delete，update,select,replaction slave ,all(除了授权给用户以外的所有权限)
eg:grant select on *.* to 'booboo'@'%' idenified by '123456789';

7.revoke <priv权限> on <dbname>.<tbname> from <username>@'%'('192.168.1.'%''); 回收用户权限，不删除用户，用户依然可以连接
flush privileges;  (手动刷新授权)
8.drop user 'username'@'%'('192.168.1.'%''); 删除用户

9.show grants for ‘user’； 查看所有用户权限

DDL 数据库定义语言
------------------
1.声明列类型
create table test_t(id int(11) primary key  not null auto_increment,name varchar(50) default 'noname',score float unique not null);

2.常见约束
primary key ,foreign key ,default,auto_increment,not null,unique,
3.建库建表
create database dbname;
create table tbname(id int ,name char(11));
4.删库删表
drop database dbname;
drop table tbname;
------------------
DML数据库管理语言
增删改
insert into tbname values(123,'maria');
insert into tbname set id values(1),(2),(3);
insert into tbname set id=5,name='kangkang';
delete from tbname where id=1;(一定注意过滤条件)

update tbname set id=1000,name='booboo' where id=1;


 字段相关
 alter table myclass add passtest int(4) default '0'; (增加字段)
 alter table myclass change old_field_name new_field_name field_type;（修改字段）
 alter table myclass drop field_name;（删除字段）

 rename对一张表的操作（重命名一张表）
 rename table <原名> to <新名>；
 alter table <原名> rename to <新名>；
 alter table <原名> rename <新名>;

========================================================================================================================
------------------------------
DCL数据库控制语言

select user,host,password from mysql.user;(查看用户密码)

grant ，revoke ， drop 授权，收权，删除用户；

DQL数据库查询语言

select * from <tbname>;(查看表的所有组成)
desc tbname;（显示表的结构信息）
> （大于） <（小于）  <> 和=！（不等于）  in 和not in     between and(左闭右开)   ，and
如果将值和串类型进行比较，必须加上限定引号。

where ,group ,having，order by (desc) ,limit 2.2

select distinct vend_name from products;(不重复)
select produce_name from produces where produce_name regexp '.000';(不区分大小写查询带000的记录)

select produce_name from produces where produce_name regexp binary '.000';(区分大小写查询带000的记录)
select max{avg,min,count}(price) from phoneinfo;(常用函数)

使用“primary key”关键字创建主键数据列。被设置为主键列不允许出现重复的值，很多情况下与“auto_increment”递增数字相结合。
如下SQL语句所示：
<pre>
Mysql>create table books(bookid int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,bookname varchar(50)); 
Mysql>insert into books(bookname) values(“book1”),(“book2”),(“book3”); 
Mysql>select * from books; 
</pre>


    若要修改列主键或类型，请参考 ALTER TABLE 语句。
设置MySQL数据表外键


    外键是设置当前表中的某一列与别一数据表中的主键列关联。主要目的是控制与外键表中的数据，保持数据一致性，完整性，也就是说：
    当前表中这一列的数据必须是关联外键列中的某一数据，而且相关联的两个数据列的类型必须相同；
    当关联外键列某一数据修改或删除时，将触当前表的某一项相应操作。可解发以下事件以及参数：
触发事件：on delete和on update 
可设参数：cascade(跟随外键改动)； 
restrict(限制外表中的外键改动)；
set Null(设空值）；
set Default（设默认值）；
no action [默认]


    设置关联的语句由[指定主键关键字：foreign key(列名)]和[引用外键关键字： references <外键表名>(外键列名)]组成。
    例如创建一个关于books的购物车数据表“gbooks”，其中“gbookid”与books表中的“bookid”创建外键关联。
<pre>
Mysql>create table gbooks(gid int(11) not null auto_increment primary key,
gbookid int(11),goodsum int(4),foreign key(gbookid) references books(bookid) on delete cascade on update cascade); 
</pre>


    删除外键：
    首先，使用SHOW CREATE TABLE语句查看创建表描述。
    其中“CONSTRAINT”关键字后面有一个引号括起来的名称，它就是这个表外键的代表，是在创建外键时自动生成的名称，
    当然在创建的过程中可以直接用“CONSTRAINT”关键字自定义名称。其查看的完整语句如下：
<pre>
Mysql>show create table gbooks; 
</pre>
    这里代表外键的名称是“gbooks_ibfk_1”，目标找到了，再使用ALTER语句进行删除。
<pre>
Mysql>ALTER TABLE gbooks DROP FOREIGN KEY gbooks_ibfk_1; 
</pre>
=====================================================================================================================


存储引擎：myisam innodb
                      事务                      锁精度                          适用场景
myisam                不支持                     表                               olap在线分析（读性能好，适用于分析）
innodb                支持                       行                               oltp在线事务（钱，互联网，高并发）

事务：ACID 
A：原子性 事物内部不可分割
mysql5.5默认存储引擎innodb 5.1默认为myisam
事务：begin：commit：
自动提交的方式

建表指定引擎 create table <tablename> (id int,name char(60)) engine=myisam;
查看表的信息：show table status\G;


myisam 锁精度只为表，局限性太大，

备份：
冷备、热备、异地灾备
冷备：将数据以隔离的形式来保存，备份数据不受原数据的影响。（优：硬件故障，人为误操作。缺点：恢复数据慢）
热备（冗余）：搭建主从冗余环境，数据一致性。（优:能够瞬间还原,硬件故障。缺点：不能解决人为误操作）
冷备：
物理备份、逻辑备份（数据类型）
离线冷备、温备、在线热备（服务可用性）
全备份、增备、差异备（备份的数量）

物理备份：文件，适用于数据量大
逻辑备份：sql语句，适用于数据量小的50G

离线冷备：不可读，不可写，服务不可用
温备：可读不可写，服务不可用
在线热备：可读可写，服务可用

全备份：所有的数据
增备：针对于上一次的备份
差异备：针对于上一次的全备份

备份的两大要素：
数据一致性，服务可用性

tar                  物理备份（全备） 
备份：
1，停服务      systemctl stop mariadb
2，备份数据     tar -cf /databackup/mysql.all.tar /var/lib/msyql/
3，启服务       systemctl start mariadb
还原：
1，停服务       systemctl stop mariadb 
2，清环境        rm -rf /var/lib/mysql/*
3，导入数据      tar -vf /databackup/mysql.all.tar -C /
4，检查权限   文件权限chown -R MySQL：mysql [目标文件]，进程权限 vim /etc/selinux/config   getenforce disabled   
5，启服务   systemctl start mariadb

mysqldump             逻辑备份 （全备）
myisam :
mysqldump -uroot -p123456 -A --lock-all-tables >/databackup/mysql.all.sql
innodb:
mysqldump -uroot -p123456 -A --single-transaction > /databackup/mysql.all.sql

还原：
停服务       systemctl stop mariadb
清环境        rm -rf /var/lib/msyql/*
启服务        systemctl start mariadb
导入数据      mysqldump -uroot -p123456 < /databackup/mysql.all.sql
刷新权限     flush privileges
测试

对于比较小的数据库而言 可以不用停服务来回复数据
1，进入数据库drop <databasename>;
2,mysqldump -uroot -p123456 < /databackup/mysql.all.sql
3,进入数据检查是否完整

innobackupx           物理备份（增备|全备）
全备份：
innobackupex --use=root --password=123456 > /databackup/mysqlbackup/
1,备份文件指定路径必须为绝对路径
2，目录可以不存在

全备份还原：
innobackupex --apply-log /databackup/mysqlbackup/xxxx
innobackupex --copy-back /databackup/mysqlbackup/xxxx


innobackupex --help |grep incremental(查看帮助)
chown -R mysql:mysql /databackup/mysqlbackup/mysql
chown mysql: /databackup/mysqlbackup/mysql -R

增量备份：
innobackupex --user=root --password=123456 /databackup/mysqlbackup/xxxx-1
innobackupex --user=root --password=123456 --incremental-basedir=/databackup/mysqlbackup/xxxx-1 --incremental /databackup/mysqlbackup/xxxx-2
innobackupex --user=root --password=123456 --incremental-basedir=/databackup/mysqlbackup/xxxx-2 --incremental /databackup/mysqlbackup/xxxx-3

增量还原：
innobackupex --apply-log --redo_only /databackup/mysqlbackup/xxxx-1 
innobackupex --apply-log --redo_only /databackup/mysqlbackup/xxxx-1 --incremental-dir=/databackup/mysqlbackup/xxxx-2
innobackupex --apply-log --redo_only /databackup/mysqlbackup/xxxx-1 --incremental-dir=/databackup/mysqlbackup/xxxx-3
日志和数据汇总到全备份中，在对全备份进行恢复

innobackupex --apply-log /databackup/mysqlbackup/xxxx-1
innobackupex --copy-back /databackup/mysqlbackup/xxxx-1