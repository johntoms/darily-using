# Python发送邮件

简单邮件传输协议(SMTP)
是一种协议，用于在邮件服务器之间发送电子邮件和路由电子邮件。
Python提供smtplib模块，该模块定义了一个SMTP客户端会话对象，可用于使用SMTP或ESMTP侦听器守护程序向任何互联网机器发送邮件。
这是一个简单的语法，用来创建一个SMTP对象，稍后将演示如何用它来发送电子邮件 -
import smtplib

smtpObj = smtplib.SMTP([host[, port[, local_hostname]]] )

这里是上面语法的参数细节 -
host - 这是运行SMTP服务器的主机。可以指定主机的IP地址或类似yiibai.com的域名。这是一个可选参数。
port - 如果提供主机参数，则需要指定SMTP服务器正在侦听的端口。通常这个端口默认值是：25。
local_hostname - 如果SMTP服务器在本地计算机上运行，那么可以只指定localhost选项。
SMTP对象有一个sendmail的实例方法，该方法通常用于执行邮件发送的工作。它需要三个参数 -
sender - 具有发件人地址的字符串。
receivers - 字符串列表，每个收件人一个。
message - 作为格式如在各种RFC中指定的字符串。

1. 使用Python发送纯文本电子邮件
   示例
   以下是使用Python脚本发送一封电子邮件的简单方法

```python
# !/usr/bin/python3

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """
From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print
    "Successfully sent email"
except SMTPException:
    print
    "Error: unable to send email"
```

在这里，已经发送了一封基本的电子邮件，使用三重引号，请注意正确格式化标题。一封电子邮件需要一个From，To和一个Subject标题，与电子邮件的正文与空白行分开。
要发送邮件，使用smtpObj连接到本地机器上的SMTP服务器。 然后使用sendmail方法以及消息，从地址和目标地址作为参数(即使来自和地址在电子邮件本身内，这些并不总是用于路由邮件)。
如果没有在本地计算机上运行SMTP服务器，则可以使用smtplib客户端与远程SMTP服务器进行通信。除非您使用网络邮件服务(
    如gmail或Yahoo! Mail)，否则您的电子邮件提供商必须向您提供可以提供的邮件服务器详细信息。以腾讯QQ邮箱为例，具体如下：
mail = smtplib.SMTP('smtp.qq.com', 587)  # 端口465或587

2. 使用Python发送HTML电子邮件
   当使用Python发送邮件信息时，所有内容都被视为简单文本。 即使在短信中包含HTML标签，它也将显示为简单的文本，HTML标签将不会根据HTML语法进行格式化。 但是，Python提供了将HTML消息作为HTML消息发送的选项。
   发送电子邮件时，可以指定一个Mime版本，内容类型和发送HTML电子邮件的字符集。
   以下是将HTML内容作为电子邮件发送的示例 -

```python
# !/usr/bin/python3

import smtplib

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>

<h1>This is headline.</h1>

"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print
    "Successfully sent email"
except SMTPException:
    print
    "Error: unable to send email"
```



3. 发送附件作为电子邮件
   要发送具有混合内容的电子邮件，需要将Content - type标题设置为multipart / mixed。 然后，可以在边界内指定文本和附件部分。
   一个边界以两个连字符开始，后跟一个唯一的编号，不能出现在电子邮件的消息部分。 表示电子邮件最终部分的最后一个边界也必须以两个连字符结尾。
   所附的文件应该用包(“m”)功能编码，以便在传输之前具有基本的64编码。

4. 发送示例
   首先我们要知道用python代理登录qq邮箱发邮件，是需要更改自己qq邮箱设置的。在这里大家需要做两件事情：邮箱开启SMTP功能 、获得授权码。之后我们来看看如何更改模板代码，实现使用Python登录QQ邮箱发送QQ邮件。
   注意：也可以使用其他服务商的
   SMTP
   访问(QQ、网易、Gmail等)。
   使用QQ邮件发送邮件之前如何设置授权码，参考：
   http: // service.mail.qq.com / cgi - bin / help?subtype = 1 & & id = 28 & & no = 1001256
   4.1发送一纯文本邮件到指定邮件

   ```python
   # ! /usr/bin/env python
   
   # coding=utf-8
   
   from email.mime.text import MIMEText
   from email.header import Header
   from smtplib import SMTP_SSL
   
   # qq邮箱smtp服务器
   
   host_server = 'smtp.qq.com'
   
   # sender_qq为发件人的qq号码
   
   sender_qq = '7697****@qq.com'
   
   # pwd为qq邮箱的授权码
   
   pwd = '****kenbb***'  ## xh**********bdc
   
   # 发件人的邮箱
   
   sender_qq_mail = '7697****@qq.com'
   
   # 收件人邮箱
   
   receiver = 'yiibai.com@gmail.com'
   
   # 邮件的正文内容
   
   mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
   
   # 邮件标题
   
   mail_title = 'Maxsu的邮件'
   
   # ssl登录
   
   smtp = SMTP_SSL(host_server)
   
   # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
   
   smtp.set_debuglevel(1)
   smtp.ehlo(host_server)
   smtp.login(sender_qq, pwd)
   
   msg = MIMEText(mail_content, "plain", 'utf-8')
   msg["Subject"] = Header(mail_title, 'utf-8')
   msg["From"] = sender_qq_mail
   msg["To"] = receiver
   smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
   smtp.quit()
   
   
   ```

   执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：yiibai.com @ gmail.com，登录
   http: // gmail.com

   注意：有时可能被认为是垃圾邮件，如果没有找到可从“垃圾邮件”查找一下。
   4.2 给多个人发送邮件

   ```python
   # ! /usr/bin/env python
   
   # coding=utf-8
   
   from email.mime.text import MIMEText
   from email.header import Header
   from smtplib import SMTP_SSL
   
   # qq邮箱smtp服务器
   
   host_server = 'smtp.qq.com'
   
   # sender_qq为发件人的qq号码
   
   sender_qq = '7697****@qq.com'
   
   # pwd为qq邮箱的授权码
   
   pwd = 'h**********bdc'  ## h**********bdc
   
   # 发件人的邮箱
   
   sender_qq_mail = '7697****@qq.com'
   
   # 收件人邮箱
   
   receivers = ['yiibai.com@gmail.com', '****su@gmail.com']
   
   # 邮件的正文内容
   
   mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
   
   # 邮件标题
   
   mail_title = 'Maxsu的邮件'
   
   # ssl登录
   
   smtp = SMTP_SSL(host_server)
   
   # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
   
   smtp.set_debuglevel(1)
   smtp.ehlo(host_server)
   smtp.login(sender_qq, pwd)
   
   msg = MIMEText(mail_content, "plain", 'utf-8')
   msg["Subject"] = Header(mail_title, 'utf-8')
   msg["From"] = sender_qq_mail
   msg["To"] = Header("接收者测试", 'utf-8')  ## 接收者的别名
   smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
   smtp.quit()
   ```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：yiibai.com @ gmail.com，登录
