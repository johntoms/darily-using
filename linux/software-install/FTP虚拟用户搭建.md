# vsftp概述
vsftp的用户有三种类型：匿名用户、系统用户、虚拟用户。

1）匿名登录：在登录FTP时使用默认的用户名，一般是ftp或anonymous。

2）本地用户登录：使用系统用户登录，在/etc/passwd中。

3）虚拟用户登录：这是FTP专有用户，有两种方式实现虚拟用户，本地数据文件和数据库服务器。

FTP虚拟用户是FTP服务器的专有用户，使用虚拟用户账号可以提供集中管理的FTP根目录，方便了管理员的管理，同时将用于FTP登录的用户名、密码与系统用户账号区别开，进一步增强了FTP服务器的安全性。某种意义上来说，匿名用户也是系统用户，只是系统用户的一个映射。公开的FTP都不会使用系统用户作为FTP帐号，而更多的采用了虚拟用户，这样能保证系统的安全性。使用虚拟用户登录FTP服务器，可以避免使用操作系统帐号作为FTP用户带来的一些安全问题，也便于通过数据库或其它程序来进行管理。虚拟用户的特点是只能访问服务器为其提供的FTP服务，而不能访问系统的其它资源。所以，如果想让用户对FTP服务器站内具有写权限，但又不允许访问系统其它资源，可以使用虚拟用户来提高系统的安全性。
## 权限配置
在VSFTP中，认证这些虚拟用户使用的是单独的口令库文件（pam_userdb），由可插入认证模块（PAM）认证。使用这种方式更加安全，并且配置更加灵活。

基本流程：FTP用户访问->PAM配置文件（由vsftpd.conf中pam_service_name指定）->PAM论证->区别用户读取配置文件（由vsftpd.conf中user_config_dir指定配置文件路径，文件名即用户名）


有两种方式建立FTP的虚拟用户，分别是：==本地数据文件方式、数据库服务器（MySQL）方式

### 安装及配置

```shell
yum install vsftpd -y      //ftp服务器 
yum install db4 -y         //虚拟用户存放密码和账号的数据库
```

#### 配置文件详解


```shell
anonymous_enable=NO        //不允许匿名账号访问
local_enable=YES           //本地用户可以访问(采用虚拟账号访问时，这个参数也要开启（虚拟账号要寄宿本地账号），虽然开启但是本地账号是不可以登陆的)
write_enable=YES          //可写可上传。这个参数是全局配置，否则上传和下载都会报错550！
allow_writeable_chroot=YES     //新版本特性，必须加上，不加会出现如下报错：
状态:	正在连接 60.205.0.65:2021...
状态:	连接建立，等待欢迎消息...
状态:	不安全的服务器，不支持 FTP over TLS。
命令:	USER hqsbcms
响应:	331 Please specify the password.
命令:	PASS ************************
响应:	500 OOPS: vsftpd: refusing to run with writable root inside chroot()

local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
xferlog_std_format=YES
ascii_upload_enable=YES
ascii_download_enable=YES
ftpd_banner=Welcome to FTP service   //登陆FTP时显示的欢迎信息
listen=YES
chroot_local_user=NO         //限制所有的本地用户在自家目录,即用户登陆系统后锁定在自家目录。虚拟主机配置下，在下面两个chroot配置后，这个参数必须为NO，否则登陆FTP后还可以访问其他目录！
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list  //指定不能离开家目录的用户列表文件，一行一个用户。使用此方法时必须chroot_local_user=NO。说明这个列表里面的用户登陆ftp后都只能访问其主目录，其他目录都不能访问！
pam_service_name=vsftpd        //指定PAM配置文件，即下面的/etc/pam.d/vsftpd文件要和这里指定的一致。
userlist_enable=YES
tcp_wrappers=YES
virtual_use_local_privs=YES       //这个参数一定要加上，虚拟用户和本地用户有相同的权限；否则ftp连上后不能上传，报错550权限拒绝！
guest_enable=YES             //启用虚拟用户
guest_username=nobody            //将虚拟用户映射为本地nobody用户（前提是local_enable=YES）
user_config_dir=/etc/vsftpd/vuser_conf      //指定不同虚拟用户配置文件的存放路径
           
connect_from_port_20=YES     //通过20端口传输数据
listen_port=2021               //监听的ftp端口
pasv_min_port=40001     //分配给ftp账号的最小端口。被动模式下的配置
pasv_max_port=40100    //分配给ftp账号的最大端口。每个账号分配一个端口，即最大允许100个ftp账号连接。
max_clients=150         //客户端的最大连接数
accept_timeout=5
connect_timeout=1
max_per_ip=5       //每个ip最大连接数
```
配置文件

```shell
anonymous_enable=NO
local_enable=YES
write_enable=YES
allow_writeable_chroot=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
xferlog_std_format=YES
ascii_upload_enable=YES
ascii_download_enable=YES
ftpd_banner=Welcome to FTP service
listen=YES
chroot_local_user=NO
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=YES
virtual_use_local_privs=YES
guest_enable=YES
guest_username=nobody
user_config_dir=/etc/vsftpd/vuser_conf
connect_from_port_20=YES
listen_port=2021
pasv_min_port=40001
pasv_max_port=40100
max_clients=150
accept_timeout=5
connect_timeout=1
max_per_ip=5
```
##### iptables配置
1.ftp是被动模式下的配置，配置后需要在iptables防火墙开通ftp访问

