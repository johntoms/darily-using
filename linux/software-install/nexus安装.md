# nexus 部署

# docker 安装
## docker 安装
1. [docker 安装文档](https://docs.docker.com/engine/install/)
2. 更改 docker 镜像源

```
# 修改或新增 /etc/docker/daemon.json

$ vi /etc/docker/daemon.json

{

"registry-mirrors": ["http://hub-mirror.c.163.com"]

}

$ systemctl restart docker.service
```

## nexus 安装
> [docker 安装 nexus](https://hub.docker.com/r/sonatype/nexus3/)
```bash
# 简单测试
$ docker run -d -p 8081:8081 --name nexus sonatype/nexus3

# 数据目录映射到主机中
$ mkdir /home/nexus/nexus-data && chown -R 200 /home/neuxs/nexus-data
$ docker run -d -p 8081:8081 --name nexus -v /home/nexus/nexus-data:/nexus-data sonatype/nexus3
```
