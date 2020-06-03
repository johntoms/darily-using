# ELK 部署

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

## elasticsearch 安装
> [elasticsearch 安装文档](https://hub.docker.com/_/elasticsearch)


```
docker run -it -d --name elasticsearch --network elk-net \
 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" \ 
elasticsearch:7.6.2
```

## kibana 安装

```
docker run -d --name kibana --network elk-net -p 5601:5601 kibana:7.6.2

```
## logstash
```
# 没有配置文件
docker run -it -d --name logstash -p 5959:5959/udp -v /home/elk/logstash:/etc/logstash --network elk-net logstash:latest

```