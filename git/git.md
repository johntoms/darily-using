# git

[TOC]

## git 简介

> git 是什么？

git 是目前世界上最先进的分布式版本控制系统之一。





> git 的特点

- 采用分布式版本控制系统，解除了对网络的依赖性。
- “多中心” 版本控制系统，本地自带控制系统，远程仓库，本地缓存系统。
- CVS作为最早的开源而且免费的集中式版本控制系统，由于CVS自身设计的问题，会造成提交文件不完整，版本库莫名其妙损坏的情况。同样是开源而且免费的SVN修正了CVS的一些稳定性问题，是目前用得最多的集中式版本库控制系统。





> git 原理图

![git原理图](http://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/git_study-%E5%8E%9F%E7%90%86%E5%9B%BE.jpg)

```markdown
# git 专有名词解释
- workspace : 工作区
- index / stage :暂缓存区
- repository : 仓库区（本地仓库）
- remote : 远程仓库
```



## git 安装

参考文档：[git 菜鸟教程安装]( http://www.runoob.com/git/git-install-setup.html)





## git 常用命令

### 新建代码库

```shell
# 在当前目录新建一个 git 代码库
$ git init

# 新建一个目录，将其初始化为 git 代码库
$ git init [project_name]

# 下载一个项目和他的整个代码历史
$ git clone [url]
```

### 配置

>  Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。

```shell
# 显示当前的Git配置
$ git config --list

# 编辑Git配置文件
$ git config -e [--global]

# 设置提交代码时的用户信息
$ git config [--global] user.name "[name]"
$ git config [--global] user.email "[email address]"
```

### 增加/删除文件

```shell
# 添加指定文件到暂存区
$ git add [file1]  [file2]

# 添加指定目录到暂存区（包括子目录）
$ git add [dir]

# 添加当前目录的所有文件到暂存区
$ git add .

# 对于同一个文件的多处变化，可多次提交
$ git add -p

# 删除工作区文件，并且将这次删除放入暂存区
git rm [file1] [file2]

# 停止追踪指定文件，但该文件保存在暂存区
git rm --cached [file]

# 改名文件，并将这个改名放入暂存区
git mv [file_original] [file_renamed]
```

### 代码提交

```shell
# 提交暂存区到仓库区
$ git commit -m 'message'

# 提交暂存区的指定文件到仓库区
$ git commit [file1] [file2] -m "message"

# 提交工作区自上次 commit 之后的变化，直接到仓库区
$ git commit -a

# 提交时显示所有 diff 信息
$ git commit -v

# 使用一次新的commit，替代上一次提交
# 如果代码没有任何新变化，则用来改写上一次commit的提交信息
$ git commit amend -m "message"

# 重做上一次commit，并包括指定文件的新变化
$ git commit --amend [file1] [file2] ...
```

### 分支

```bash
# 列出所有本地分支
$ git branch

# 列出所有远程分支
$ git branch -r

# 列出所有本地分支和远程分支
$ git branch -a

# 新建一个分支，但依然停留在当前分支
$ git branch [branch-name]

# 切换到指定分支，并更新工作区
$ git checkout [branch-name]

# 切换到上一个分支
$ git checkout -

# 建立追踪关系，在现有分支与指定的远程分支之间
$ git branch --set-upstream [branch] [remote-branch]

# 合并指定分支到当前分支
$ git merge [branch]

# 选择一个commit，合并进当前分支
$ git cherry-pick [commit]

# 删除分支
$ git branch -d [branch-name]

# 删除远程分支
$ git push origin --delete [branch-name]
$ git branch -dr [remote/branch]
```

### 标签

```shell
# 列出所有tag
$ git tag

# 新建一个tag在当前commit
$ git tag [tag]

# 新建一个tag在指定commit
$ git tag [tag] [commit]

# 删除本地tag
$ git tag -d [tag]

# 删除远程tag
$ git push origin :refs/tags/[tagName]

# 查看tag信息
$ git show [tag]

# 提交指定tag
$ git push [remote] [tag]

# 提交所有tag
$ git push [remote] --tags

# 新建一个分支，指向某个tag
$ git checkout -b [branch] [tag]
```

### 查看状态

```bash
# 显示有变更的文件
$ git status

# 显示当前分支的版本历史
$ git log

# 显示commit历史，以及每次commit发生变更的文件
$ git log --stat

# 搜索提交历史，根据关键词
$ git log -S [keyword]

# 显示某个commit之后的所有变动，每个commit占据一行
$ git log [tag] HEAD --pretty=format:%s

# 显示某个commit之后的所有变动，其"提交说明"必须符合搜索条件
$ git log [tag] HEAD --grep feature

# 显示某个文件的版本历史，包括文件改名
$ git log --follow [file]
$ git whatchanged [file]

# 显示指定文件相关的每一次diff
$ git log -p [file]

# 显示过去5次提交
$ git log -5 --pretty --oneline

# 显示所有提交过的用户，按提交次数排序
$ git shortlog -sn

# 显示指定文件是什么人在什么时间修改过
$ git blame [file]

# 显示暂存区和工作区的代码差异
$ git diff

# 显示暂存区和上一个commit的差异
$ git diff --cached [file]

# 显示工作区与当前分支最新commit之间的差异
$ git diff HEAD

# 显示两次提交之间的差异
$ git diff [first-branch]...[second-branch]

# 显示今天你写了多少行代码
$ git diff --shortstat "@{0 day ago}"

# 显示某次提交的元数据和内容变化
$ git show [commit]

# 显示某次提交发生变化的文件
$ git show --name-only [commit]

# 显示某次提交时，某个文件的内容
$ git show [commit]:[filename]

# 显示当前分支的最近几次提交
$ git reflog

# 从本地master拉取代码更新当前分支：branch 一般为master
$ git rebase [branch]
```

### 远程同步

```shell
$ git remote update  --更新远程仓储
# 下载远程仓库的所有变动
$ git fetch [remote]

# 显示所有远程仓库
$ git remote -v

# 显示某个远程仓库的信息
$ git remote show [remote]

# 增加一个新的远程仓库，并命名
$ git remote add [shortname] [url]

# 取回远程仓库的变化，并与本地分支合并
$ git pull [remote] [branch]

# 上传本地指定分支到远程仓库
$ git push [remote] [branch]

# 强行推送当前分支到远程仓库，即使有冲突
$ git push [remote] --force

# 推送所有分支到远程仓库
$ git push [remote] --all
```

### 撤销

```shell
# 恢复暂存区的指定文件到工作区
$ git checkout [file]

# 恢复某个commit的指定文件到暂存区和工作区
$ git checkout [commit] [file]

# 恢复暂存区的所有文件到工作区
$ git checkout .

# 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
$ git reset [file]

# 重置暂存区与工作区，与上一次commit保持一致
$ git reset --hard

# 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
$ git reset [commit]

# 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
$ git reset --hard [commit]

# 重置当前HEAD为指定commit，但保持暂存区和工作区不变
$ git reset --keep [commit]

# 新建一个commit，用来撤销指定commit
# 后者的所有变化都将被前者抵消，并且应用到当前分支
$ git revert [commit]

# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop
```

## git 常见场景

### git 删除远程已经推送过的文件或者文件夹

1. 把github上的文件删除，但是本地仓库里的文件

   ```bash
   
   git rm --cached filename/-r directory
   git commit "xxxx"
   git push
   ```

2. 删除远程code 文件夹,本地保留

   ```bash
   ## 注意删除文件夹时要带上 -r 参数
   git rm --cached -r code
   git commit -m "delete directory"
   git push
   ```

   

## 参考链接

[git博客](<http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html>)

[git 官方文档](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%85%B3%E4%BA%8E%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6)