2.vim /etc/sysconfig/iptables-config


```
-A INPUT -s 60.68.250.13  //外网地址 -m state --state NEW -m tcp -p tcp --dport 2021 -j ACCEPT
-A INPUT -s 60.68.250.13  //外网地址 -m state --state NEW -m tcp -p tcp --dport 40001:40100 -j ACCEPT
```
> 虚拟用户的配置

设置登陆ftp的虚拟账号文件（格式依次是：第一行是账户名，次行是该账号的密码；即奇数行是账户名，偶数行是对应上一行的账户密码）。
这个虚拟账号是不需要手动创建的，它不是真实存在于系统中的，即/etc/passwd文件里没有的，它是借助于宿主账号nobody。

1.创建用户


```shell
vim /etc/vsftpd/vuser_password.txt
```


```shell
cat /etc/vsftpd/vuser_password.txt

hqsbcms
hqsbcms_2016@huanqiu.com

```
> 生成虚拟用户口令认证的db文件（该文件设定600权限）,这是本地数据库文件


```shell
db_load -T -t hash -f /etc/vsftpd/vuser_passwd.txt /etc/vsftpd/vuser_passwd.db
```
> 修改vuser_password.db权限为600

```shell
chmod 600 /etc/vsftpd/vuser_passwd.db
```
> 创建chroot_list文件，将虚拟用户放在这个列表文件里，说明这些用户登陆后都只能锁定到对应主目录内


```shell
cat /etc/vsftpd/chroot_list

hqsbcms
```
> 创建vuser_conf目录，目录名是在vsftpd.conf配置中指定的，里面是虚拟用户配置文件（文件名是虚拟用户名）


```shell

pwd:/etc/vsftpd/

mkdir vuser_conf
```
> 在vuser_conf下创建hqsbcms用户的配置文件


```shell
pwd:/etcvsftpd/vuser_conf/

cat hqsbcms

local_root=/hqsb/ftp/       //指定虚拟账号登陆后的主目录，目录权限要是宿主账号nobody，这样就可以实现账号映射
write_enable=YES       //写权限
anon_umask=022
anon_world_readable_only=NO  //下载权限（当其他四项的YES为NO时，则此账号登陆FTP后只有可读和下载权限了）
anon_upload_enable=YES   //上传权限
anon_mkdir_write_enable=YES    //创建目录权限
anon_other_write_enable=YES    //删除和重命名权限

```
> 配置文件hqsbcms代码如下：

```shell
local_root=/hqsb/ftp/
write_enable=YES
anon_umask=022
anon_world_readable_only=NO
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
#download_enable=YES
```
> 配置 /etc/pam.d/vsftpd
```shell
[root@iZ2ze7nfzlqbc8nu1x0bg0Z vsftpd]# ll /lib64/security/pam_userdb.so
-rwxr-xr-x 1 root root 15392 Nov  6  2016 /lib64/security/pam_userdb.so
```

```shell
cat /etc/pam.d/vsftpd       //注释掉文件中原来的内容，添加下面两行内容
#%PAM-1.0
#session optional pam_keyinit.so force revoke
#auth required pam_listfile.so item=user sense=deny file=/etc/vsftpd/ftpusers onerr=succeed
#auth required pam_shells.so
#auth include password-auth
#account include password-auth
#session required pam_loginuid.so
#session include password-auth
# 32-bit
#auth required /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd
#account required /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd
# 64-bit
auth sufficient /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd          //这个vuser_passwd根据的是vuser_passwd.db
account sufficient /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd       //这里64bit系统，必须用sufficient，否则上面vuser_conf目录下的虚拟主机配置文件无效！
```
> /etc/pam.d/vsftpd 所要添加的内容

```shell
[root@iZ2ze7nfzlqbc8nu1x0bg0Z vsftpd]# cat /etc/pam.d/vsftpd
#%PAM-1.0
#session    optional     pam_keyinit.so    force revoke
#auth       required	pam_listfile.so item=user sense=deny file=/etc/vsftpd/ftpusers onerr=succeed
#auth       required	pam_shells.so
#auth       include	password-auth
#account    include	password-auth
#session    required     pam_loginuid.so
#session    include	password-auth
auth sufficient /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd
account sufficient /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd
```

```shell
cat /etc/passwd|grep nobody      //宿主账号nobody的信息不用做任何修改，shell类型是不是/sbin/nologin都可以，不影响ftp登陆限制到主目录下，因为vsfprd里配置了三个chroot。
nobody:x:99:99:Nobody:/:/sbin/nologin
```

```shell
chown -R nobody.nobody /hqsb/ftp     //设置虚拟账号hqsbcms指定的主目录的权限为nobody，这样就可以映射到宿主账号nobody
```

