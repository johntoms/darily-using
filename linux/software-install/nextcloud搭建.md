搭建个人云存储一般会想到ownCloud，堪称是自建云存储服务的经典。而Nextcloud是ownCloud原开发团队打造的号称是“下一代”存储。初一看觉得“口气”不小，刚推出来就重新“定义”了Cloud，真正试用过后就由衷地赞同这个Nextcloud：它是个人云存储服务的绝佳选择。可以说Nextcloud 是一款自由 (开源) 的类 Dropbox 软件，由 ownCloud 分支演化形成。它使用 PHP 和 JavaScript 编写，支持多种数据库系统，比如 MySQL/MariaDB、PostgreSQL、Oracle 数据库和 SQLite。它可以使你的桌面系统和云服务器中的文件保持同步，Nextcloud 为 Windows、Linux、Mac、安卓以及苹果手机都提供了客户端支持。同时，Nextcloud 也并非只是 Dropbox 的克隆，它还提供了很多附加特性，如日历、联系人、计划任务以及流媒体 Ampache。

与ownCloud相比，Nextcloud的功能丝毫没有减弱，甚至由于可以安装云存储服务应用，自制性更强，也更符合用户的需求。Nextcloud官网的帮助文档写得相当地详细，几乎任何关于Nextcloud的问题都可以找到答案，这说明Nextcloud开发团队确实比ownCloud更加优秀。

一开始以为Nextcloud只是一个网盘云存储，后来看到Nextcloud内置了Office文档、图片相册、日历联系人、两步验证、文件管理、RSS阅读等丰富的应用，我发现Nextcloud已经仅仅可以用作个人或者团队存储与共享，还可以打造成为一个个人办公平台，几乎相当于一个个人的Dropbox了。

以下内容将介绍如何在 CentOS 7 服务器中安装和配置最新版本的 Nextcloud 12，并且会通过 Nginx 和 PHP7-FPM 来运行 Nextcloud，同时使用 MariaDB 做为数据库系统。Nextcloud云盘环境部署后，可以实现web网页端、手机移动端和桌面客户端三者数据同步，其中桌面客户端可以在本地设置一个文件夹，用于同步数据，这样也就相当于在本地备份了数据。同时客户端只要设置开机启动，即只要是启动状态中，它和网页端的数据就是自动同步的。

1.查看centos版本

```
[root@izuf69goi7zjhqqki0418ez ~]# cat /etc/redhat-release 
CentOS Linux release 7.4.1708 (Core) 

```
2.查看是否安装php,php-common,nginx

```
[root@izuf69goi7zjhqqki0418ez ~]# rpm -qa|grep php
[root@izuf69goi7zjhqqki0418ez ~]# rpm -qa|grep php-common
[root@izuf69goi7zjhqqki0418ez ~]# rpm -qa|grep nginx
```
3.CentOS默认的yum源中并不包含Nginx和php-fpm，首先要为CentOS添加epel源：

```
[root@izuf69goi7zjhqqki0418ez ~]# yum -y install epel-release
[root@izuf69goi7zjhqqki0418ez ~]# yum -y install nginx
```
4.需要再添加一个yum源来安装php-fpm，可以使用webtatic（这个yum源对国内网络来说恐怕有些慢，当然你也可以选择其它的yum源）

```
[root@izuf69goi7zjhqqki0418ez ~]# rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
[root@izuf69goi7zjhqqki0418ez ~]# yum -y install php70w-fpm php70w-cli php70w-gd php70w-mcrypt php70w-mysql php70w-pear php70w-xml php70w-mbstring php70w-pdo php70w-json php70w-pecl-apcu php70w-pecl-apcu-devel
```
完成后，检查一下php-fpm是否已正常安装


```
[root@izuf69goi7zjhqqki0418ez ~]# php -v
PHP 7.0.30 (cli) (built: Apr 28 2018 08:14:08) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2017 Zend Technologies
```
5.配置php-fpm

