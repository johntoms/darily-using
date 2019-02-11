# DHCP

> **动态主机设置协议**（英语：**Dynamic Host Configuration Protocol，DHCP**）是一个[局域网](https://baike.baidu.com/item/%E5%B1%80%E5%9F%9F%E7%BD%91)的[网络协议](https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E5%8D%8F%E8%AE%AE)，使用[UDP](https://baike.baidu.com/item/UDP)协议工作，主要有两个用途：用于内部网或网络服务供应商自动分配[IP](https://baike.baidu.com/item/IP)地址；给用户用于内部网管理员作为对所有计算机作中央管理的手段。

## 功能概述

DHCP（Dynamic Host Configuration Protocol，动态主机配置协议）通常被应用在大型的局域网络环境中，主要作用是集中的管理、分配IP地址，使网络环境中的主机动态的获得IP地址、Gateway地址、DNS服务器地址等信息，并能够提升地址的使用率。

DHCP协议采用客户端/服务器模型，主机地址的动态分配任务由网络主机驱动。当DHCP服务器接收到来自网络主机申请地址的信息时，才会向网络主机发送相关的地址配置等信息，以实现网络主机地址信息的动态配置。DHCP具有以下功能：

\1. 保证任何IP地址在同一时刻只能由一台DHCP客户机所使用。

\2. DHCP应当可以给用户分配永久固定的IP地址。

\3. DHCP应当可以同用其他方法获得IP地址的[主机](https://baike.baidu.com/item/%E4%B8%BB%E6%9C%BA)共存（如手工配置IP地址的主机）。

\4. DHCP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)应当向现有的BOOTP[客户端](https://baike.baidu.com/item/%E5%AE%A2%E6%88%B7%E7%AB%AF)提供服务。

DHCP有三种机制分配IP地址：

1) 自动分配方式（Automatic Allocation），DHCP服务器为主机指定一个永久性的IP地址，一旦DHCP客户端第一次成功从DHCP服务器端租用到IP地址后，就可以永久性的使用该地址。

[![相关图片](https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=716c302eddc451daf2f60be986fc52a5/4b90f603738da97753ab2e5bb051f8198618e33e.jpg)](https://baike.baidu.com/pic/DHCP/218195/0/1e71f724d22034414d088d5f?fr=lemma&ct=single)

2) 动态分配方式（Dynamic Allocation），DHCP服务器给主机指定一个具有时间限制的IP地址，时间到期或主机明确表示放弃该地址时，该地址可以被其他主机使用。

3) 手工分配方式（Manual Allocation），客户端的IP地址是由网络管理员指定的，DHCP服务器只是将指定的IP地址告诉客户端主机。

三种地址分配方式中，只有动态分配可以重复使用客户端不再需要的地址。

DHCP消息的格式是基于BOOTP（Bootstrap Protocol）消息格式的，这就要求设备具有BOOTP中继代理的功能，并能够与BOOTP客户端和DHCP服务器实现交互。BOOTP中继代理的功能，使得没有必要在每个物理网络都部署一个DHCP服务器。RFC 951和RFC 1542对BOOTP协议进行了详细描述。

## 应用场景

**什么时候最好使用 DHCP ？**

公司内部很多 Laptop[计算机](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA)使用的场合！因为 Laptop在使用上，当设定为DHCP client 的时候，那么只要它连接上的网域里面有一部可以上网的 DHCP服务器 ，那部Laptop也就可以连接上 Internet 了！

网域内[计算机](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA)数量相当的多时：另外一个情况就是网域内计算机数量相当庞大时，大到您没有办法一个一个的进行说明来设定他们自己的网络参数，这个时候为了省麻烦，还是架设DHCP 来的方便。

**什么情况下不建议使用 DHCP 主机？**

Client 在开机的时候会主动的发送讯息给网域上的所有机器，这个时候，如果网域上就是没有DHCP[主机](https://baike.baidu.com/item/%E4%B8%BB%E6%9C%BA)呢？那么这部 Client 端[计算机](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA)会发送四次请求信息，第一次等待时间为 1 秒，其余三次的等待时间分别是 9、13、16 秒。如果还是没有DHCP服务器的响应，那么在5分钟之后，Client端计算机会重复这一动作。

在网域内的[计算机](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA)，有很多机器其实是做为[主机](https://baike.baidu.com/item/%E4%B8%BB%E6%9C%BA)的用途，很少Client 需求，那么似乎就没有必要架设 DHCP。