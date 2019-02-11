# MySQL源码安装 

1. 下载源码包

```bash
wget http://zy-res.oss-cn-hangzhou.aliyuncs.com/mysql/mysql-5.7.17-linux-glibc2.5-x86_64.tar.gz
```

2. 创建所需得目录目录放入/data/mysql/下

   ```bash
   mkdir -p /data/{mysql/data,mysql/error,mysql-log}
   ```

3. 添加mysql用户组

   ```bash
   groupadd mysql
   ```

4. 创建mysql用户

   ```bash
   useradd -s /sbin/nologin -g mysql -M mysql
   id mysql
   ```

5. 解压mysql源码包

   ```bash
   tar -xvf mysql-5.7.17-linux-glibc2.5-x86_64.tar.gz
   ```

6. 移动解压后的文件到/data/mysql/下

   ```bash
   mv mysql-5.7.17-linux-glibc2.5-x86_64/* /data/mysql/
   ```

7. 备份/etc/my.cnf

   ```bash
   mv /etc/my.cnf /etc/my.cnf.bak
   ```

8. 编辑配置文件

   ```shell
   [client]
   port            = 3306
   socket          = /data/mysql/mysql.sock
   [mysqld]
   basedir = /data/mysql
   datadir = /data/mysql/data
   port = 3306
   server_id = 2
   socket  = /data/mysql/mysql.sock
   log-bin = /data/mysql-log/log-bin
   log_error = /data/mysql/error/slave.err
   pid-file  = /data/mysql/mysql.pid
   ```

9. 修改/data目录的权限

   ```bash
   chown mysql.mysql -R /data/
   ```

10. 注意事项

  编译源码之前版本mysql_install_db是在mysql_basedir/script下，5.7放在了mysql_install_db/bin目录下,且已被废弃。"--initialize"会生成一个随机密码(~/.mysql_secret)，而"--initialize-insecure"不会生成密码 --datadir目标目录下不能有数据文件。可能找不到随机密码的隐藏文件，打开my.cnf查看错误日志文件的路径(log-error=/xx/xx.log)，找到此错误日志文件搜索字符串 A temporary password is generated for root@localhost:，可以找到这个随机密码，通常这一行日志在log文件的最初几行，比较容易看到。使用找到的随机密码登录mysql，首次登录后，mysql要比必须修改默认密码，否则不能执行任何其他数据库操作，这样体现了不断增强的Mysql安全性。登陆mysql需要修改root密码，否则会出现下列情况：

  ```shell
  root@localhost : (none) 11:16:52> show databases;
  
  ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
  ```

  修改root密码

  ```bash
  SET password='MYSQL';
  ```

11. 编译源码

    ```bash
    /data/mysql/bin/mysqld  --initialize-insecure --user=mysql --basedir=/data/mysql --datadir=/data/mysql/data/
    ```

    有报错如下：

    ![libaio.so.1报错](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/libaio_so_error.png)
    安装libaio依赖包,再次安装。

12. 安装 libaio 模块

    ```bash
    yum install libaio
    ```

13. 复制mysql.server到启动目录

    ```bash
    cp /data/mysql/support-files/mysql.server /etc/init.d/mysqld
    ```

14. 建立软连接mysql命令到/usr/local/bin/下

    ```bash
    ln -sv /data/mysql/bin/mysql /usr/local/bin/
    ```

    

15. 创建目录并建立软链接到/usr/local/bin/mysql/bin/mysqld

    ```bash
    mkdir /usr/local/mysql/bin -p && ln -sv /data/mysql/bin/mysqld /usr/local/mysql/bin/mysqld
    ```

16. 启动mysql

    ```bash
    service mysqld start
    ```

    ![安装成功测试](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/mysql-install-successful.png)

17. 测试ok!!!

## 常见问题

![/var/lib/mysql/mysql.sock不存在](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/mysql-installprolicy-error.png)

mysql 没有对/var/lib/mysql操作的权限

```bash
chown -R mysql:mysql /var/lib/mysql
service mysqld start
```

