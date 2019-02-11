-  一、安装前准备

首先检查VPS上的tun设备是否可用，如果不可用需要联系客服打开，否则OpenVPN无法启用。
通过root用户登陆，执行

```
cat /dev/net/tun
cat: /dev/net/tun: File descriptor in bad state
```

如果现实结果如上所示，则表示tun设备可用，其它则表示设备异常，无法安装OpenVPN。

- 二、安装方法
> 2.1 使用yum安装程序所需开发包

```
yum install -y openssl openssl-devel automake pkgconfig iptables
```


> 2.2 安装pkcs11-helper RPM包

```
rpm -ivh pkcs11-helper-1.07-2.el5.1.i386.rpm
rpm -ivh pkcs11-helper-devel-1.07-2.el5.1.i386.rpm
```


> 2.3  安装 LZO

```
rpm -ivh pkcs11-helper-1.07-2.el5.1.i386.rpm
rpm -ivh pkcs11-helper-devel-1.07-2.el5.1.i386.rpm
```


> 2.4  安装 OpenVPN

```
tar zxvf openvpn-2.1.4.tar.gz
cd openvpn-2.1.4
./configure --prefix=/opt/openvpn --with-lzo-headers=/opt/lzo/include --with-lzo-lib=/opt/lzo/lib --with-ssl-headers=/usr/include/openssl --with-ssl-lib=/usr/lib
make
make install
```


> 2.5 下面就开始key证书文件的创建，总共需要创建三个，即ca，server key，client key

> 2.5.1 生成证书Key

```
cp -r easy-rsa /opt/openvpn/
cd /opt/openvpn/easy-rsa/2.0/

vim export_new_var
export D=`pwd`
export KEY_CONFIG=$D/openssl.cnf
export KEY_DIR=$D/keys
export KEY_SIZE=1024
export KEY_COUNTRY=CN
export KEY_PROVINCE=SH
export KEY_CITY=PD
export KEY_ORG="zcc.com"
export KEY_EMAIL="root@zcc.com"

source export_new_var
./clean-all
./build-ca
```

> 2.5.2 建立 server key

```
./build-key-server server
```


> 生成客户端 key

```
./build-key client1
```
> 备注：
如果想生成多个client key的话，重复以上步骤，修改client1为client2，client3……即可

> 至此，所有的key都已经生成完毕，如果你想删除这些key，重新生成的话，执行以下命令。

```
source vars
./clean-all
```

> 生成 Diffie Hellman 参数

```
vim build-dh
```


```
$OPENSSL 修改成 openssl 或者在开头添加OPENSSL=`which openssl`

将 keys 下的所有文件打包下载到本地
tar -cf keys.tar keys
```

> 2.5.3 创建服务端配置文件

```
vi /opt/openvpn/etc/server.conf
port 1195
proto udp
dev tun
ca /opt/openvpn/easy-rsa/2.0/keys/ca.crt
cert /opt/openvpn/easy-rsa/2.0/keys/server.crt
key /opt/openvpn/easy-rsa/2.0/keys/server.key
dh /opt/openvpn/easy-rsa/2.0/keys/dh1024.pem
server 10.10.20.0 255.255.255.0
client-to-client
keepalive 10 120
comp-lzo
persist-key
persist-tun
status /opt/openvpn/easy-rsa/2.0/keys/openvpn-status.log
verb 4

push "route 0.0.0.0 0.0.0.0"
push "redirect-gateway def1 bypass-dhcp"

#推送vpn的网关作为客户端的网关，需要配合iptables使用，添加两条iptables：
iptables -t nat -A POSTROUTING -s 10.10.20.0/24 -o eth0 -j MASQUERADE
iptables -A INPUT -p udp -m udp --dport 1195 -j ACCEPT
FORWARD 里面不可以阻止所有，或者清空FORWARD
#开启转发
sysctl -w net.ipv4.ip_forward=1

push "dhcp-option DNS 10.10.20.1"
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"
```

- 三、启动openvpn

```
/opt/openvpn/sbin/openvpn --config /opt/openvpn/etc/server.conf > /dev/null 2>&1 &
```

- 四、客户端配置client.ovpn

> 创建客户端配置文件,这一步是在客户端设置的，不需要在服务器设置

```
client
dev tun
proto udp
remote 210.209.70.204 1195 #ip为openvpn的ip地址
persist-key
persist-tun
ca ca.crt
cert client1.crt
key client1.key
ns-cert-type server
comp-lzo
verb 3
redirect-gateway def1 #此行是不需要的，才可以正常，有待于进一步研究
route-method exe
route-delay 2
```


- 五、卸载OpenVPN

如果你觉得OpenVPN用起来太过于麻烦或其它原因想卸载OpenVPN，那么，请执行以下操作。


```
killall openvpn
rpm -e pkcs11-helper-1.07-2.el5.1.i386.rpm
rpm -e pkcs11-helper-devel-1.07-2.el5.1.i386.rpm

rm -rf /opt/lzo
rm -rf /opt/openvpn
```