http: // gmail.com

4.3.使用Python发送HTML格式的邮件
Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html。代码如下：

```python
# ! /usr/bin/env python

# coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

# qq邮箱smtp服务器

host_server = 'smtp.qq.com'

# sender_qq为发件人的qq号码

sender_qq = '7697****@qq.com'

# pwd为qq邮箱的授权码

pwd = '***bmke********'  ##

# 发件人的邮箱

sender_qq_mail = '7697****@qq.com'

# 收件人邮箱

receiver = 'yiibai.com@gmail.com'

# 邮件的正文内容

mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"

# 邮件标题

mail_title = 'Maxsu的邮件'

# ssl登录

smtp = SMTP_SSL(host_server)

# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式

smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

msg = MIMEText(mail_content, "html", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8')  ## 接收者的别名

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
```

执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：yiibai.com @ gmail.com，登录
http: // gmail.com

4.4.Python发送带附件的邮件
要发送带附件的邮件，首先要创建MIMEMultipart()
实例，然后构造附件，如果有多个附件，可依次构造，最后使用smtplib.smtp发送。
实现代码如下所示 -
```python
# ! /usr/bin/env python

# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# qq邮箱smtp服务器

host_server = 'smtp.qq.com'

# sender_qq为发件人的qq号码

sender_qq = '7697****@qq.com'

# pwd为qq邮箱的授权码

pwd = '*****mkenb****'  ##

# 发件人的邮箱

sender_qq_mail = '7697****@qq.com'

# 收件人邮箱

receiver = 'yiibai.com@gmail.com'

# 邮件的正文内容

mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"

# 邮件标题

mail_title = 'Maxsu的邮件'

# 邮件正文内容

msg = MIMEMultipart()

# msg = MIMEText(mail_content, "plain", 'utf-8')

msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8')  ## 接收者的别名

# 邮件正文内容

msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件

att1 = MIMEText(open('attach.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'

# 这里的filename可以任意写，写什么名字，邮件中显示什么名字

att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
msg.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件

att2 = MIMEText(open('yiibai.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="yiibai.txt"'
msg.attach(att2)

# ssl登录

smtp = SMTP_SSL(host_server)

# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式

smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
```



执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：yiibai.com @ gmail.com，登录
http: // gmail.com

4.5.在HTML文本中添加图片
邮件的HTML文本中一般邮件服务商添加外链是无效的，所以要发送带图片的邮件内容，可以参考下面的实例代码实现：

```python
# ! /usr/bin/env python

# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# qq邮箱smtp服务器

host_server = 'smtp.qq.com'

# sender_qq为发件人的qq号码

sender_qq = '7697****3@qq.com'

# pwd为qq邮箱的授权码

pwd = 'h******mk*****'  #

# 发件人的邮箱

sender_qq_mail = '7697****3@qq.com'

# 收件人邮箱

receiver = ['yiibai.com@gmail.com', 'h****u@qq.com']

# 邮件的正文内容

mail_content = ""

# 邮件标题

mail_title = 'Maxsu的邮件'

# 邮件正文内容

# msg = MIMEMultipart()

msg = MIMEMultipart('related')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8')  ## 接收者的别名

msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)

# 邮件正文内容

mail_body = """

 <p>你好，Python 邮件发送测试...</p>
 <p>这是使用python登录qq邮箱发送HTML格式和图片的测试邮件：</p>
 <p><a href='http://www.yiibai.com'>易百教程</a></p>
 <p>图片演示：</p>
 <p>![](cid:send_image)</p>

"""

# msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

msgText = (MIMEText(mail_body, 'html', 'utf-8'))
msgAlternative.attach(msgText)

# 指定图片为当前目录

fp = open('my.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用

msgImage.add_header('Content-ID', '<send_image>')
msg.attach(msgImage)

# ssl登录

smtp = SMTP_SSL(host_server)

# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式

smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()


```



执行上面代码后，登录接收邮件的邮件帐号，这里接收邮件的账号为：yiibai.com @ gmail.com，登录
http: // gmail.com



## 参考

[原文链接](http://www.yiibai.com/python/python_sending_email.html)
[Python教程](http://www.yiibai.com/python/)

