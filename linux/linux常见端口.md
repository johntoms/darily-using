# linux常见端口及描述

| 端口号        | 简述                                   | 说明                                                         |
| ------------- | -------------------------------------- | ------------------------------------------------------------ |
| 21            | FTP                                    | FTP 服务所开放端口，用于上传和下载文件。                     |
| 22            | SSH                                    | SSH端口，用于通过命令行模式远程连接LINUX实例。               |
| 23            | telnet                                 | telnet 端口，用于telnet远程登陆ECS实例。                     |
| 25            | SMTP                                   | SMTP服务所开放的端口，用于发送邮件。阿里云默认25端口受限，提交工单解封25端口。 |
| 80            | HTTP                                   | 用于HTTP服务提供访问功能。IIS、Apache、Nginx等服务。         |
| 110           | POP                                    | POP3协议，POP3电子邮件收发协议。                             |
| 143           | IMAP                                   | IMAP（Internet Message Access Protocol）协议，IMAP是用于发送电子邮件的接收协议。 |
| 443           | HTTPS                                  | 用于提供https访问功能。HTTPS是一种提供加密和通过安全端口传输的一种协议。 |
| 1433          | SQL server                             | SQL Server 的 TCP 端口，用于供 SQL Server 对外提供服务。     |
| 1434          | SQL server                             | SQL Server 的 UDP 端口，用于返回 SQL Server 使用了哪个 TCP/IP 端口。 |
| 1521          | Oracle                                 | Oracle 通信端口，ECS 实例上部署了 Oracle SQL 需要放行的端口。 |
| 3306          | MySQL                                  | MySQL 数据库对外提供服务的端口。                             |
| 3389          | Windows Server Remote Desktop Services | Windows Server Remote Desktop Services（远程桌面服务）端口，可以通过这个端口 远程连接 ECS 实例。 |
| 6379          | redis                                  | redis向外提供服务的默认端口                                  |
| 8080          | 代理端口                               | 同 80 端口一样，8080 端口常用于 WWW 代理服务，实现网页浏览。如果您使用了 8080 端口，访问网站或使用代理服务器时，需要在 IP 地址后面加上 :8080。安装 Apache Tomcat 服务后，默认服务端口为 8080。Jboss |
| 11211         | memcached                              | memcached默认状态下的端口号                                  |
| 27017         | mongodb                                | mongodb 默认端口号                                           |
| 137，138，139 | NetBIOS                                | 137、138 为 UDP 端口，通过网上邻居传输文件时使用的端口。139 通过这个端口进入的连接试图获得 NetBIOS/SMB 服务。NetBIOS 协议常被用于 Windows 文件、打印机共享和 Samba。 |

无法访问某些端口
现象：ECS 实例监听了对应端口，但这个端口在部分地区无法访问，而其它端口访问正常的情况。

分析：部分运营商判断端口 135、139、444、445、5800、5900 等为高危端口，默认被屏蔽。

解决：建议您修改敏感端口为其它非高危端口承载业务。