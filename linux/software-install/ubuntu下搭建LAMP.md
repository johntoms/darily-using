> 1.更新apt-get源

```
root@wordpress:~# apt-get update
```
> 安装apache2
```
root@wordpress:~# apt-get install apache2 -y
```
> 安装mysql
```
root@wordpress:~# apt-get install mysql-server
```
> 安装php7.0
```
root@wordpress:~# apt-get install php7.0
#安装php依赖包
root@wordpress:~# apt-get install  libapache2-mod-php7.0 -y
root@wordpress:~# apt-get install php-mysql -y
```
> 检测是否安装成功


```
root@wordpress:~# php -v
PHP 7.0.30-0ubuntu0.16.04.1 (cli) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2017 Zend Technologies
    with Zend OPcache v7.0.30-0ubuntu0.16.04.1, Copyright (c) 1999-2017, by Zend Technologies
root@wordpress:~# service apache2 start
root@wordpress:~# service mysql start
```
> 安装lrzsz模块和unzip

```
root@wordpress:/var/www/html# apt-get install lrzsz unzip -y
```
> 将要搭建的wordpress包拖到/var/www/html/ ，并解压文件，修改wordpress所属用户和所属组为www-data

```
root@wordpress:/var/www/html# unzip wordpress-4.9.6.zip 
root@wordpress:/var/www/html# chown -R www-data :www-data wordpress
root@wordpress:/var/www/html# ll
total 9304
drwxr-xr-x 3 root     root        4096 May 27 19:54 ./
drwxr-xr-x 3 root     root        4096 May 27 19:31 ../
-rw-r--r-- 1 root     root       11321 May 27 19:31 index.html
drwxr-xr-x 5 www-data www-data    4096 May 27 20:04 wordpress/
-rw-r--r-- 1 root     root     9502138 May 26 11:26 wordpress-4.9.6.zip
```
> 访问IP/wordpress/ OK

> wordpress 证书配置

> 安装openssl
```
root@wordpress:/var/www/html# apt-get install openssl
```
> apache2配置文件详解
```
etc/apache2下的文件夹与文件
apache2.conf：Apache的主要配置文件，包含全局配置。
envvars：Apache2环境变量设置。
ports.conf：配置Apache监听的端口。
mods-available：这个目录包含模块和模块配置文件，不是所有的模块都有配置文件。
mods-enabled：持有/etc/apache2/mods-available目录下文件的链接，当该目录下有一个模块文件和其配置文件，那么Apache重启后该模块将生效。
sites-available：这个目录包含Apache虚拟主机的配置文件。虚拟主机允许Apache配置多个站点并为每个站点配置不同的参数。后面下面配置的时候会配置80端口的http重定向为443的https。
sites-enabled：持有/etc/apache2/sites-available目录下文件的链接。当Apache重启后，该目录中包含的站点将会被激活。
```
> 查看80和443端口是否开启
```
root@wordpress:/etc/apache2# vim ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 80

<IfModule ssl_module>
        Listen 443
</IfModule>

<IfModule mod_gnutls.c>
        Listen 443
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```
