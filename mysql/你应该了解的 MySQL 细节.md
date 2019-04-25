# MySQL
> 此文
> 发布在掘金网站上，[传送门](https://juejin.im/post/5cbfd06ef265da03b57b5a35)。


> 做为关系型数据库，是目前最为流行的开源数据之一，凭借其高性能和丰富的数据类型为
> IT 事业提供后台数据存储与管理工具。 MySQL(发音为”my ess cue
> el”)是一种开放源代码的关系型数据库管理系统，因为是开放源代码的，在下载后可以根据自己的需要进行修改。由于其体积小、速度快、总体拥有成本低，尤其是开放源码这一特点，许多中小型网站为了降低网站总体拥有成本而选择了MySQL作为网站数据库。

**写在前面:**
本文章主要主要介绍 mysql5.7。详情版本更迭请参考官访方文档: [MySQL官网](https://www.mysql.com/)

## MySQL 发展历史
---------------------
### 名字由来
- MySQL的海豚标志的名字叫“sakila”，它是由MySQL AB的创始人从用户在“海豚命名”的竞赛中建议的大量的名字表中选出的。获胜的名字是由来自非洲斯威士兰的开源软件开发者Ambrose Twebaze提供。根据Ambrose所说，Sakila来自一种叫SiSwati的斯威士兰方言，女性化名称Sakila源自SiSwati。Sakila也是坦桑尼亚、Arusha地区的一个镇的镇名，靠近Ambrose的母国乌干达。

- MySQL名称的起源不明。一直以来，我们的基本目录以及大量库和工具均采用了前缀“my”。不过，共同创办人Monty Widenius的女儿名字也叫“My”。时至今日，MySQL名称的起源仍是一个迷，即使对我们也一样。

### 早起发展
- 1979年，有一个人叫Monty Widenius, 为一个叫TcX的小公司打工，并用BASIC设计了一个报表工具，可以在4M主频和16KB内在的计算机上运行。过了不久，又将此工具，使用C语言重写，移植到Unix平台，当时，它只是一个很底层的面向报表的存储引擎。这个工具叫做Unireg。

- 1985 年，瑞典的几位志同道合小伙子（以David Axmark 为首） 成立了一家公司，这就是MySQL AB 的前身。这个公司最初并不是为了开发数据库产品，而是在实现他们想法的过程中，需要一个数据库。他们希望能够使用开源的产品。但在当时并没有一个合适的选择，没办法，那就自己开发吧。 
在最初，他们只是自己设计了一个利用索引顺序存取数据的方法，也就是I S A M（Indexed Sequential Access Method）存储引擎核心算法的前身，利用ISAM 结合mSQL 来实现他们的应用需求。在早期，他们主要是为瑞典的一些大型零售商提供数据仓库服务。在系统使用过程中，随着数据量越来越大，系统复杂度越来越高，ISAM 和mSQL 的组合逐渐不堪重负。在分析性能瓶颈之后，他们发现问题出在mSQL 上面。不得已，他们抛弃了mSQL，重新开发了一套功能类似的数据存储引擎，这就是ISAM 存储引擎。大家可能已经注意到他们当时的主要客户是数据仓库，应该也容易理解为什么直至现在，MySQL 最擅长的是查询性能，而不是事务处理（需要借助第三方存储引擎）。

- 1990年，TcX的customer 中开始有人要求要为它的API提供SQL支持，当时，有人想到了直接使用商用数据库算了，但是Monty觉得商用数据库的速度难令人满意。于是，他直接借助于mSQL的代码，将它集成到自己的存储引擎中。但不巧的是，效果并不太好。于是,Monty雄心大起，决心自己重写一个SQL支持。

### 近期发展
- 1996年，MySQL 1.0发布, 在小范围内使用。到了96年10月，MySQL 3.11.1 发布了，没有2.x版本。最开始，只提供了Solaris下的二进制版本。一个月后，Linux版本出现了。 此时的MySQL还非常简陋，除了在一个表上做一些Insert，Update，Delete和Select 操作职位，没有其他更多的功能。 
紧接下来的两年里，MySQL依次移植到各个平台下。它发布时，采用的许可策略，有些与众不同：允许免费商用，但是不能将MySQL与自己的产品绑定在一起发布。如果想一起发布，就必须使用特殊许可，意味着要花银子。当然，商业支持也是需要花银子的。其它的，随用户怎么用都可以。这种特殊许可为MySQL带来了一些收入，从而为它的持续发展打下了良好的基础。

- 1999-2000年，有一家公司在瑞典成立了，叫MySQL AB。 雇了几个人,与Sleepycat合作，开发出了 Berkeley DB引擎, 因为BDB支持事务处理，所以，MySQL从此开始支持事务处理了。

- 2000年4月，MySQL对旧的存储引擎进行了整理，命名为MyISAM。

- 2001年，Heikiki Tuuri向MySQL提出建议，希望能集成他们的存储引擎InnoDB，这个引擎同样支持事务处理，还支持行级锁。所以在2001年发布的3.23 版本的时候，该版本已经支持大多数的基本的SQL 操作，而且还集成了MyISAM和InnoDB 存储引擎。MySQL与InnoDB的正式结合版本是4.0。

- 2004年10月，发布了经典的4.1版本。 2005年10月，有发布了里程碑的一个版本，MySQL 5.0. 在5.0中加入了游标，存储过程，触发器，视图和事务的支持。在5.0 之后的版本里，MySQL明确地表现出迈向高性能数据库的发展步伐。

- 2008 年 01 月 16 日, MySQL被Sun公司收购。
- 2009 年 04 月 20 日, Oracle收购Sun 公司，MySQL 转入Oracle 门下。
- 2010 年 04 月 22 日, 发布MySQL 5.5, MySQLcluster 7.1.
- 2011 年 04 月 11 日, 发布 MySQL5.6, 参考链接：https://dev.mysql.com/doc/relnotes/mysql/5.6/en/
- 2013 年 04 月 23 日, 发布 MySQL5.7, 参考链接：https://dev.mysql.com/doc/relnotes/mysql/5.7/en/
- 2016 年 09 月 12 日, 发布 MySQL8.0, 参考链接：https://dev.mysql.com/doc/relnotes/mysql/8.0/en/
--------------------- 
## MySQL 系统库

|数据库名|说明|
|---|---|---|
| information_schema | `Information_schema`它提供了访问数据库元数据的方式。什么是元数据呢？元数据是关于数据的数据，如数据库名或表名，列的数据类型，或访问权限等。有些时候用于表述该信息的其他术语包括“数据词典”和“系统目录”。|
| mysql              |mysql的核心数据库，类似于sql server中的master表，主要负责存储数据库的用户、权限设置、关键字等mysql自己需要使用的控制和管理信息。(常用的，在mysql.user表中修改root用户的密码)。|
| performance_schema |主要用于收集数据库服务器性能参数。并且库里表的存储引擎均为PERFORMANCE_SCHEMA，而用户是不能创建存储引擎为PERFORMANCE_SCHEMA的表。MySQL5.7默认是开启的。MySQL5.6默认是关闭的。|
| sys                |sys库所有的数据源来自：performance_schema。目标是把performance_schema的把复杂度降低，让DBA能更好的阅读这个库里的内容。让DBA更快的了解DB的运行情况。|
### MySQL 系统表


#### information_schema

|表名称 |
| ------- |
|CHARACTER_SETS |
|COLLATIONS |
|COLLATION_CHARACTER_SET_APPLICABILITY |
|COLUMNS |
|COLUMN_PRIVILEGES |
|ENGINES |
|EVENTS |
|FILES |
|GLOBAL_STATUS |
|GLOBAL_VARIABLES |
|KEY_COLUMN_USAGE |
|OPTIMIZER_TRACE |
|PARAMETERS |
|PARTITIONS |
|PLUGINS |
|PROCESSLIST |
|PROFILING |
|REFERENTIAL_CONSTRAINTS |
|ROUTINES |
|SCHEMATA |
|SCHEMA_PRIVILEGES |
|SESSION_STATUS |
|SESSION_VARIABLES |
|STATISTICS |
|TABLES |
|TABLESPACES |
|TABLE_CONSTRAINTS |
|TABLE_PRIVILEGES |
|TRIGGERS |
|USER_PRIVILEGES |
|VIEWS |
|INNODB_LOCKS |
|INNODB_TRX |
|INNODB_SYS_DATAFILES |
|INNODB_FT_CONFIG |
|INNODB_SYS_VIRTUAL |
|INNODB_CMP |
|INNODB_FT_BEING_DELETED |
|INNODB_CMP_RESET |
|INNODB_CMP_PER_INDEX |
|INNODB_CMPMEM_RESET |
|INNODB_FT_DELETED |
|INNODB_BUFFER_PAGE_LRU |
|INNODB_LOCK_WAITS |
|INNODB_TEMP_TABLE_INFO |
|INNODB_SYS_INDEXES |
|INNODB_SYS_TABLES |
|INNODB_SYS_FIELDS |
|INNODB_CMP_PER_INDEX_RESET |
|INNODB_BUFFER_PAGE |
|INNODB_FT_DEFAULT_STOPWORD |
|INNODB_FT_INDEX_TABLE |
|INNODB_FT_INDEX_CACHE |
|INNODB_SYS_TABLESPACES |
|INNODB_METRICS |
|INNODB_SYS_FOREIGN_COLS |
|INNODB_CMPMEM |
|INNODB_BUFFER_POOL_STATS |
|INNODB_SYS_COLUMNS |
|INNODB_SYS_FOREIGN |
|INNODB_SYS_TABLESTATS |


#### mysql

|表名称 |
| ------- |
|columns_priv |
|db |
|engine_cost |
|event |
|func |
|general_log |
|gtid_executed |
|help_category |
|help_keyword |
|help_relation |
|help_topic |
|innodb_index_stats |
|innodb_table_stats |
|ndb_binlog_index |
|plugin |
|proc |
|procs_priv |
|proxies_priv |
|server_cost |
|servers |
|slave_master_info |
|slave_relay_log_info |
|slave_worker_info |
|slow_log |
|tables_priv |
|time_zone |
|time_zone_leap_second |
|time_zone_name |
|time_zone_transition |
|time_zone_transition_type |
|user |


#### performance_schema
> 详情请参考： [MySQL 官方解释](https://dev.mysql.com/doc/refman/5.7/en/performance-schema.html)

|表名称 |
| ------- |
|accounts |
|cond_instances |
|events_stages_current |
|events_stages_history |
|events_stages_history_long |
|events_stages_summary_by_account_by_event_name |
|events_stages_summary_by_host_by_event_name |
|events_stages_summary_by_thread_by_event_name |
|events_stages_summary_by_user_by_event_name |
|events_stages_summary_global_by_event_name |
|events_statements_current |
|events_statements_history |
|events_statements_history_long |
|events_statements_summary_by_account_by_event_name |
|events_statements_summary_by_digest |
|events_statements_summary_by_host_by_event_name |
|events_statements_summary_by_program |
|events_statements_summary_by_thread_by_event_name |
|events_statements_summary_by_user_by_event_name |
|events_statements_summary_global_by_event_name |
|events_transactions_current |
|events_transactions_history |
|events_transactions_history_long |
|events_transactions_summary_by_account_by_event_name |
|events_transactions_summary_by_host_by_event_name |
|events_transactions_summary_by_thread_by_event_name |
|events_transactions_summary_by_user_by_event_name |
|events_transactions_summary_global_by_event_name |
|events_waits_current |
|events_waits_history |
|events_waits_history_long |
|events_waits_summary_by_account_by_event_name |
|events_waits_summary_by_host_by_event_name |
|events_waits_summary_by_instance |
|events_waits_summary_by_thread_by_event_name |
|events_waits_summary_by_user_by_event_name |
|events_waits_summary_global_by_event_name |
|file_instances |
|file_summary_by_event_name |
|file_summary_by_instance |
|global_status |
|global_variables |
|host_cache |
|hosts |
|memory_summary_by_account_by_event_name |
|memory_summary_by_host_by_event_name |
|memory_summary_by_thread_by_event_name |
|memory_summary_by_user_by_event_name |
|memory_summary_global_by_event_name |
|metadata_locks |
|mutex_instances |
|objects_summary_global_by_type |
|performance_timers |
|prepared_statements_instances |
|replication_applier_configuration |
|replication_applier_status |
|replication_applier_status_by_coordinator |
|replication_applier_status_by_worker |
|replication_connection_configuration |
|replication_connection_status |
|replication_group_member_stats |
|replication_group_members |
|rwlock_instances |
|session_account_connect_attrs |
|session_connect_attrs |
|session_status |
|session_variables |
|setup_actors |
|setup_consumers |
|setup_instruments |
|setup_objects |
|setup_timers |
|socket_instances |
|socket_summary_by_event_name |
|socket_summary_by_instance |
|status_by_account |
|status_by_host |
|status_by_thread |
|status_by_user |
|table_handles |
|table_io_waits_summary_by_index_usage |
|table_io_waits_summary_by_table |
|table_lock_waits_summary_by_table |
|threads |
|user_variables_by_thread |
|users |
|variables_by_thread |


#### sys
- 字母开头： 适合人阅读，显示是格式化的数
- x$开头 ： 适合工具采集数据，原始类数据
> 更多关于 `sys` 请参考:

- [MySQL5.6 PERFORMANCE_SCHEMA 说明
](https://www.cnblogs.com/zhoujinyi/p/5236705.html)
- [浅谈MySQL5.7 sys schema](https://yq.aliyun.com/articles/36106)

|表名称 |
| ------- |
|host_summary |
|host_summary_by_file_io |
|host_summary_by_file_io_type |
|host_summary_by_stages |
|host_summary_by_statement_latency |
|host_summary_by_statement_type |
|innodb_buffer_stats_by_schema |
|innodb_buffer_stats_by_table |
|innodb_lock_waits |
|io_by_thread_by_latency |
|io_global_by_file_by_bytes |
|io_global_by_file_by_latency |
|io_global_by_wait_by_bytes |
|io_global_by_wait_by_latency |
|latest_file_io |
|memory_by_host_by_current_bytes |
|memory_by_thread_by_current_bytes |
|memory_by_user_by_current_bytes |
|memory_global_by_current_bytes |
|memory_global_total |
|metrics |
|processlist |
|ps_check_lost_instrumentation |
|schema_auto_increment_columns |
|schema_index_statistics |
|schema_object_overview |
|schema_redundant_indexes |
|schema_table_lock_waits |
|schema_table_statistics |
|schema_table_statistics_with_buffer |
|schema_tables_with_full_table_scans |
|schema_unused_indexes |
|session |
|session_ssl_status |
|statement_analysis |
|statements_with_errors_or_warnings |
|statements_with_full_table_scans |
|statements_with_runtimes_in_95th_percentile |
|statements_with_sorting |
|statements_with_temp_tables |
|sys_config |
|user_summary |
|user_summary_by_file_io |
|user_summary_by_file_io_type |
|user_summary_by_stages |
|user_summary_by_statement_latency |
|user_summary_by_statement_type |
|version |
|wait_classes_global_by_avg_latency |
|wait_classes_global_by_latency |
|waits_by_host_by_latency |
|waits_by_user_by_latency |
|waits_global_by_latency |
|x$host_summary |
|x$host_summary_by_file_io |
|x$host_summary_by_file_io_type |
|x$host_summary_by_stages |
|x$host_summary_by_statement_latency |
|x$host_summary_by_statement_type |
|x$innodb_buffer_stats_by_schema |
|x$innodb_buffer_stats_by_table |
|x$innodb_lock_waits |
|x$io_by_thread_by_latency |
|x$io_global_by_file_by_bytes |
|x$io_global_by_file_by_latency |
|x$io_global_by_wait_by_bytes |
|x$io_global_by_wait_by_latency |
|x$latest_file_io |
|x$memory_by_host_by_current_bytes |
|x$memory_by_thread_by_current_bytes |
|x$memory_by_user_by_current_bytes |
|x$memory_global_by_current_bytes |
|x$memory_global_total |
|x$processlist |
|x$ps_digest_95th_percentile_by_avg_us |
|x$ps_digest_avg_latency_distribution |
|x$ps_schema_table_statistics_io |
|x$schema_flattened_keys |
|x$schema_index_statistics |
|x$schema_table_lock_waits |
|x$schema_table_statistics |
|x$schema_table_statistics_with_buffer |
|x$schema_tables_with_full_table_scans |
|x$session |
|x$statement_analysis |
|x$statements_with_errors_or_warnings |
|x$statements_with_full_table_scans |
|x$statements_with_runtimes_in_95th_percentile |
|x$statements_with_sorting |
|x$statements_with_temp_tables |
|x$user_summary |
|x$user_summary_by_file_io |
|x$user_summary_by_file_io_type |
|x$user_summary_by_stages |
|x$user_summary_by_statement_latency |
|x$user_summary_by_statement_type |
|x$wait_classes_global_by_avg_latency |
|x$wait_classes_global_by_latency |
|x$waits_by_host_by_latency |
|x$waits_by_user_by_latency |
|x$waits_global_by_latency |
## MySQL 用户管理

1. 权限列表

|权限|说明|
|---|---|
|ALL或 ALL PRIVILEGES| 代表指定权限等级的所有权限|
|ALTER|允许使用ALTER TABLE来改变表的结构，ALTER TABLE同时也需要CREATE和INSERT权限。重命名一个表需要对旧表具有ALTER和DROP权限，对新表具有CREATE和INSERT权限。|
|ALTER ROUTINE|允许更改和删除存储过程和函数|
|CREATE|允许创建数据库和表|
|CREATE ROUTINE|允许创建存储过程和包|
|CREATE TABLEBSPACE |允许创建、更改和删除变空间和日志文件组|
|CREATE TEMPORARY TABLES |允许创建临时表|
|CREATE USER| 允许更改、创建、删除、重命名用户和收回所有权限|
|CREATE VIEW| 允许创建视图|
|DELETE | 允许从数据库的表中删除行|
|DROP   | 允许删除数据库、表和视图|
|EVENT  | 允许在事件调度里面创建、更改、删除和查看事件|
|EXECUETE |   允许执行存储过程和包|
|FILE   |     允许在服务器的主机上通过LOAD DATA INFILE、SELECT ... INTO OUTFILE和LOAD_FILE()函数读写文件|
|GRANT OPTION  |  允许向其他用户授予或移除权限|
|INDEX  | 允许创建和删除索引|
|INSERT | 允许向数据库的表中插入行|
|LOCK TABLE | 允许执行LOCK TABLES语句来锁定表|
|PROCESS| 允许显示在服务器上执行的线程信息，即被会话所执行的语句信息。这个权限允许你执行SHOW PROCESSLIST和mysqladmin processlist命令来查看线程，同时这个权限也允许你执行SHOW ENGINE命令|
|PROXY  | 允许用户冒充成为另外一个用户|
|REFERENCES | 允许创建外键|
|RELOAD | 允许使用FLUSH语句|
|REPLICATION CLIENT | 允许执行SHOW MASTER STATUS,SHOW SLAVE STATUS和SHOW BINARY LOGS命令|
|REPLICATION SLAVE  | 允许SLAVE服务器连接到当前服务器来作为他们的主服务器|
|SELECT | 允许从数据库中查询表|
|SHOW DATABASES | 允许账户执行SHOW DATABASE语句来查看数据库。没有这个权限的账户只能看到他们具有权限的数据库。|
|SHOW VIEW |  允许执行SHOW CREATE VIEW语句|
|SHUTDOWN |   允许执行SHUTDOWN语句和mysqladmin shutdown已经mysql_shutdown() C API函数|
|SUPER   |允许用户执行CHANGE MASTER TO,KILL或mysqladmin kill命令来杀掉其他用户的线程，允许执行PURGE BINARY LOGS命令，通过SET LOBAL来设置系统参数，执行mysqladmin debug命令，开启和关闭日志，即使read_only参数开启也可以执行update语句，打开和关闭从服务器上面的复制，允许在连接数达到max_connections的情况下连接到服务器。|
|TRIGGER |允许操作触发器|
|UPDATE  | 代表没有任何权限，只能登陆。|

2. `mysql` 系统表
```shell
root@MySQL-01 14:15:  [mysql]> show tables;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| engine_cost               |
| event                     |
| func                      |
| general_log               |
| gtid_executed             |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| ndb_binlog_index          |
| plugin                    |
| proc                      |
| procs_priv                |
| proxies_priv              |
| server_cost               |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
31 rows in set (0.00 sec)
```
|表|说明|
|:---:|:---:|
|user|存放用户账户信息以及全局级别（所有数据库）权限，决定了来自哪些主机的哪些用户可以访问数据库实例，如果有全局权限则意味着对所有数据库都有此权限。|
|db|存放数据库级别的权限，决定了来自哪些主机的哪些用户可以访问此数据库。|
|tables_priv|存放表级别的权限，决定了来自哪些主机的哪些用户可以访问此数据库的这个表。|
|columns_priv|存放列级别的权限，决定了来自哪些主机的哪些用户可以访问此数据库的这个表的这个字段。|
|procs_priv|存放存储过程和函数级别的权限|
## 数据库操作
> 针对于库实例的操作，以下仅为简单的操作。


### 查看数据库
```mysql
desc 表名;       // 表信息 
show columns from 表名;       // 表字段 
describe 表名;       // 表信息 
show create table 表名;        // 表创建语句 
show create database 数据库名;        // 显示数据库 信息 
show table status from 数据库名;        // 数据库状态 
show tables或show tables from database_name;       // 显示当前数据库中所有表的名称 
show databases;       // 显示mysql中所有数据库的名称 
show processlist;       // 显示系统中正在运行的所有进程，也就是当前正在执行的查询。大多数用户可以查看他们自己的进程，但是如果他们拥有process权限，就可以查看所有人的进程，包括密码。 
show table status;       // 显示当前使用或者指定的database中的每个表的信息。信息包括表类型和表的最新更新时间 
show columns from table_name from database_name;        // 显示表中列名称 
show columns from database_name.table_name;        // 显示表中列名称 
show grants for user_name@localhost;        // 显示一个用户的权限，显示结果类似于grant 命令 
show index from table_name;        // 显示表的索引 show status;解释：显示一些系统特定资源的信息，例如，正在运行的线程数量 
show variables;        // 显示系统变量的名称和值 show privileges;解释：显示服务器所支持的不同权限 
show create database database_name ;       // 显示create database 语句是否能够创建指定的数据库 
show create table table_name;       // 显示create database 语句是否能够创建指定的数据库 
show engies;        // 显示安装以后可用的存储引擎和默认引擎。 
show innodb status ;        // 显示innoDB存储引擎的状态 
show logs;        // 显示BDB存储引擎的日志 
show warnings;       //显示最后一个执行的语句所产生的错误、警告和通知 
show errors;       // 只显示最后一个执行语句所产生的错误
show provileges; // 查看所有权限列表
```

### 创建数据库
```mysql
## 连接到数据库中
1. CREATE SCHEMA IF NOT EXISTS `databse_name` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin ;
2. CREATE DATABASE IF NOT EXISTS `database_name` DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ic;

## 使用 mysqladmin
mysqladmin -uroot -p123456 create `database_name`;
```

### 删除数据库
```mysql
## 连接到数据库中
DROP DATABASE IF EXISTS `table_name`;

## 使用 mysqladmin
mysql -uroot -p123456 DROP DATABASE IF EXISTS `table_name`;
```
### 创建数据库表 
```mysql
CREATE TABLE `table_name` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `field1` text COLLATE utf8_unicode_ci NOT NULL COMMENT '字段1',
    `field2` varchar(128) COLLATE utf8_unicode_ci NOT NUmyLL DEFAULT '' COMMENT '字段2',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 插入表数据
