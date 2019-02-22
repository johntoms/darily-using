

## rds备份还原到自建数据库

1 mysqldump备份还原：（rds逻辑备份不包含系统库，还原的时候需要指定数据库）
  1）下载 
  wget -c '<数据备份文件外网下载地址>' -O <自定义文件名>.tar.gz
  2）解压
  tar -xf 文件

  gunzip 文件

  3导入
  导入之前先把之前的gtid有关的清理掉，reset master;不然导入的时候会报错说这个值不为空不能导入

 mysqldump -u -p 库 < 文件

2 物理备份还原
  1）下载
  wget -c '<数据备份文件外网下载地址>' -O <自定义文件名>.tar.gz
  2）解压
  操作系统中已安装数据备份文件解压工具rds_backup_extract.sh。
  需下载：http://oss.aliyuncs.com/aliyunecs/rds_backup_extract.sh?spm=a2c4g.11186623.2.6.CG4CLz&file=rds_backup_extract.sh

 bash rds_backup_extract.sh -f <数据备份文件名>.tar.gz -C /alidata/mysql/data （解压的路径）
 解压后的图片见图一
 3）导入
 innobackupex --defaults-file=/alidata/mysql/data/backup-my.cnf --apply-log /alidata/mysql/data
 4）更改权限
   chown mysql. -R /alidata/mysql/data

> 在此之前需要这个文档 https://yq.aliyun.com/articles/9044
>  .需要在my.cnf中配置的一些关键参数：
>
> > 上面的和sqlve相关的是配置主从时需要的，如果只是导入数据重启的话只需要加入物理备份文件中的三条就可以了
```shell
   server-id ###Slave配置需要

   master-info-repository=file### Slave配置需要

   relay-log-info_repository=file### Slave配置需要

   binlog-format=ROW### Slave配置需要

   gtid-mode=on###开启GTID需要

   enforce-gtid-consistency=true###开启GTID需要

   innodb_data_file_path=ibdata1:200M:autoextend###使用RDS的物理备份中的backup-my.cnf参数

   innodb_log_files_in_group=2###使用RDS的物理备份中的backup-my.cnf参数

   innodb_log_file_size=524288000###使用RDS的物理备份中的backup-my.cnf参数
```

 5)为避免版本问题，需修改backup-my.cnf参数
 vi /home/mysql/data/backup-my.cnf
 注释
```shell
innodb_fast_checksum
innodb_page_size
innodb_log_block_size
```

 6）启动
 /etc/init.d/mysqld start
 7）登录
 mysql -uroot
 8）恢复完成后，表mysql.user中不包含在RDS实例中创建的用户
 恢复完成的数据库的user表信息如下
 ![](pic\08.png)

没有rds创建的用户的信息


如果需要的话需要新建。在新建用户前，执行如下命令
  delete from mysql.db where user<>'root' and char_length(user)>0;
  delete from mysql.tables_priv where user<>'root' and char_length(user)>0;
   flush privileges;

 