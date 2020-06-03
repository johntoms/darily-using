# LDAP 部署

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

## docker 安装 LDAP
> [github 参考文档](https://github.com/osixia/docker-openldap#set-your-own-environment-variables)

> [docker hub 文档](https://www.cnblogs.com/eoalfj/p/11837415.html)

```
# 安装 ldap

# 创建 ldap-net worker
docker network create openldap-net
# 创建ldap映射目录
mkdir -p /home/ldap/data
mkdir -p /home/ldap/config

# 启用 ldap server
docker run -p 389:389 -p 636:636 --network openldap-net --env LDAP_ORGANISATION="caoxiangpeng" --env LDAP_DOMAIN="zydevops.com" \
--env LDAP_ADMIN_PASSWORD="YR1iNFJ1kJ2e87Qq" --volume /home/ldap/data:/var/lib/ldap --volume /home/ldap/config:/etc/ldap/slapd.d --name openldap --detach osixia/openldap:1.3.0

# 安装 ldapaccountmanager 
# 创建 ldapaccountmanager 映射目录
mkdir -p /home/ldapaccountmanager/config

# 启用 ldapaccountmanager server
# 有配置文件
docker run \
-p 9000:80 -it -d \
--network openldap-net \
--volume /home/ldapaccountmanager/config/config.cfg:/etc/ldap-account-manager/config.cfg \
--volume /home/ldapaccountmanager/config/lam.conf:/var/lib/ldap-account-manager/lam.conf \
--env LAM_SKIP_PRECONFIGURE=true \
--name ldapaccountmanager \
ldapaccountmanager/lam:stable

# 无配置文件
docker run -p 9000:80 --network openldap-net -it -d ldapaccountmanager/lam:stable


#  修改ldap密码
docker run --name ssp --network openldap-net -d -p 80:80 openfrontier/ldap-ssp

docker create \
  --name=ldap-auth \
  --network openldap-net \
  -e TZ=Asia/Shanghai \
  -p 9001:8888 \
  -p 9002:9000 \
  --restart unless-stopped \
  linuxserver/ldap-auth
```
