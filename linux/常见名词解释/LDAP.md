# LDAP

> LDAP是轻量目录访问协议，英文全称是Lightweight Directory Access Protocol，一般都简称为LDAP。它是基于X.500标准的，但是简单多了并且可以根据需要定制。与X.500不同，LDAP支持TCP/IP，这对访问Internet是必须的。LDAP的核心规范在RFC中都有定义，所有与LDAP相关的RFC都可以在LDAPman RFC网页中找到。

## 目录结构

LDAP目录以树状的层次结构来存储数据。如果你对自顶向下的DNS树或UNIX文件的目录树比较熟悉，也就很容易掌握LDAP目录树这个概念了。就象DNS的[主机名](https://baike.baidu.com/item/%E4%B8%BB%E6%9C%BA%E5%90%8D)那样，LDAP目录记录的标识名（Distinguished Name，简称DN）是用来读取单个记录，以及回溯到树的顶部。后面会做详细地介绍。

为什么要用层次结构来组织数据呢？原因是多方面的。下面是可能遇到的一些情况：

l 如果你想把所有的美国客户的联系信息都“推”到位于到[西雅图](https://baike.baidu.com/item/%E8%A5%BF%E9%9B%85%E5%9B%BE)办公室（负责营销）的LDAP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)上，但是你不想把公司的资产管理信息“推”到那里。

l 你可能想根据目录树的结构给予不同的员工组不同的权限。在下面的例子里，资产管理组对“asset-mgmt"部分有完全的访问权限，但是不能访问其它地方。

l 把LDAP存储和复制功能结合起来，可以定制目录树的结构以降低对WAN带宽的要求。位于西雅图的营销办公室需要每分钟更新的美国销售状况的信息，但是欧洲的销售情况就只要每小时更新一次就行了。

刨根问底：基准DN

LDAP目录树的最顶部就是根，也就是所谓的“基准DN"。基准DN通常使用下面列出的三种格式之一。假定我在名为FooBar的电子商务公司工作，这家公司在Internet上的名字是foobar

o="FooBar, Inc.", c=US

（以X.500格式表示的基准DN）

在这个例子中，o=FooBar, Inc. 表示组织名，在这里就是公司名的同义词。c=US 表示公司的总部在美国。以前，一般都用这种方式来表示基准DN。但是事物总是在不断变化的，现在所有的公司都已经（或计划）上Internet上。随着Internet的全球化，在基准DN中使用国家代码很容易让人产生混淆。现在，X.500格式发展成下面列出的两种格式。

o=foobar.com

（用公司的Internet地址表示的基准DN）

这种格式很直观，用公司的[域名](https://baike.baidu.com/item/%E5%9F%9F%E5%90%8D)作为基准DN。这也是现在最常用的格式。

dc=foobar, dc=com

（用DNS域名的不同部分组成的基准DN）

就象上面那一种格式，这种格式也是以DNS域名为基础的，但是上面那种格式不改变域名（也就更易读），而这种格式把域名：foobar点com分成两部分 dc=foobar, dc=com。在理论上，这种格式可能会更灵活一点，但是对于最终用户来说也更难记忆一点。考虑一下foobar.com这个例子。当foobar.com和gizmo.com合并之后，可以简单的把“dc=com"当作基准DN。把新的记录放到已经存在的dc=gizmo, dc=com目录下，这样就简化了很多工作（当然，如果foobar.com和wocket.edu合并，这个方法就不能用了）。如果LDAP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)是新安装的，我建议你使用这种格式。再请注意一下，如果你打算使用[活动目录](https://baike.baidu.com/item/%E6%B4%BB%E5%8A%A8%E7%9B%AE%E5%BD%95)（Active Directory），Microsoft已经限制你必须使用这种格式。



### 组织数据

在UNIX文件系统中，最顶层是根目录（root）。在根目录的下面有很多的文件和目录。象上面介绍的那样，LDAP目录也是用同样的方法组织起来的。

在根目录下，要把数据从逻辑上区分开。因为历史上（X.500）的原因，大多数LDAP目录用OU从逻辑上把数据分开来。OU表示“Organization Unit"，在X.500协议中是用来表示公司内部的机构：销售部、财务部，等等。现在LDAP还保留ou=这样的命名规则，但是扩展了分类的范围，可以分类为：ou=people, ou=groups, ou=devices，等等。更低一级的OU有时用来做更细的归类。例如：LDAP目录树（不包括单独的记录）可能会是这样的：

dc=foobar, dc=com

ou=customers

ou=asia

ou=europe

ou=usa

ou=employees

ou=rooms

ou=groups

ou=assets-mgmt

ou=nisgroups

ou=recipes



### 单独记录

DN是LDAP记录项的名字

在LDAP目录中的所有记录项都有一个唯一的“Distinguished Name"，也就是DN。每一个LDAP记录项的DN是由两个部分组成的：相对DN（RDN）和记录在LDAP目录中的位置。

RDN是DN中与目录树的结构无关的部分。在LDAP目录中存储的记录项都要有一个名字，这个名字通常存在cn（Common Name）这个属性里。因为几乎所有的东西都有一个名字，在LDAP中存储的对象都用它们的cn值作为RDN的基础。如果我把最喜欢的吃燕麦粥食谱存为一个记录，我就会用cn=Oatmeal Deluxe作为记录项的RDN。

l 我的LDAP目录的基准DN是dc=foobar,dc=com

l 我把自己的食谱作为LDAP的记录项存在ou=recipes

l 我的LDAP记录项的RDN设为cn=Oatmeal Deluxe

上面这些构成了燕麦粥食谱的LDAP记录的完整DN。记住，DN的读法和DNS[主机名](https://baike.baidu.com/item/%E4%B8%BB%E6%9C%BA%E5%90%8D)类似。下面就是完整的DN：

cn=Oatmeal Deluxe,ou=recipes,dc=foobar,dc=com

举一个实际的例子来说明DN

现在为公司的员工设置一个DN。可以用基于cn或uid（User ID），作为典型的用户帐号。例如，FooBar的员工Fran Smith（[登录名](https://baike.baidu.com/item/%E7%99%BB%E5%BD%95%E5%90%8D)：fsmith）的DN可以为下面两种格式：

uid=fsmith,ou=employees,dc=foobar,dc=com

（基于登录名）

LDAP（以及X.500）用uid表示“User ID"，不要把它和UNIX的uid号混淆了。大多数公司都会给每一个员工唯一的登录名，因此用这个办法可以很好地保存员工的信息。你不用担心以后还会有一个叫Fran Smith的加入公司，如果Fran改变了她的名字（结婚？离婚？或宗教原因？），也用不着改变LDAP记录项的DN。

cn=Fran Smith,ou=employees,dc=foobar,dc=com

（基于姓名）

可以看到这种格式使用了Common Name（CN）。可以把Common Name当成一个人的全名。这种格式有一个很明显的缺点就是：如果名字改变了，LDAP的记录就要从一个DN转移到另一个DN。但是，我们应该尽可能地避免改变一个记录项的DN。



### 定制对象

你可以用LDAP存储各种类型的[数据对象](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%AF%B9%E8%B1%A1)，只要这些对象可以用属性来表示，下面这些是可以在LDAP中存储的一些信息：

l 员工信息：员工的姓名、[登录名](https://baike.baidu.com/item/%E7%99%BB%E5%BD%95%E5%90%8D)、口令、员工号、他的经理的登录名，[邮件服务器](https://baike.baidu.com/item/%E9%82%AE%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%99%A8)，等等。

l 物品跟踪信息：计算机名、IP地址、标签、型号、所在位置，等等。

l 客户联系列表：客户的公司名、主要联系人的电话、传真和电子邮件，等等。

l 会议厅信息：会议厅的名字、位置、可以坐多少人、电话号码、是否有投影机。

l 食谱信息：菜的名字、配料、烹调方法以及准备方法。

因为LDAP目录可以定制成存储任何文本或二进制数据，到底存什么要由你自己决定。LDAP目录用对象类型（object classes）的概念来定义运行哪一类的对象使用什么属性。在几乎所有的LDAP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)中，你都要根据自己的需要扩展基本的LDAP目录的功能，创建新的对象类型或者扩展现存的对象类型。

LDAP目录以一系列“属性对”的形式来存储记录项，每一个记录项包括属性类型和属性值（这与关系型数据库用行和列来存取数据有根本的不同）。下面是我存在LDAP目录中的一部分食谱记录：

dn: cn=Oatmeal Deluxe, ou=recipes, dc=foobar, dc=com

cn: Instant Oatmeal Deluxe

recipeCuisine: breakfast

recipeIngredient: 1 packet instant oatmeal

recipeIngredient: 1 cup water

recipeIngredient: 1 pinch salt

recipeIngredient: 1 tsp brown sugar

recipeIngredient: 1/4 apple, any type

请注意上面每一种配料都作为属性recipeIngredient值。LDAP目录被设计成象上面那样为一个属性保存多个值的，而不是在每一个属性的后面用逗号把一系列值分开。

因为用这样的方式存储数据，所以数据库就有很大的灵活性，不必为加入一些新的数据就重新创建表和索引。更重要的是，LDAP目录不必花费内存或硬盘空间处理“空”域，也就是说，实际上不使用可选择的域也不会花费你任何资源。



### 示例

作为例子的一个单独的[数据项](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E9%A1%B9)

让我们看看下面这个例子。我们用Foobar, Inc.的员工Fran Smith的LDAP记录。这个记录项的格式是LDIF，用来导入和导出LDAP目录的记录项。

dn: uid=fsmith, ou=employees, dc=foobar, dc=com

objectclass: person

objectclass: organizationalPerson

objectclass: inetOrgPerson

objectclass: foobarPerson

uid: fsmith

givenname: Fran

sn: Smith

cn: Fran Smith

cn: Frances Smith

telephonenumber: 510-555-1234

roomnumber: 122G

o: Foobar, Inc.

mailRoutingAddress: fsmith@foobar.com

mailhost: mail.foobar.com

userpassword: {crypt}3x1231v76T89N

uidnumber: 1234

gidnumber: 1200

homedirectory: /home/fsmith

loginshell: /usr/local/bin/bash

属性的值在保存的时候是保留大小写的，但是在默认情况下搜索的时候是不区分大小写的。某些特殊的属性（例如，password）在搜索的时候需要区分大小写。

让我们一点一点地分析上面的记录项。

dn: uid=fsmith, ou=employees, dc=foobar, dc=com

这是Fran的LDAP记录项的完整DN，包括在目录树中的完整路径。LDAP（和X.500）使用uid（User ID），不要把它和UNIX的uid号混淆了。

objectclass: person

objectclass: inetOrgPerson

objectclass: foobarPerson

可以为任何一个对象根据需要分配多个对象类型。person对象类型要求cn（common name）和sn（surname）这两个域不能为空。person对象类型允许有其它的可选域，包括givenname、telephonenumber，等等。organizational Person给person加入更多的可选域，inetOrgPerson又加入更多的可选域（包括电子邮件信息）。最后，foobarPerson是为Foobar定制的对象类型，加入了很多定制的属性。

uid: fsmith

givenname: Fran

sn: Smith

cn: Fran Smith

cn: Frances Smith

telephonenumber: 510-555-1234

roomnumber: 122G

o: Foobar, Inc.

以前说过了，uid表示User ID。当看到uid的时候，就在脑袋里想一想“login"。

请注意CN有多个值。就象上面介绍的，LDAP允许某些属性有多个值。为什么允许有多个值呢？假定你在用公司的LDAP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)查找Fran的电话号码。你可能只知道她的名字叫Fran，但是对人力资源处的人来说她的正式名字叫做Frances。因为保存了她的两个名字，所以用任何一个名字检索都可以找到Fran的电话号码、电子邮件和办公房间号，等等。

mailRoutingAddress: fsmith@foobar.com

mailhost: mail.foobar.com

就象现在大多数的公司都上网了，Foobar用Sendmail发送邮件和处理外部邮件路由信息。Foobar把所有用户的邮件信息都存在LDAP中。最新版本的Sendmail支持这项功能。

Userpassword: {crypt}3x1231v76T89N

uidnumber: 1234

gidnumber: 1200

gecos: Frances Smith

homedirectory: /home/fsmith

loginshell: /usr/local/bin/bash

注意，Foobar的系统管理员把所有用户的口令映射信息也都存在LDAP中。FoobarPerson类型的对象具有这种能力。再注意一下，用户口令是用UNIX的口令加密格式存储的。UNIX的uid在这里为uidnumber。提醒你一下，关于如何在LDAP中保存NIS信息，有完整的一份RFC。在以后的文章中我会谈一谈NIS的集成。

LDAP复制

LDAP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)可以使用基于“推”或者“拉”的技术，用简单或基于安全证书的安全验证，复制一部分或者所有的数据。

例如，Foobar有一个“公用的”LDAP服务器，地址为ldap.foobar.com，端口为389。Netscape Communicator的电子邮件查询功能、UNIX的“ph"命令要用到这个服务器，用户也可以在任何地方查询这个服务器上的员工和客户联系信息。公司的主LDAP[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)运行在相同的计算机上，不过[端口号](https://baike.baidu.com/item/%E7%AB%AF%E5%8F%A3%E5%8F%B7)是1389。

你可能即不想让员工查询资产管理或食谱的信息，又不想让信息技术人员看到整个公司的LDAP目录。为了解决这个问题，Foobar有选择地把子目录树从主LDAP服务器复制到“公用”LDAP服务器上，不复制需要隐藏的信息。为了保持数据始终是最新的，主[目录服务器](https://baike.baidu.com/item/%E7%9B%AE%E5%BD%95%E6%9C%8D%E5%8A%A1%E5%99%A8)被设置成即时“推”同步。这些种方法主要是为了方便，而不是安全，因为如果有权限的用户想查询所有的数据，可以用另一个LDAP端口。

假定Foobar通过从[奥克兰](https://baike.baidu.com/item/%E5%A5%A5%E5%85%8B%E5%85%B0)到欧洲的低带宽数据的连接用LDAP管理客户联系信息。可以建立从ldap.foobar.com:1389到munich-ldap.foobar.com:389的数据复制，象下面这样：

periodic pull: ou=asia,ou=customers,o=sendmail.com

periodic pull: ou=us,ou=customers,o=sendmail.com

immediate push: ou=europe,ou=customers,o=sendmail.com

“拉”连接每15分钟同步一次，在上面假定的情况下足够了。“推”连接保证任何欧洲的联系信息发生了变化就立即被“推”到Munich。

用上面的复制模式，用户为了访问数据需要连接到哪一台[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8)呢？在Munich的用户可以简单地连接到本地服务器。如果他们改变了数据，本地的LDAP服务器就会把这些变化传到主LDAP服务器。然后，主LDAP服务器把这些变化“推”回本地的“公用”LDAP服务器保持数据的同步。这对本地的用户有很大的好处，因为所有的查询（大多数是读）都在本地的服务器上进行，速度非常快。当需要改变信息的时候，最终用户不需要重新配置客户端的软件，因为LDAP[目录服务器](https://baike.baidu.com/item/%E7%9B%AE%E5%BD%95%E6%9C%8D%E5%8A%A1%E5%99%A8)为他们完成了所有的数据交换工作。