```
[root@izuf69goi7zjhqqki0418ez ~]# vim /etc/php-fpm.d/www.conf
.....
user = nginx                                   //将用户和组都改为nginx
group = nginx
.....
listen = 127.0.0.1:9000                        //php-fpm所监听的端口为9000
......
env[HOSTNAME] = $HOSTNAME                     //去掉下面几行注释
env[PATH] = /usr/local/bin:/usr/bin:/bin
env[TMP] = /tmp
env[TMPDIR] = /tmp
env[TEMP] = /tmp
```
6.在/var/lib目录下为session路径创建一个新的文件夹，并将用户名和组设为nginx

```
[root@izuf69goi7zjhqqki0418ez ~]#  mkdir -p /var/lib/php/session
[root@izuf69goi7zjhqqki0418ez ~]# chown nginx:nginx -R /var/lib/php/session/
[root@izuf69goi7zjhqqki0418ez ~]# ll -d /var/lib/php/session/
drwxr-xr-x 2 nginx nginx 4096 May 24 13:24 /var/lib/php/session/
```
7.启动Nginx和php-fpm服务，并添加开机启动

```
[root@izuf69goi7zjhqqki0418ez ~]# systemctl start php-fpm
[root@izuf69goi7zjhqqki0418ez ~]# systemctl start nginx
[root@izuf69goi7zjhqqki0418ez ~]# systemctl enable php-fpm
Created symlink from /etc/systemd/system/multi-user.target.wants/php-fpm.service to /usr/lib/systemd/system/php-fpm.service.
[root@izuf69goi7zjhqqki0418ez ~]# systemctl enable nginx
Created symlink from /etc/systemd/system/multi-user.target.wants/nginx.service to /usr/lib/systemd/system/nginx.service
```
8.安装并配置MariaDB
使用MaraiDB作为Nextcloud数据库。yum安装MaraiDB服务。nextcloud默认为sqlite3数据库。centos默认的源为mariadb，安装mysqldb。

```
[root@izuf69goi7zjhqqki0418ez ~]#  yum -y install mariadb mariadb-server
```
> 启动mariadb，并加入开机自启。

```
[root@izuf69goi7zjhqqki0418ez ~]# systemctl start mariadb
[root@izuf69goi7zjhqqki0418ez ~]# systemctl enable mariadb.service
Created symlink from /etc/systemd/system/multi-user.target.wants/mariadb.service to /usr/lib/systemd/system/mariadb.service.

```
9.登录MariaDB，设置root密码为Qwer123456，为Nextcloud创建相应的用户和数据库。
例如数据库为nextcloud_db，用户为nextclouduser，密码为nextclouduser@yuexin：
```
[root@izuf69goi7zjhqqki0418ez ~]# mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2
Server version: 5.5.56-MariaDB MariaDB Server

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> set password=password("Qwer123456");
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> flush privileges;
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.00 sec)

MariaDB [(none)]> create database nextcloud_db;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> grant all on nextcloud_db.* to nextclouduser@localhost identified by "nextclouduser@YueXin";
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> flush privileges;
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> exit

```
10.为nextcloud配置https证书。

```
#lrzsz 用于windows和linux文件交互，sz 文件名 linux -> windows机器。
windows -> linux  直接拖动文件到xshell，即可。
#unzip 解压zip文件

yum -y install lrzsz unzip
```
> 为证书创建一个文件夹cert


```
[root@izuf69goi7zjhqqki0418ez ~]# mkdir -p /etc/nginx/cert/
[root@izuf69goi7zjhqqki0418ez ~]# cd /etc/nginx/cert/
[root@izuf69goi7zjhqqki0418ez cert]# ls
214707227890949.zip

#更改证书名字为nextcloud
[root@izuf69goi7zjhqqki0418ez cert]# mv 214707227890949.key nextcloud.key
[root@izuf69goi7zjhqqki0418ez cert]# mv 214707227890949.pem  nextcloud.pem
[root@izuf69goi7zjhqqki0418ez cert]# ls
214707227890949.zip  nextcloud.key  nextcloud.pem
```
> 更改cert文件夹权限为700和证书权限为600

