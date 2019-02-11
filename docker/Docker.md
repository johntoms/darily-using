# Docker

## Docker简介

### Docker应用场景

- Web 应用的自动化打包和发布。
- 自动化测试和持续集成、发布。
- 在服务型环境中部署和调整数据库或其他的后台应用。
- 从头编译或者扩展现有的OpenShift或Cloud Foundry平台来搭建自己的PaaS环境。

------

### 检查版本

```bash
$ docker --version
Docker version 18.03, build c97c6d6

$ docker-compose --version
docker-compose version 1.22.0, build 8dd22a9

$ docker-machine --version
docker-machine version 0.14.0, build 9ba6da9
```

### 安装nginx

```bash
docker run -d -p 80:80 --name webserver nginx
```

### 查看容器内的详情

```bash
docker ps -a /--all  #cat all container
$ docker container ls
$ docker container stop webserver
$ docker container ls -a
$ docker container rm webserver
$ docker image ls
$ docker image rm nginx
```

# 运行已经创建好的容器

```shell
docker exec -it pwc-mysql /bin/bash
```

