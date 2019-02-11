**（一）、*安装docker***

1.Docker要求centos系统的内核版本高于3.10，查看本页面的前提条件来验证你的CentOS 版本是否支持 Docker 。

2.查看系统内核

```
[root@iZ2ze9tso4j4i1xrit3jhgZ ~]# uname -r
3.10.0-514.26.2.el7.x86_64
```

3.确保yum包更新到最新

```
sudo yum update
```

4.卸载旧版本（如果安装旧版本的话）

```
sudo yum remove docker  docker-common docker-selinux docker-engine
```

5.安装依赖包

```
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

6.设置yum源

```
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

7.查看仓库中的所有docker版本，选定自己所须得版本。

```
yum list docker-ce --showduplicates | sort -r
```

8.安装docker

```
sudo yum install docker-ce  #由于repo中默认只开启stable仓库，故这里安装的是最新稳定版17.12.0
$ sudo yum install <FQPN>  # 例如：sudo yum install docker-ce-17.12.0.ce
```

9.测试docker

```
[root@iZ2ze9tso4j4i1xrit3jhgZ ~]# docker -v
Docker version 18.03.1-ce, build 9ee9f40

systemctl start docker
systemctl enable docker  //加入开机自启
```

（二）、问题

因为之前已经安装过旧版本的docker，在安装的时候报错如下：

```
Transaction check error:
  file /usr/bin/docker from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/docker-containerd from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/docker-containerd-shim from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/dockerd from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
```

```
sudo yum erase docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
```

再次安装docker。