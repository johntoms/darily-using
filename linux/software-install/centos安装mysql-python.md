Centos 安装python-mysql

1.pip install MySQL-python
报错信息如下：
```
 Complete output from command python setup.py egg_info:
    sh: mysql_config: 未找到命令
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-build-j8q7Uq/MySQL-python/setup.py", line 17, in <module>
        metadata, options = get_config()
      File "setup_posix.py", line 43, in get_config
        libs = mysql_config("libs_r")
      File "setup_posix.py", line 25, in mysql_config
        raise EnvironmentError("%s not found" % (mysql_config.path,))
    EnvironmentError: mysql_config not found
```
2.缺少相关依赖包mysql-devel，此时需要安装mysql-devel，yum install mysql-devel

```
yum install mysql-devel
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * epel: mirrors.tongji.edu.cn
 * extras: mirrors.163.com
 * updates: mirrors.cn99.com
正在解决依赖关系
--> 正在检查事务
---> 软件包 mariadb-devel.x86_64.1.5.5.56-2.el7 将被 安装
--> 解决依赖关系完成

依赖关系解决

===========================================================
 Package         架构     版本                源      大小
===========================================================
正在安装:
 mariadb-devel   x86_64   1:5.5.56-2.el7      base   752 k

事务概要
===========================================================
安装  1 软件包

总下载量：752 k
安装大小：3.3 M
Is this ok [y/d/N]: y
Downloading packages:
mariadb-devel-5.5.56-2.el7.x86_64.rpm | 752 kB   00:01     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  正在安装    : 1:mariadb-devel-5.5.56-2.el7.x86_64    1/1 
  验证中      : 1:mariadb-devel-5.5.56-2.el7.x86_64    1/1 

已安装:
  mariadb-devel.x86_64 1:5.5.56-2.el7                      

完毕！
```

3.再次安装会报出这样一个错误，代码如下：

```
gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -Dversion_info=(1,2,5,'final',1) -D__version__=1.2.5 -I/usr/include/mysql -I/usr/include/python2.7 -c _mysql.c -o build/temp.linux-x86_64-2.7/_mysql.o
    _mysql.c:29:20: 致命错误：Python.h：没有那个文件或目录
     #include "Python.h"
                        ^
    编译中断。
    error: command 'gcc' failed with exit status 1
```
缺少依赖关系包python-devel，yum install python-devel

```
[root@localhost ~]# yum install devel
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * epel: ftp.cuhk.edu.hk
 * extras: mirrors.cn99.com
 * updates: mirrors.cn99.com
没有可用软件包 devel。
错误：无须任何处理
[root@localhost ~]# yum install python-devel
已加载插件：fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * epel: mirrors.tongji.edu.cn
 * extras: mirrors.163.com
 * updates: mirrors.cn99.com
正在解决依赖关系
--> 正在检查事务
---> 软件包 python-devel.x86_64.0.2.7.5-58.el7 将被 安装
--> 解决依赖关系完成

依赖关系解决

===========================================================
 Package         架构      版本              源       大小
===========================================================
正在安装:
 python-devel    x86_64    2.7.5-58.el7      base    395 k

事务概要
===========================================================
安装  1 软件包

总下载量：395 k
安装大小：1.1 M
Is this ok [y/d/N]: y
Downloading packages:
python-devel-2.7.5-58.el7.x86_64.rpm  | 395 kB   00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  正在安装    : python-devel-2.7.5-58.el7.x86_64       1/1 
  验证中      : python-devel-2.7.5-58.el7.x86_64       1/1 

已安装:
  python-devel.x86_64 0:2.7.5-58.el7                       

完毕！
```
OK,开始使用吧。
