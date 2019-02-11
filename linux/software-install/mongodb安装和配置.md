> Mongodb 社区版源码

```
https://www.mongodb.com/download-center#community
```

> 下载源码包
```
mkdir -p /usr/local/mongodb/
cd /usr/local/mongodb/ && wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-4.0.1.tgz
# 解压源码包
tar -zxvf mongodb-linux-x86_64-4.0.1.tgz
# 移动 mongodb 到 /usr/local/mongodb/
cd mongodb-linux-x86_64-4.0.1
mv mongodb-linux-x86_64-4.0.1/* /usr/local/mongodb/
# 加入环境变量
export PATH=/usr/local///mongodb///bin:$PATH
# 创建配置文件
mkdir -p /etc/mongodb && vim /etc/mongodb/mongodb.conf
# 创建 mongodb 的数据目录
mkdir -p /data/mongodb/
# 创建 mongodb 的日志目录和文件
touch mongodb.log
# 编辑配置文件
vim /etc/mongodb/mongodb.conf

# 端口配置
port=27017
# 数据路径
dbpath=/data/mongodb/
# 日志路径
logpath=/data/mongodb.log
# 在后台运行
fork=true
# 日志以追加的方式写入
logappend=true
# mongodb的journal，简单来说就是用于数据故障恢复和持久化数据的，它以日志方式来记录。从1.8版本开始有此功能，2.0开始默认打开此功能，但32位的系统是默认关闭的。
journal=false
```
> 加入环境变量 ,仅为临时变量
```
export /usr/local/mongodb/bin/:$PATH
```

> 启动命令
```
./mongod -f /etc/mongodb/mongodb.conf
或者
./mongod --config /etc/mongodb/mongodb.conf
或者
mongod -f /etc/mongodb/mongodb.conf
或者
mongod --config /etc/mongodb/mongodb.conf
```
> 停止命令
```
./mongod --shutdown -f /etc/mongodb/mongodb.conf
```
> 连接命令
```
./mongo
或者
mongo
```
[mongodb入门](https://www.runoob.com/mongodb/mongodb-tutorial.html)



> 简易安装脚本
```
#!/bin/bash
mkdir -p /usr/local/mongodb/
mkdir -p /etc/mongodb
cd /usr/local/mongodb/ && wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-4.0.1.tgz
# 解压源码包
tar -zxvf mongodb-linux-x86_64-4.0.1.tgz
# 移动 mongodb 到 /usr/local/mongodb/
cd mongodb-linux-x86_64-4.0.1
mv /usr/local/mongodb/mongodb-linux-x86_64-4.0.1/* /usr/local/mongodb/
# 加入环境变量
`export PATH=/usr/local///mongodb///bin:$PATH`
# 创建 mongodb 的数据目录
mkdir -p /data/mongodb/
# 创建 mongodb 的日志目录和文件
touch /data/mongodb.log
echo 'port=27017
dbpath=/data/mongodb/
logpath=/data/mongodb.log
fork=true
logappend=true
journal=false'>> /etc/mongodb/mongodb.conf
/usr/local/mongodb/bin/mongod -f /etc/mongodb/mongodb.conf
mongo_result = `pidof mongod`
if [ ! $mongo_result ];then
    echo 'install mongodb failed'
else
    echo 'install mongodb successfully'
fi
```