```shell
#在根目录下创建  /hqsb/ftp/

mkdir -p /hqsb/ftp/

chmod -R 700 /hqsb/ftp
```

> 启动vsftpd


```shell
service vsftpd start
```
-----------------------------------------

vsftpd进程启动报错：
starting vsftpd for vsftpd: 500 OOPS: bad bool value in config file for: anonymous_enable
> 处理办法：
> 要保证vsftpd.conf文件里每行的配置后面都不要有空格。
>  
> 解决：
> vim编辑/etc/vsftpd/vsftpd.conf文件，在尾行模式下输入“:%s/\s\+$”，然后回车即可。


```shell
备注：
vim删除行首行尾空格和tab的命令如下（非编辑状态下输入）：
:%s/^\s\+         删除行首的空格和tab
:%s/\s\+$         删除行尾的空格和tab

上面两条命令的解释：
%s          表示全局搜索
/             为分隔符。
^            代表行首
\s            代表空格和tab
\+           代表匹配一个或多个
$             匹配行尾
```
问题一：在ftp客户端（比如FileZilla）进行连接，发现连接失败，无法连接到服务器！

原因及解决：由于ftp配置中采用的是被动模式，而客户端连接默认的是主动模式。所以需要手动修改下客户端的默认配置。修改如下：
依次点击FileZilla客户端左上角的"文件"->"站点管理器"->"新建站点"

这样，就能正常连接上FTP服务器了。以后每次连接的时候，就依次打开左上角"文件"->"站点管理器"里之前设置并保存好的站点就行（如上面的185.5-ftp站点）。使用上诉虚拟账号登陆ftp后，只能登陆到其设置的主目录/hqsb/ftp下，服务器上的其他目录资源都不能访问！


```markdown
温馨提示：
浏览器访问只支持FTP的被动模式，也就是说只有在FTP配置成被动模式时，才能在远程浏览器里通过url访问。比如上面配置后，可以通过web访问ftp://103.110.186.5:2021/
```
>== 使用ssl加密传输==（不再使用明文传输）


```shell
pwd:/etc/vsftpd/
[root@iZ2ze7nfzlqbc8nu1x0bg0Z vsftpd]# mkdir /etc/vsftpd/sslkey
[root@iZ2ze7nfzlqbc8nu1x0bg0Z vsftpd]# cd /etc/vsftpd/sslkey/

[root@iZ2ze7nfzlqbc8nu1x0bg0Z sslkey]# openssl req -new -x509 -nodes -out vsftpd.pem -keyout vsftpd.pem
Generating a 2048 bit RSA private key
........................................+++
................................................................................................................+++
writing new private key to 'vsftpd.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:CN
State or Province Name (full name) []:Beijing
Locality Name (eg, city) [Default City]:BeiJing
Organization Name (eg, company) [Default Company Ltd]:YueXin
Organizational Unit Name (eg, section) []:technology
Common Name (eg, your name or your server's hostname) []:YueXin
Email Address []:cxptest@test.com

[root@iZ2ze7nfzlqbc8nu1x0bg0Z sslkey]# ls
vsftpd.pem
[root@iZ2ze7nfzlqbc8nu1x0bg0Z sslkey]# vim /etc/vsftpd/vsftpd.conf
// 重启vsftpd服务
[root@iZ2ze7nfzlqbc8nu1x0bg0Z sslkey]# service vsftpd restart
Redirecting to /bin/systemctl restart  vsftpd.service
```
> 添加虚拟账号


```shell
比如添加账号ops（密码为ops@123），指定目录为/mnt/ops，操作如下：
[root@bastion-IDC vsftpd]# pwd
/etc/vsftpd
[root@bastion-IDC vsftpd]# cat chroot_list
hqsbcms
ops
 
[root@bastion-IDC vsftpd]# cat vuser_passwd.txt
hqsbcms
hqsbcms_2016@huanqiu.com
ops
ops@123
 
[root@bastion-IDC vsftpd]# db_load -T -t hash -f /etc/vsftpd/vuser_passwd.txt /etc/vsftpd/vuser_passwd.db
 
[root@bastion-IDC vsftpd]# cat vuser_conf/ops
local_root=/mnt/ops/
write_enable=YES
anon_umask=022
anon_world_readable_only=NO
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
 
[root@bastion-IDC vsftpd]# chown -R nobody.nobody /mnt/ops
[root@bastion-IDC vsftpd]# chmod -R 777 /mnt/ops
 
照此操作就可以添加FTP虚拟账号了，每个虚拟账号可以对应一个主目录，并且限定到只能ftp访问该主目录
------------------------------------------------------------
 
如果想让虚拟账号ops权限为只读以及只能下载（没有上传、删除、重命名、创建文件目录等写权限），那么它的配置修改如下：
[root@bastion-IDC vsftpd]# cat vuser_conf/ops
local_root=/mnt/ops/
write_enable=NO
anon_umask=022
anon_world_readable_only=NO
anon_upload_enable=NO
anon_mkdir_write_enable=NO
anon_other_write_enable=NO
```
