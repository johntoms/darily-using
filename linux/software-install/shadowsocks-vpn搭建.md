0.pip的安装

(1)、首先检查linux有没有安装python-pip包，直接执行 
```
yum install python-pip
```



(2)、没有python-pip包就执行命令 
```
yum -y install epel-release
```



(3)、执行成功之后，再次执行
```
yum install python-pip
```



(4)、对安装好的pip进行升级 
```
pip install --upgrade pip
```


详情参见pip的安装


[link](https://note.youdao.com/)http://note.youdao.com/noteshare?id=7f8ea4c1e66d77e3cce359c9bec14b0e&sub=557F5F3E6401424CAA0157A091ADDBCB

1.pip安装shadowsocks



```
pip install shadowsocks
```


2.创建shadowsocks文件目录
```
mkdir /etc/shadowsocks
```


3.修改配置文件

```
vi /etc/shadowsocks/config.json
```


详情如下：

```
{
#配置服务器ip，填写0.0.0.0
“server”:"0.0.0.0",
#配置端口号和密#码
#可以采用多用户和单用户配置
#端口号尽量大些0~65536（特殊端口号不要用）
"port_password":{
"32150":"123456789",
"32151":"123456789",
"32152":"123456789",
"32153":"123456789"
                },
#超时时间
"timeout":300,
#加密算法
“method”：“aes-256-cfb”,
#true or false 开启后能降低延迟
"fast_open":false
}
```

正确代码如下：

```
{
"server":"0.0.0.0",
"port_password":{
"32150":"123456789",
"32151":"123456789",
"32152":"123456789",
"32153":"123456789"
                },
"timeout":300,
"method":"aes-256-cfb",
"fast_open":false
}
```


4.shadowsocks的重启停止和启动


```
sudo ssserver -c /etc/shadowsocks/config.json -d start/stop/restart
```

5.设置shadowsocks自动开机启动

```
vi /etc/rc.local
#在空格处键入下列命令
sudo ssserver -c /etc/shadowsocks/config.json -d start
```

6.开放对应端口的安全组