```
[root@izuf69goi7zjhqqki0418ez cert]#  chmod 700 /etc/nginx/cert
[root@izuf69goi7zjhqqki0418ez cert]# chmod 600 /etc/nginx/cert/*
[root@izuf69goi7zjhqqki0418ez cert]# ll
total 8
-rw------- 1 root root 1674 May 23 11:39 nextcloud.key
-rw------- 1 root root 3678 May 23 11:39 nextcloud.pem
```
11.下载并安装nextcloud，最新版。

官方地址：https://nextcloud.com/install/#instructions-server
-

> 在服务器上下载较慢，建议下载到本地后再上传。


```
[root@izuf69goi7zjhqqki0418ez src]# pwd
/usr/local/src
[root@izuf69goi7zjhqqki0418ez src]# ll
total 59680
-rw-r--r-- 1 root root 61108941 May 24 14:39 nextcloud-13.0.2.zip
[root@izuf69goi7zjhqqki0418ez src]# unzip nextcloud-13.0.2.zip 
[root@izuf69goi7zjhqqki0418ez src]# mv nextcloud /usr/share/nginx/html/
```

12.进入Nginx的root目录，并为Nextcloud创建data目录，将Nextcloud的用户和组修改为nginx
```
[root@izuf69goi7zjhqqki0418ez src]# cd /usr/share/nginx/html/
[root@izuf69goi7zjhqqki0418ez html]# ls
404.html  index.html  nginx-logo.png
50x.html  nextcloud   poweredby.png
[root@izuf69goi7zjhqqki0418ez html]# mkdir -p nextcloud/data/
[root@izuf69goi7zjhqqki0418ez html]#  chown nginx:nginx -R nextcloud/
[root@izuf69goi7zjhqqki0418ez html]# ll -d nextcloud
drwxr-xr-x 14 nginx nginx 4096 May 24 14:44 nextcloud
```
13.设置Nginx虚拟主机
进入Nginx的虚拟主机配置文件所在目录并创建一个新的虚拟主机配置（记得修改两个server_name为自己的域名）：
```
[root@izuf69goi7zjhqqki0418ez html]#  cd /etc/nginx/conf.d/[root@izuf69goi7zjhqqki0418ez conf.d]# ls
[root@izuf69goi7zjhqqki0418ez conf.d]# vim nextcloud.conf
```


