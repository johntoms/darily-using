rds  相关

一周一次全备，一天一次增倍（标准）

rds 一天一次全备 oss
备份时间的选择（在空闲时间备份）
备份保留时间 7天


binlog日志备份还原文件
mysqlbinlog   二进制日志转化工具

数据默认不打开，需要手动配置

show values 

vim etc/my.cnf

log-bin=/var/lib/mysql-log/mastera
at 位置标识
;数据提交符
binlog格式：3种
	statement SQL语句模式 5.5                     日志量小
	row 行模式            5.6  5.7 显示的更细致   日志量大
	mixed 混合模式
	
	5.5 log_format=row
	5.6,5.7 默认的为row格式
	
	逆向还原（delete from换成insert into）
	
	
	cpu过高
	1.锁冲突      2.应用负载QPS  
![rds-for-mysql-cpu飙高](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/rds_for_mysql%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5.png)
故障排查

当前数据库所有的会话信息
show processlist；
select * from information_schema.processlist；
1.三种锁
1.锁等待和死锁
阿里报告文档里有行锁阻塞和死锁，直接查看。
2.metadata lock 
在mysql里敲命令：
select * from performance_schema.processlist where  state="Wating for table metadata lock";
查询 mysql中的锁在information_schema.process  where state="waiting for table metadata lock"

2.QPS 应用负载

在监控与报警/引擎监控下观察走势图，看QPS的图。

3.慢查询


4.SQL审计功能  读写比例。
show columns from DB1.t1；
相当于desc DB1.t1；