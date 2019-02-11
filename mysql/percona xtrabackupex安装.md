**percona xtrabackupex安装**



进入官网选择与自己系统匹配的版本，centos6.8 mariadb10.0 默认服务器版本为mysql-5.1.7，建议选择percona xtrabackupex 2.0.0,/Percona-XtraBackup-2.3.2不适合这个版本。 

[root@localhost bin]# innobackupex --user=root --password='123456' /tmp/ 发现有错误，配置文件有问题，修改配置文件。

vim /etc/my.cnf

[mysqld]

datadir=/var/lib/mysql

\#打开bin-log日志

bin-log=msyql-log

[mysql.server] basedir=/usr/local/mysql

成功安装！

常用配置实例

[client] default-character-set = utf8

port = 3306

socket = /tmp/mysql.sock

[mysqld]

user = mysql

port = 3306

socket = /tmp/mysql.sock

basedir = /opt/mysql

datadir = /opt/mysql/var

log-error = /opt/mysql/var/mysql-error.log

pid-file = /opt/mysql/var/mysql.pid

log_slave_updates = 1

log-bin = /opt/mysql/var/mysql-bin

binlog_format = mixed

binlog_cache_size = 4M

max_binlog_cache_size = 8M

max_binlog_size = 1G

expire_logs_days = 90

key_buffer_size = 384M

sort_buffer_size = 2M

read_buffer_size = 2M

read_rnd_buffer_size = 16M

join_buffer_size = 2M

thread_cache_size = 8

query_cache_size = 32M

query_cache_limit = 2M

query_cache_min_res_unit = 2k

thread_concurrency = 32

table_cache = 614

table_open_cache = 512

open_files_limit = 10240

back_log = 600

max_connections = 5000

max_connect_errors = 6000

external-locking = FALSE

max_allowed_packet = 16M

default-storage-engine = MYISAM

thread_stack = 192k

transaction_isolation = READ-COMMITTED

tmp_table_size = 256M

max_heap_table_size = 512M

bulk_insert_buffer_size = 64M

myisam_sort_buffer_size = 64M

myisam_max_sort_file_size = 10G

myisam_repair_threads = 1

myisam_recover

long_query_time = 2

slow_query_log

slow_query_log_file = /opt/mysql/var/slow.log

skip-name-resolve

skip-locking

skip-networking

innodb_additional_mem_pool_size = 16M

innodb_buffer_pool_size = 512M

innodb_data_file_path = ibdata1:256M:autoextend

innodb_file_io_threads = 4

innodb_thread_aoncurrency = 8

innodb_flush_log_at_trx_commit = 2

innodb_log_buffer_size = 16M

innodb_log_file_size = 128M

innodb_log_files_in_group = 3

innodb_max_dirty_pages_pct = 90

innodb_lock_wait_timeout = 120

innodb_file_per_table = 0

[mysqldump]

quick

max_allow_packet = 64M

[mysql]

no-auto-rehash

safr-updates

[myisamchk]

key_buffer_size = 256M

sort_buffer_size = 256M

read_buffer = 2M

[mysqldump]

quick

max_allow_packet = 64M

[mysql]

no-auto-rehash

safe-updates

[myisamchk]

key_buffer_size = 256M

sort_buffer_size = 256M

read_buffer = 2M

write_buffer = 2M

[mysqlhotcopy]

interactive-timeout