> 完整的配置文件           ps(不做修改也可)
```
upstream php-handler {
    server 127.0.0.1:9000;
    #server unix:/var/run/php5-fpm.sock;
}
     
server {
    listen 80;
    server_name www.cxpstudy.top;
    # enforce https
    return 301 https://$server_name$request_uri;
}
     
server {
    listen 443 ssl;
    server_name www.cxpstudy.top;
     
    ssl_certificate /etc/nginx/cert/nextcloud.pem;
    ssl_certificate_key /etc/nginx/cert/nextcloud.key;
     
    # Add headers to serve security related headers
    # Before enabling Strict-Transport-Security headers please read into this
    # topic first.
    add_header Strict-Transport-Security "max-age=15768000;
    includeSubDomains; preload;";
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
    add_header X-Download-Options noopen;
    add_header X-Permitted-Cross-Domain-Policies none;
     
    # Path to the root of your installation
    root /usr/share/nginx/html/nextcloud/;
     
    location = /robots.txt {
        allow all;
        log_not_found off;
        access_log off;
    }
     
   # The following 2 rules are only needed for the user_webfinger app.
   # Uncomment it if you're planning to use this app.
   #rewrite ^/.well-known/host-meta /public.php?service=host-meta last;
   #rewrite ^/.well-known/host-meta.json /public.php?service=host-meta-json
   # last;
     
    location = /.well-known/carddav {
      return 301 $scheme://$host/remote.php/dav;
    }
    location = /.well-known/caldav {
      return 301 $scheme://$host/remote.php/dav;
    }
     
    # set max upload size
    client_max_body_size 512M;
    fastcgi_buffers 64 4K;
     
    # Disable gzip to avoid the removal of the ETag header
    gzip off;
     
    # Uncomment if your server is build with the ngx_pagespeed module
    # This module is currently not supported.
    #pagespeed off;
    error_page 403 /core/templates/403.php;
    error_page 404 /core/templates/404.php;
     
    location / {
        rewrite ^ /index.php$uri;
    }
     
    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)/ {
        deny all;
    }
    location ~ ^/(?:\.|autotest|occ|issue|indie|db_|console) {
        deny all;
    }
     
    location ~ ^/(?:index|remote|public|cron|core/ajax/update|status|ocs/v[12]|updater/.+|ocs-provider/.+|core/templates/40[34])\.php(?:$|/) {
        include fastcgi_params;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_param HTTPS on;
        #Avoid sending the security headers twice
        fastcgi_param modHeadersAvailable true;
        fastcgi_param front_controller_active true;
        fastcgi_pass php-handler;
        fastcgi_intercept_errors on;
        fastcgi_request_buffering off;
    }
     
    location ~ ^/(?:updater|ocs-provider)(?:$|/) {
        try_files $uri/ =404;
        index index.php;
    }
     
    # Adding the cache control header for js and css files
    # Make sure it is BELOW the PHP block
    location ~* \.(?:css|js)$ {
        try_files $uri /index.php$uri$is_args$args;
        add_header Cache-Control "public, max-age=7200";
        # Add headers to serve security related headers (It is intended to
        # have those duplicated to the ones above)
        # Before enabling Strict-Transport-Security headers please read into
        # this topic first.
        add_header Strict-Transport-Security "max-age=15768000;includeSubDomains; preload;";
        add_header X-Content-Type-Options nosniff;
        add_header X-Frame-Options "SAMEORIGIN";
        add_header X-XSS-Protection "1; mode=block";
        add_header X-Robots-Tag none;
        add_header X-Download-Options noopen;
        add_header X-Permitted-Cross-Domain-Policies none;
        # Optional: Don't log access to assets
        access_log off;
    }
     
    location ~* \.(?:svg|gif|png|html|ttf|woff|ico|jpg|jpeg)$ {
        try_files $uri /index.php$uri$is_args$args;
        # Optional: Don't log access to other assets
        access_log off;
    }
}

```

14.接下来测试以下配置文件是否有错误，确保没有问题后重启Nginx服务。

```
[root@izuf69goi7zjhqqki0418ez conf.d]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
[root@izuf69goi7zjhqqki0418ez conf.d]# systemctl restart nginx
```
15.在dns解析服务商处，把解析地址写成为自己服务器的ip地址。访问https://www.cxpstudy.top即可。

16.优化建议
这种提示一般在NextCloud的服务器管理中可以看到，建议缓存类的直接安装一个即可，安装多了也没有什么用。
为了Nextcloud服务的安全和性能, 请将所有设置配置正确.
 
PHP 模块 ‘fileinfo’ 缺失. 我们强烈建议启用此模块以便在 MIME 类型检测时获得最准确的结果.
HTTP 请求头 “Strict-Transport-Security” 没有配置为至少 “15552000” 秒. 出于增强安全性考虑, 推荐按照安全提示中的说明启用HSTS.
 
内存缓存未配置. 如果可用, 需要配置 memcache 以增强性能.
PHP 的组件 OPcache 没有正确配置. 为了提供更好的性能, 我们建议在php.ini文件中使用下列设置:
 实际文件在：

