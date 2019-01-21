- 简介
- 安装过程
  - 准备工作
  - 安装依赖
  - 设置gitlab安装源
  - 安装gitlab
- SSL配置
- 常用命令
  - 服务管理
  - 运维管理
  - 日志排查
- 备份与恢复



## 简介

GitLab 是一个利用Ruby on Rails 开发的开源版本控制系统，实现一个自托管的Git项目仓库，可通过Web界面进行访问公开的或者私人项目。

它拥有与GitHub类似的功能，能够浏览源代码，管理缺陷和注释。可以管理团队对仓库的访问，它非常易于浏览提交过的版本并提供一个文件历史库。团队成员可以利用内置的简单聊天程序（Wall）进行交流。它还提供一个代码片段收集功能可以轻松实现代码复用，便于日后有需要的时候进行查找。

开源中国代码托管平台 [码云](http://git.oschina.net/) 就是基于GitLab项目搭建。

GitLab 分为 GitLab Community Edition(CE) 社区版 和 GitLab Enterprise Edition(EE) 专业版。社区版免费，专业版收费，两个版本在功能上的差异对比，可以参考[官方对比说明](https://about.gitlab.com/features/#compare)。

## 安装过程

本文以RedHat系为例，更多安装方法参考：<https://about.gitlab.com/installation/>

- 准备工作

以CentOS7为例，推荐配置至少内存4G.

- 安装依赖

~~~markdown
---------------------------------------------------------------------------------------
sudo yum install -y curl policycoreutils-python openssh-server
sudo systemctl enable sshd
sudo systemctl start sshd
sudo firewall-cmd --permanent --add-service=http
sudo systemctl reload firewalld

sudo yum install postfix
sudo systemctl enable postfix
sudo systemctl start postfix

---------------------------------------------------------------------------------------
注意：
> 1.postfix启动出现 fatal: parameter inet ··· 错误。

[root@iZbp1h5pmg6spg0eodt4laZ ~]# sudo systemctl start postfix
Job for postfix.service failed because the control process exited with error code. See "systemctl status postfix.service" and "journalctl -xe" for details.
[root@iZbp1h5pmg6spg0eodt4laZ ~]# systemctl status postfix.service
● postfix.service - Postfix Mail Transport Agent
   Loaded: loaded (/usr/lib/systemd/system/postfix.service; enabled; vendor preset: disabled)
   Active: failed (Result: exit-code) since 六 2018-09-15 14:48:32 CST; 23s ago
  Process: 1856 ExecStart=/usr/sbin/postfix start (code=exited, status=1/FAILURE)
  Process: 1854 ExecStartPre=/usr/libexec/postfix/chroot-update (code=exited, status=0/SUCCESS)
  Process: 1851 ExecStartPre=/usr/libexec/postfix/aliasesdb (code=exited, status=75)

9月 15 14:48:30 iZbp1h5pmg6spg0eodt4laZ systemd[1]: Starting Postfix Mail Tr...
9月 15 14:48:30 iZbp1h5pmg6spg0eodt4laZ aliasesdb[1851]: /usr/sbin/postconf:...
9月 15 14:48:31 iZbp1h5pmg6spg0eodt4laZ aliasesdb[1851]: newaliases: fatal: ...

▽
9月 15 14:48:31 iZbp1h5pmg6spg0eodt4laZ postfix[1856]: fatal: parameter inet...
9月 15 14:48:32 iZbp1h5pmg6spg0eodt4laZ systemd[1]: postfix.service: control...
9月 15 14:48:32 iZbp1h5pmg6spg0eodt4laZ systemd[1]: Failed to start Postfix ...
9月 15 14:48:32 iZbp1h5pmg6spg0eodt4laZ systemd[1]: Unit postfix.service ent...
9月 15 14:48:32 iZbp1h5pmg6spg0eodt4laZ systemd[1]: postfix.service failed.
Hint: Some lines were ellipsized, use -l to show in full.

**解决方案**：
1. 查看centos的postfix日志
[root@iZbp1h5pmg6spg0eodt4laZ sbin]# more  /var/log/maillog
Sep 15 14:44:24 localhost postfix/sendmail[961]: fatal: parameter inet_interface
s: no local interface found for ::1
Sep 15 14:44:24 localhost postfix[967]: fatal: parameter inet_interfaces: no loc
al interface found for ::1
Sep 15 14:48:31 localhost postfix/sendmail[1853]: fatal: parameter inet_interfac
es: no local interface found for ::1
Sep 15 14:48:31 localhost postfix[1856]: fatal: parameter inet_interfaces: no lo
cal interface found for ::1
Sep 15 14:49:38 localhost postfix/sendmail[1883]: fatal: parameter inet_interfac
es: no local interface found for ::1
Sep 15 14:49:38 localhost postfix[1887]: fatal: parameter inet_interfaces: no lo
cal interface found for ::1

2. vim /etc/postfix/main.cf
修改
inet_interfaces = localhost

inet_protocols = all

为

inet_interfaces = all

inet_protocols = all

即可。

----------------------------------------------------------------------------------
> 2. /var/spool/postfix 目录无权限问题

[root@linux115 spool]# service postfix start
启动 postfix： [失败]

[root@linux115 log]# postfix start
postsuper: fatal: scan_dir_push: open directory defer: Permission denied
postfix/postfix-script: fatal: Postfix integrity check failed!
[root@linux115 log]# postfix check
postsuper: fatal: scan_dir_push: open directory defer: Permission denied

1.查看日志文件
```
more /var/log/maillog
```
有如下两行：
May 26 09:01:51 linux115 postfix/postsuper[6199]: fatal: scan_dir_push: open directory defer: Permission denied
May 26 09:01:52 linux115 postfix/postfix-script[6200]: fatal: Postfix integrity check failed!


问题原因：
那是/var/spool/postfix 这个目录拥有都权限的问题，原来默认的拥有都是root，需要将拥有者改为postfix，如（1）


解决命令：
（1）
[root@linux115 spool]# chown -R postfix:postfix /var/spool/postfix/

[root@linux115 spool]# service postfix start
启动 postfix： [确定]
~~~

- 设置gitlab安装源

官方源安装方法：

```
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
```

由于网络问题，国内推荐使用清华大学镜像源进行安装：

```
cat>/etc/yum.repos.d/gitlab-ce.repo<<'EOF'
[gitlab-ce]
name=Gitlab CE Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el$releasever/
gpgcheck=0
enabled=1
EOF
```

- 安装GitLab

首先可以设置域名，域名需要保证能够正常解析，可以根据使用场景选择公网域名或者是本地hosts测试。

```shell
sudo EXTERNAL_URL="http://gitlab.ikiwi.me" yum install -y gitlab-ce
```

也可以不设置域名，域名绑定可以随时在配置文件`/etc/gitlab/gitlab.rb`里进行修改：

```shell
external_url 'http://gitlab.xxx.com'
```

直接安装：

```shell
sudo yum install -y gitlab-ce
```

安装完成以后，运行下面的命令进行配置：

```shell
sudo gitlab-ctl reconfigure
```

- 安装完成

  ![安装 gitlab 完成](http://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/gitlab%E6%90%AD%E5%BB%BA-%E5%AE%89%E8%A3%85%E5%AE%8C%E6%88%90.png)



>  注意

1. sudo gitlab-ctl reconfigure

   **我的服务器器为 1 核 1 G。服务跑起来，未作任何操作，内存偶尔已占到 90% ，内存请至少为 2 核 4G ，才能够保证服务的可用性。**

   出现如下报错

   ```shell
   Running handlers:
   There was an error running gitlab-ctl reconfigure:
   
   storage_directory[/var/opt/gitlab/git-data] (gitlab::gitlab-rails line 44) had an error: Errno::ENOMEM: ruby_block[directory resource: /var/opt/gitlab/git-data] (/opt/gitlab/embedded/cookbooks/cache/cookbooks/package/resources/storage_directory.rb line 33) had an error: Errno::ENOMEM: Cannot allocate memory - fork(2)
   
   Running handlers complete
   Chef Client failed. 1 resources updated in 28 seconds
   [root@iZbp1h5pmg6spg0eodt4laZ gitlab]# sudo gitlab-ctl reconfigure
   Starting Chef Client, version 13.6.4
   
   Running handlers:
   There was an error running gitlab-ctl reconfigure:
   
   Unable to determine node name: configure node_name or configure the system's hostname and fqdn
   
   Running handlers complete
   Chef Client failed. 0 resources updated in 11 seconds
   ```

   解决方案：

   扩大内存，建议内存至少为 2 核 4 G 。

   > 确认 gitlab 是否运行

   ```shell
   # 1.使用netstat  lnutp 查看端口已被监听
   [root@iZbp141zpwm5zf3knma42kZ ~]# netstat -luntp
   Active Internet connections (only servers)
   Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
   tcp        0      0 127.0.0.1:9100          0.0.0.0:*               LISTEN      12387/node_exporter
   tcp        0      0 127.0.0.1:9229          0.0.0.0:*               LISTEN      12678/gitlab-workho
   tcp        0      0 127.0.0.1:9168          0.0.0.0:*               LISTEN      12726/ruby
   tcp        0      0 127.0.0.1:8080          0.0.0.0:*               LISTEN      12172/unicorn maste
   tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      12224/nginx: master
   tcp        0      0 127.0.0.1:8082          0.0.0.0:*               LISTEN      12187/sidekiq 5.1.3
   tcp        0      0 127.0.0.1:9236          0.0.0.0:*               LISTEN      12696/gitaly
   tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      10700/sshd
   tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      10919/master
   tcp        0      0 0.0.0.0:8060            0.0.0.0:*               LISTEN      12224/nginx: master
   tcp        0      0 127.0.0.1:32000         0.0.0.0:*               LISTEN      10498/java
   tcp        0      0 127.0.0.1:9121          0.0.0.0:*               LISTEN      12506/redis_exporte
   tcp        0      0 127.0.0.1:9090          0.0.0.0:*               LISTEN      12739/prometheus
   tcp        0      0 127.0.0.1:9187          0.0.0.0:*               LISTEN      12781/postgres_expo
   tcp        0      0 127.0.0.1:9093          0.0.0.0:*               LISTEN      12757/alertmanager
   tcp6       0      0 :::25                   :::*                    LISTEN      10919/master
   tcp6       0      0 :::9094                 :::*                    LISTEN      12757/alertmanager
   udp        0      0 0.0.0.0:46502           0.0.0.0:*                           723/dhclient
   udp        0      0 0.0.0.0:68              0.0.0.0:*                           723/dhclient
   udp        0      0 192.168.0.237:123       0.0.0.0:*                           835/ntpd
   udp        0      0 127.0.0.1:123           0.0.0.0:*                           835/ntpd
   udp        0      0 0.0.0.0:123             0.0.0.0:*                           835/ntpd
   udp6       0      0 :::9094                 :::*                                12757/alertmanager
   udp6       0      0 :::123                  :::*                                835/ntpd
   udp6       0      0 :::26909                :::*                                723/dhclient
   
   ```

   ```shell
   # 2. 网页端测试
   # a. 如果您的域名已经解析到服务器，可以直接访问域名
   # b. 如果没有解析的话，可以在域名解析控制台设置解析，亦或是直接在浏览器中输入 公网 ip 查看 ， 如：http://47.97.206.180
   
   # 3. 关于域名解析，不是本文的重点，在这里不做赘述，如果您的域名是在阿里云购买的，请参考：设置域名解析 https://help.aliyun.com/document_detail/29716.html?spm=5176.11065259.1996646101.searchclickresult.4ba232c9yTCxEP，如果有疑问，请提交工单进行咨询。请提交工单进行咨询。其他运营商的域名请联系域名供应商。
   ```

![gitlab 网页端展示](http://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/gitlab%E6%90%AD%E5%BB%BA-%E7%BD%91%E9%A1%B5%E7%AB%AF.png)

## SSL配置

GitLab默认是使用HTTP的，可以手动配置为HTTPS.

- 上传SSL证书

创建ssl目录，用于存放SSL证书

```
# mkdir -p /etc/gitlab/ssl
# chmod 0700 /etc/gitlab/ssl
```

上传证书并修改证书权限

```
# chmod 600 /etc/gitlab/ssl/*
```

- 修改GitLab的配置文件

修改配置文件`/etc/gitlab/gitlab.rb`

```
external_url "https://gitlab.xxx.com"
nginx['redirect_http_to_https'] = true
nginx['ssl_certificate'] = "/etc/gitlab/ssl/gitlab.xxx.com.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/gitlab.xxx.com.key"
```

- 重建配置，使其生效

```
# gitlab-ctl reconfigure
```

以上操作后，GitLab自带的Nginx服务的配置文件 `/var/opt/gitlab/nginx/conf/gitlab-http.conf` 会被重新修改：

```shell
server {
 listen *:80;
 server_name gitlab.xxx.com;
 server_tokens off; ## Don't show the nginx version number, a security best practice
 return 301 https://gitlab.xxx.com:443$request_uri;
 access_log /var/log/gitlab/nginx/gitlab_access.log gitlab_access;
 error_log   /var/log/gitlab/nginx/gitlab_error.log;
}
```

**证书配置**

![gitlab搭建-证书配置](http://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/gitlab%E6%90%AD%E5%BB%BA-%E8%AF%81%E4%B9%A6%E9%85%8D%E7%BD%AE.png)

```shell
server {
    listen 443;
    server_name localhost;
    ssl on;
    root html;
    index index.html index.htm;
    ssl_certificate   cert/cxpstudy.pem;
    ssl_certificate_key  cert/cxpstudy.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    location / {
        root html;
        index index.html index.htm;
    }
}

# 此为注释不要写到配置文件中
# 必须配置选项如下：
#ssl_certificate   cert/cxpstudy.pem;
#ssl_certificate_key  cert/cxpstudy.key;
#ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
#ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
#ssl_prefer_server_ciphers on;
```

不用额外再配置，HTTP 会自动跳转到 HTTPS 。记得要对外放行443端口。



**如果有证书的更换，必须要重启才会生效，如果是第一次配置则不用重启，会自动生效。**

```shell
gitlab服务重启
gitlab-ctl restart
gitlab重新加载配置文件
gitlab-ctl reconfigure
```

>  https配置成功

![gitlab-https配置成功](http://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/gitlab-https%E9%85%8D%E7%BD%AE.png)

## 常用命令

### 服务管理

```shell
# 启动所有 gitlab 组件：
gitlab-ctl start
# 停止所有 gitlab 组件：
gitlab-ctl stop
# 停止所有 gitlab postgresql 组件：
gitlab-ctl stop postgresql
# 停止相关数据连接服务
gitlab-ctl stop unicorn
gitlab-ctl stop sidekiq
# 重启所有 gitlab 组件：
gitlab-ctl restart
# 重启所有 gitlab gitlab-workhorse 组件：
gitlab-ctl restart gitlab-workhorse
# 查看服务状态
gitlab-ctl status
# 生成配置并启动服务
gitlab-ctl reconfigure
```

### 运维管理

```shell
# 查看版本
cat /opt/gitlab/embedded/service/gitlab-rails/VERSION
# 检查gitlab
gitlab-rake gitlab:check SANITIZE=true --trace
# 实时查看日志
gitlab-ctl tail
# 数据库关系升级
gitlab-rake db:migrate
# 清理redis缓存
gitlab-rake cache:clear
# 升级GitLab-ce 版本
yum update gitlab-ce
# 升级PostgreSQL最新版本
gitlab-ctl pg-upgrade
```

### 日志排查

```shell
# 实时查看所有日志
gitlab-ctl tail
# 实时检查redis的日志
gitlab-ctl tail redis
# 实时检查postgresql的日志
gitlab-ctl tail postgresql
# 检查gitlab-workhorse的日志
gitlab-ctl tail gitlab-workhorse
# 检查logrotate的日志
gitlab-ctl tail logrotate
# 检查nginx的日志
gitlab-ctl tail nginx
# 检查sidekiq的日志
gitlab-ctl tail sidekiq
# 检查unicorn的日志
gitlab-ctl tail unicorn
```



## 备份与恢复

GitLab作为公司项目代码的版本管理系统，数据非常重要，所以应做好备份工作。

### 修改备份目录

GitLab备份的默认目录是`/var/opt/gitlab/backups` ，如果想改备份目录，可修改`/etc/gitlab/gitlab.rb`：

```
gitlab_rails['backup_path'] = '/data/backups'
```

修改配置后，记得：

```
gitlab-ctl reconfigure
```

### 备份命令

```
gitlab-rake gitlab:backup:create
```

该命令会在备份目录（默认：/var/opt/gitlab/backups/）下创建一个tar压缩包xxxxxxxx_gitlab_backup.tar，其中开头的xxxxxx是备份创建的时间戳，这个压缩包包括GitLab整个的完整部分。

### 自动备份

通过任务计划crontab 实现自动备份

```
# 每天2点备份gitlab数据
0 2 * * * /usr/bin/gitlab-rake gitlab:backup:create
```

### 备份保留7天

可设置只保留最近7天的备份，编辑配置文件`/etc/gitlab/gitlab.rb`

```shell
# 数值单位：秒
gitlab_rails['backup_keep_time'] = 604800
```

重新加载gitlab配置文件

```shell
gitlab-ctl reconfigure
```

### 恢复

备份文件：

```
/var/opt/gitlab/backups/1499244722_2017_07_05_9.2.6_gitlab_backup.tar
```

停止 unicorn 和 sidekiq ，保证数据库没有新的连接，不会有写数据情况。

```shell
# 停止相关数据连接服务
gitlab-ctl stop unicorn
gitlab-ctl stop sidekiq

# 指定恢复文件，会自动去备份目录找。确保备份目录中有这个文件。
# 指定文件名的格式类似：1499242399_2017_07_05_9.2.6，程序会自动在文件名后补上：“_gitlab_backup.tar”
# 一定按这样的格式指定，否则会出现 The backup file does not exist! 的错误
gitlab-rake gitlab:backup:restore BACKUP=1499242399_2017_07_05_9.2.6

# 启动Gitlab
gitlab-ctl start
```

