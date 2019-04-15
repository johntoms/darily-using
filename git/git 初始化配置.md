# 命令行指令
## Git 全局设置
```shell
git config --global user.name "username"
git config --global user.email "email"
```

## 已存在的文件夹或 Git 仓库
```shell
cd existing_folder
git init

# 创建忽略上传的文件或者文件夹
vim .gitignore
/venv/
/tmp/

# 配置本项目的 git `用户名` 和 `邮箱`
# 若全局 用户名 和 邮箱 与本项目要求的相同，则可以忽略此步骤
git config --local user.name "username"
git config --local user.email "email"


git remote add origin https://code.aliyun.com/johntoms/ldap-manager.git
git add .
git commit
git push -u origin master
```
