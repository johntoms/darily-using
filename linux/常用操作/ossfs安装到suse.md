# ossfs安装到suse

## 简介

ossfs 能让您在Linux系统中把OSS bucket 挂载到本地文件系统中，您能够便捷地通过本地文件系统操作OSS 上的对象，实现数据的共享。

## 主要功能

ossfs 基于s3fs 构建，具有s3fs 的全部功能。主要功能包括：

- 支持POSIX 文件系统的大部分功能，包括文件读写，目录，链接操作，权限，uid/gid，以及扩展属性（extended attributes）。
- 通过OSS 的multipart 功能上传大文件。
- MD5 校验保证数据完整性。

## 局限性

ossfs提供的功能和性能和本地文件系统相比，具有一些局限性。具体包括：

- 随机或者追加写文件会导致整个文件的重写。

- 元数据操作，例如list directory，性能较差，因为需要远程访问OSS服务器。

- 文件/文件夹的rename操作不是原子的。

- 多个客户端挂载同一个OSS bucket时，依赖用户自行协调各个客户端的行为。例如避免多个客户端写同一个文件等等。

- 不支持hard link。

- 不适合用在高并发读/写的场景，这样会让系统的load升高。

## 参考文档

ssfs使用文档：<https://help.aliyun.com/document_detail/32196.html>
oss源代码： <https://github.com/aliyun/ossfs>

## oss源代码安装如下：
```shell
# 创建一个目录
mkdir ossfs 创建一个目录
cd ossfs/ 进到目录下
```

## 添加源
```shell
zypper ar -fc <https://mirrors.aliyun.com/opensuse/distribution/leap/42.3/repo/oss/> ali:42.3:OSS  （zypper ar（ 添 加 一 个 新 的 安 装 源））
zypper ar -fc <https://mirrors.aliyun.com/opensuse/distribution/leap/42.3/repo/non-oss/> ali:42.3:NON-OSS
zypper ar -fc <https://mirrors.aliyun.com/opensuse/update/leap/42.3/oss/> ali:42.3:UPDATE-OSS
zypper ar -fc <https://mirrors.aliyun.com/opensuse/update/leap/42.3/non-oss> ali:42.3:UPDATE-NON-OSS
cd /etc/zypp/repos.d/
mv SLES12-SP0.repo SLES12-SP0.repo.bak
mv SLES12-SP0-Updates.repo SLES12-SP0-Updates.repo.bak
zypper refresh（刷新软件源）
zypper install git 安装git 
cd ossfs/
git clone <https://github.com/aliyun/ossfs.git> （git clone将存储库克隆到当前目录）
cd ossfs/
zypper install libcurl-devel fuse-devel openssl-devel 

zypper install gcc-c++
./autogen.sh
./configure
zypper install libxml2-devel
./configure 

make -j4 编译

make install 安装
```

## 挂载

```shell
echo my-bucket:faint:123 > /etc/passwd-ossfs （账号下bucket 和云账号的AK）
chmod 640 /etc/passwd-ossfs
mkdir /tmp/ossfs (要挂在的目录)
ossfs my-bucket /tmp/ossfs -ourl=[http://oss-cn-hangzhou.aliyuncs.com](http://oss-cn-hangzhou.aliyuncs.com/) （Bucket下的EndPoint）
```



