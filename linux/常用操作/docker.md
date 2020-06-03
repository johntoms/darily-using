# docker

## 常用功能命令
1. 一键清除本地缓存的所有无用的docker镜像命令
```
 docker images -q --filter "dangling=true" | xargs -t --no-run-if-empty docker rmi
```