```
[root@iZuf69goi7zjhqqki0418eZ etc]# vim /usr/share/doc/php70w-common-7.0.30/php.ini-development
[root@iZuf69goi7zjhqqki0418eZ etc]# vim /usr/share/doc/php70w-common-7.0.30/php.ini-production
```


```
opcache.enable=1
opcache.enable_cli=1
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=10000
opcache.memory_consumption=128
opcache.save_comments=1
opcache.revalidate_freq=1

```

16.1为nextcloud添加memcached缓存


```
修改nextcloud程序目录下的config目录中的config.php文件，在配置文件中添加如下，这个是多个Memcached实例，单个自己改：
  
'memcache.local' => '\OC\Memcache\APCu',
'memcache.distributed' => '\OC\Memcache\Memcached',
'memcached_servers' => array(
     array('localhost', 11211),
     array('server1.example.com', 11211),
     array('server2.example.com', 11211),
     ),
```

```
依据本篇如上安装记录，添加memcache缓存的方法（本机单机安装memcahced）
[root@nextcloud src]# yum -y install memcached
[root@nextcloud src]# cat /etc/sysconfig/memcached
PORT="11211"
USER="memcached"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS=""
[root@nextcloud src]# systemctl start memcached
[root@nextcloud src]# systemctl enable memcached
Created symlink from /etc/systemd/system/multi-user.target.wants/memcached.service to /usr/lib/systemd/system/memcached.service.
[root@nextcloud src]# lsof -i:11211
COMMAND      PID      USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
memcached 146026 memcached   26u  IPv4 3320544      0t0  TCP *:memcache (LISTEN)
memcached 146026 memcached   27u  IPv6 3320545      0t0  TCP *:memcache (LISTEN)
memcached 146026 memcached   28u  IPv4 3320549      0t0  UDP *:memcache
memcached 146026 memcached   29u  IPv6 3320550      0t0  UDP *:memcache
 
修改nextcloud的config配置文件，添加memcached缓存配置
[root@nextcloud config]# pwd
/usr/share/nginx/html/nextcloud/config
[root@nextcloud config]# cp config.php config.php.bak
[root@nextcloud config]# vim config.php
......
  'memcache.local' => '\OC\Memcache\APCu',
  'memcache.distributed' => '\OC\Memcache\Memcached',
  'memcached_servers' => array(
   array('localhost', 11211),
     ),
```

> 为nextcloud添加redis缓存
```
在nextcloud的config配置文件中添加如下，这个是通过TCP连接的：
'memcache.local' => '\OC\Memcache\Redis',
'redis' => array(
     'host' => 'localhost',
     'port' => 6379,
      ),
 
还有性能更好的UNIX连接：
'memcache.local' => '\OC\Memcache\Redis',
'redis' => array(
     'host' => '/var/run/redis/redis.sock',
     'port' => 0,
     'dbindex' => 0,
     'password' => 'secret',
     'timeout' => 1.5,
      ),
 
同时，官方还推荐加入如下，来用于存储文件锁：
'memcache.locking' => '\OC\Memcache\Redis',
```

```
1）修改php.ini上传文件大小限制
[root@nextcloud ~]# vim /etc/php.ini
......
max_execution_time = 0    #默认是30秒，改为0，表示没有限制
......
post_max_size = 10800M    #设定 POST 数据所允许的最大大小,如果POST数据尺寸大于post_max_size $_POST 和 $_FILES superglobals 便会为空.
......
upload_max_filesize = 10240M   #表示所上传的文件的最大大小
 
#另外要说明的是,post_max_size 大于 upload_max_filesize 为佳.
 
2）修改nginx.conf
[root@nextcloud ~]# vim /etc/nginx/conf.d/nextcloud.conf
.....
client_max_body_size 10240M;
 
3）重启php和nginx服务
[root@nextcloud ~]# systemctl restart php-fpm
[root@nextcloud ~]# systemctl restart nginx
```
