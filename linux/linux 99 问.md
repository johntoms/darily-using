　20.安装Linux，对硬件有什么要求？

　　Linux对硬件要求很低，可以运行在386以上CPU，8M以上内存的IBM PC机上。但由于设备厂商的支持力度不够，所以Linux倒是对很多新设备的支持不是很好，新设备的驱动程序总是慢一步。

　　21.安装Linux需要做哪些准备？

　　1） 收集系统资料：记录下内存大小，CDROM接口类型，SCSI卡型号，网卡型号，鼠标类型，显卡芯片组、时钟芯片、显存大小等相关信息；

　　2） 检查CMOS设置，关闭病毒开发，设置其从光驱启动；

　　3） 如果你的Linux安装盘无法自启动的话还需制作启动盘；

　　4） 为Linux的安装腾出硬盘空间，最好有1G左右。

　　22.安装Linux前要有哪些基础知识呢？

　　安装Linux时，至少需要两个分区：Linux native主分区、Linux Swap交换分区。主分区用来存放Linux的文件，交换分区为运行Linux提供虚拟内存。

　　交换区每个8-256M，最多可以有8个，一般建立一个与内存等大的就行了。

　　DOS中，不管物理上、逻辑上，每个分区就是一个独立的部分，比如：C盘、D盘、E盘，每个盘都有一个根目录。而在Linux中，物理上是一个个分区，而逻辑上所有的分区都是一个整体的，Linux中只有一个根目录。

　　23.Linux如何命名我的硬盘？

　　Linux对硬盘的处理，与DOS系统基本上是一样的，先做分区，然后再做格式化。分区的命令是不同的，DOS下，每一个分区是用一个英文字母来表示，而在Linux下则更加灵活，它通过字母和数字的组合来标识硬盘分区。

　　如"hda1"，hd是一个部分，代表IDE硬盘，如果是SCSI硬盘的话，为sa；a代表IDE1口的主硬盘（2代表IDE1口从硬盘、3代表IDE2口主硬盘、4代表IDE2口从硬盘）；最后的数字代表在该设备上的分区顺序，前四个分区（主分区和扩展分区）用1-4表示，软逻辑分区从5开始。

　　24.如何安装Linux？

　　每种Linux发行版所提供的安装方法都不大一样，但是一般来说都经历以下几个阶段：

　　1） 一些基本设置：如安装语言、键盘；

　　2） 进行硬盘分区、格式化：一般发行版都提供了图形界面，如果不熟悉硬盘分区的爱好者最好在行家指导下进行；

　　3） 选择要安装的软件包：建议初学者全部安装，待以后熟悉了后再重新定制，以免在学习过程中丢这落那的；

　　4） 设备配置：如打印机、网卡、显卡等，请根据实际情况选择；

　　5） 安装LILO：建议装在主引导扇，使用LILO来完成多系统引导；

　　6） 为Linux的超级用户root设置密码。

　　大家可以参考每种Linux的相关资料来尝试安装。

　　25.如何在一块硬盘上安装多个作系统？

　　许多Linux爱好者都希望能够在保留Windows9x作系统的同时，安装Linux。为了能够在多个作系统的自动选择，就需要一个启动管理器，Linux带了一个很好的启动管理器---lilo。

　　所以在安装多个作系统时，你只需先安装其它作系统，最后安装Linux，并将lilo安装在主引导扇上，这样重新启动系统时，将出现lilo：等待你选择你要启动的作系统。

​    26.如何配置linux启动管理器lilo？

 　　根据需要修改/etc/lilo.conf文件，然后执行/sbin/lilo让设置生效。下面是一个lilo.conf文件的示例：

　　boot=/dev/hda

　　map=/boot/map

　　install=/boot/boot.b

　　prompt

　　timeout=50

　　default=linux

　　image=/boot/vmlinuz-2.2.5-15

　　label=linux

　　root=/dev/hda1

　　initrd=/boot/initrd-2.2.5-15.img

　　read-only

　　other=/dev/hda2

　　label=windows

　　其中，timeout是用来设置lilo等待输入的时间，在此表示如果5秒不选择的话就进入default；

　　default选项用来指定默认启动哪个系统；

　　image小节用来指定linux的启动信息，包括启动位置，名字--linux；

　　other小节用来指定其他作系统的启动信息，包括启动位置、名字。

　　27.如何启动、关闭系统？

　　启动Linux很简单，只要在lilo中选择linux（输入linux）就可以了，在启动过程中，将会向控制台写许多信息，直到出现用户登录提示login:，输入用户名和密码就可以登录系统，开始Linux世界的探索。

　　关机时一定要注意，不能直接关闭计算机电源，那样会破坏Linux的文件系统，你可以使用以下命令来实现：

　　1） 重启：执行reboot命令或同时按下Ctrl+Alt+Del键；

　　2） 关闭系统：执行shutdown -h now命令。

　　28.Linux下的目录作与DOS/Windows有什么不同？

　　Linux的文件系统与DOS类似，也是采用树形结构的。但目录的表示有一点是完全不同的，Linux用"/"表示根目录，而DOS用""表示根目录。以下是在Linux下常用的目录作命令：

　　1）"mkdir 目录名"：建立目录；

　　2）"rmdir 目录名"：删除空目录；

　　3）"cd 目录名"：改变目录；

　　注:cd与目录名之间一定要空格，比如到根目录，需用"cd /"，而非"cd/"

　　4）"pwd"：查看自己所在的目录；

　　29.在Linux如何对文件进行作？

　　你可以使用ls -l命令列出目录的详细信息，就相当于DOS的DIR命令。ls命令的输出如下所示：

　　total 2

　　drwxr-xr-x 2 xu user 1024 Mar 13 0:34 sub1

　　-rw-r----- l xu user 678 Jun 15 1:45 hodo.txt

　　最左边一列是文件/目录权限，第3列是的属主信息，第4列是属主所在用户组，第5列是所占空间大小，接下去是日期、时间，最后一列是文件/目录名。以下是一些 常用文件作命令：

　　rm：删除文件 more：浏览文件 cp：拷贝文件

　　30.如何编辑一个文本文件？

　　你可以使用vi来编辑一个文件文件，它是在 Unix 世界里最普及的文字处理工具，几乎所有的UNIX机器上都有这个编辑器。

　　1） 启动vi：执行"vi 文件名"，一启动vi在命令状态，可以输入各种vi的命令，不能编辑；

　　2） 存盘：w、存盘退出：wq、不存盘退出：q!；

　　3） 进入编辑状态：插入：i、新增：a；

　　4） 退出编辑状态：按ESC键；

　　5） 进入编辑状态后，编辑起来很像DOS下的edit；

　　6） 在命令状态下还有一些常用的命令：

　　x 删除游标所在字元；

　　dd 删除游标所在的列。

​     31.安装完Linux后，根目录下一大堆，都是些什么？

 　　/bin：存放最常用命令；

　　/boot：启动Linux的核心文件；

　　/dev：设备文件；

　　/etc：存放各种配置文件；

　　/home：用户主目录；

　　/lib：系统最基本的动态链接共享库；

　　/mnt：一般是空的，用来临时挂载别的文件系统；

　　/proc：虚拟目录，是内存的映射；

　　/sbin：系统管理员命令存放目录；

　　/usr：最大的目录，存许应用程序和文件；

　　/usr/X11R6：X-Window目录；

　　/usr/src：Linux源代码；

　　/usr/include：系统头文件；

　　/usr/lib：存放常用动态链接共享库、静态档案库；

　　/usr/bin、/usr/sbin：这是对/bin、/sbin的一个补充；

　　32.如何安装网卡？

　　你可以用root登录后运行netconf来安装网卡。输入网卡的设备名、选择网卡的模块号，IO地址、IRQ中断等信息，然后存盘退出，执行：/etc/rc.d/init.d/network restart；

　　如果你的网卡未能列在可选的网卡模块列表中的话，你就需要下载驱动程序，然后将其编译成模块。最后用"insmod 模块名"命令完成安装。

　　33.如何驱动D-Link DE220网卡？

　　D-Link的DE220是一款性价比较好的，支持即插即用的ISA网卡。但正是由于即插即用功能使得其在Linux下安装会遇到一些麻烦：

　　1） 在DOS环境下，用DE220网卡的驱动程序盘中的一个工具setup将其设置成非PNP的；

　　2） 到Windows的控制面板中获取其IO地址和中断号，一般情况下，IO地址是240，中断号是10；

　　3） 启动Linux，登录后执行"netconf"，将第一块网卡设为Enable，设备名为eth0，模块为ne，IO地址为0x240，IRQ为10；

　　4） 存盘退出后，运行/etc/rc.d/init.d/network restart即可。

　　34.如何驱动D-Link DFE530 TX网卡？

　　D-Link 530 TX网卡是一款性价比较好的10M/100M自适应的PCI网卡，拥有广大的用户群，然后Linux在安装向导中却没有列在列表中。

　　其实，一般Linux都已经包含了这款网卡的驱动模块：tulip.o，你可以直接执行"insmod tulip"来完成网卡的安装。

　　35.如何驱动D-Link DFE540 TX网卡？

　　如果你的网卡是D-Link DFE540 TX，那么在安装时不要选网卡，否则可能造成一些不必要的麻烦。

　　1） 下载最新的tulip.c文件，并复制到/usr/src/tulip下；

　　2）执行以下命令，编译生成tulip.o：

　　#cd /usr/src/tulip

　　 #gcc -DMODVERSIONS -DMODULE -D__KERNEL__ -Wall -Wstrict-prototypes -O6 -c tulip.c

　　3）执行insmod tulip.o；

　　4）执行/etc/rc.d/init.d/network restart，让网卡生效。

　　36.如何驱动Davicom 9201网卡？

　　Davicom 9201 PCI网卡在安装Linux时，不能直接完成。其实，大多数的Linux发行版都提供了这款网卡的驱动模块---dmfe.o，如果你的机器也是这种网卡的话，可以在安装Linux时略过网卡配置，安装完启动系统、登录后，执行："insmod dmfe"命令添加驱动模块，然后执行"/etc/rc.d/init.d/network restart"就可以了。

​     37.如何驱动第二块网卡？

 　　在Linux系统中，你可以很容易地使用配置工具netconf安装第二块网卡，在netconf中选择第二块网卡，设备名：eth1、选择其驱动模块、输入IO地址和IRQ中断号，存盘退出后，执行：

　　/etc/rc.d/init.d/network restart

　　38.如何驱动普通声卡？

　　在Linux系统中提供了一个十分方便使用的声卡配置工具sndconfig，如果你的声卡比较大众化，就可以使用它来驱动你的声卡：

　　1） 用root登录系统，运行/usr/sbin/sndconfig；

　　2） 从声卡选择列表中选择适合你的声卡，一般的声卡都可以使用SoundBlaster；

　　3） 选完后，sndconfig需要你设置声卡的IO地址和IRQ中断号，根据你的实际情况选择；

　　4） 设置完成按OK按钮，如果听到Linus说话的声音就大功告成了。

　　39.如何驱动YAMAHA719声卡？

　　Yamaha719声卡在Linux下的驱动是十分麻烦的：

　　1） 重新编译核心，不选择SB或SB PRO之类的声卡，选中CRYSTAL SOFTWARE …的芯片；

　　2） 然后，重新配置声卡，选CS4xxx选项；

　　3） 再填写好相应的I/O地址、IRQ中断、DMA即可。

　　如果你的声卡是Yamaha 724的话，请使用OSS来解决。

　　40.通用声卡安装程序OSS如何使用？

　　OSS是一款解决Linux下声卡难以配置问题的商业软件，它支持绝大部分的Linux发行版

　　1） 将下载的OSS软件包osslinux392v-glibc-2212-UP.tar.gz解压：

　　tar zxvf osslinux392v-glibc-2212-UP.tar.gz

　　2） 在解开的目录下执行./oss-install，程序一般会提示你已经安装了其它声卡模块，选择去掉；

　　3） 接下来就是处理过程、协议及一大堆东西，接受协议安装，使用默认安装路径即可(/usr/lib/oss)；

　　4） oss一般可以自动检测出大部分声卡，如果与你的实际情况相符，就直接在菜单中选择"Save changes and Exit.."就完成了设置；

　　5） 你可以使用/usr/lib/oss/soundon命令用来打开oss驱动，用/usr/lib/osssoundoff关闭oss驱动。

　　41.通用声卡安装程序ALSA如何使用？

　　ALSA，Advanced Linux Sound Architecture，是一个遵从GPL版权的通用PCI声卡解决软件。这个软件包括rpm和tar两种格式，其中rpm格式比较容易安装，这里就以rpm包为例介绍。

　　1）下载以下四个文件：

　　alsa-driver-0.4.1d-1.i386.rpm

　　alsa-lib-0.4.1d-1.i386.rpm

　　alsa-utils-0.4.1-1.i386.rpm

　　alsaconf-0.4.1-1.386.rpm

　　2）执行以下命令完成安装：

　　rpm -ivh alsa-driver-0.4.1d-1.i386.rpm

　　rpm -ivh alsa-lib-0.4.1d-1.i386.rpm

　　rpm -ivh alsa-utils-0.4.1-1.i386.rpm

　　rpm -ivh alsaconf-0.4.1-1.386.rpm

　　3） 然后执行alsaconf命令，选择合适的声卡类型；

　　4） 重新启动系统，然后执行命令：/usr/doc/alsa-driver/snddvices

　　42.Linux下如何安装Modem？

　　1） 在Windows中查看你的Modem位于什么端口上；

　　2） 在Linux中通过直接与端口交互来使用Modem，其对应关系如下：

　　COM1：/dev/cau0 COM2：/dev/cau1

　　COM3：/dev/cau2 COM4：/dev/cau3

　　3） 设置Modem的最高速率：

　　＃setserial /dev/cau1 spd.hi （最高速率设为57600bps）

　　＃setserial /dev/cau1 spd.vhi （最高速率设为115200bps）

　　43.如果通过Modem拔号上网？

　　1） 执行命令ln /dev/modem /dev/cau1（根据实际情况）

　　2） 创建一个脚本：touch sw，加入：

　　/usr/sbin/pppd connect ′/usr/sbin/chat ″ ″ ATDT163 CONNECT ″ ″ ogin:username word:password ′ /dev/modem 38400 modem defaultrout

　　将username与password用你的上网帐号和密码代入。

　　3） 你还可以使用KDE中的kppp工具方便地实现。

​     44.Linux下有图形界面吗？

 　　为了完善Unix系统的图形界面，麻省理工学院在1984开始了一个X-window开发计划，通过十余年的发展，X-window这一自由软件已经成为了Unix/Linux世界图形界面的事实标准。

　　X-window分为三个层次：

　　1）X-Window底层库，是最低实现层；

　　2）X-SERVER，与显卡相关的中间层；

　　3）窗口管理器，实现最终用户界面，如KDE、GNOME等。

　　45.如何配置X-Window？

　　所谓配置X-Window就是根据机器的实际设备选择X-SERVER。可以通过xf86config或图形化界面的Xconfigure等程序来配置。

　　1） 运行Xconfigure程序，然后选择合适的显卡类型，如果没有，则需要下载显卡的驱动；

　　2） 选择显存大小，和X-SERVER；

　　3） 选择合适的分辨率、色深组合

　　4） 存盘退出后，运行startx启动X-Window。

　　46.如何驱动intel i740显卡？

　　如果你的Linux无法识别i740的话，你可以这么做：

　　1）下载新的 显卡数据库 和 i740 XBF驱动程序：

　　xf86config-glibc-1.0.0.i386.tgz 和 xfcomi740.tgz

　　2）解压这两个包，覆盖原来目录：

　　tar xvfz /tmp/xf86config*.tgz

　　tar xvfz /tmp/xfcomi740.tgz

　　3）执行cp /usr/X11R6/bin/XFCom_i740 /usr/X11R6/bin/XF86_XBF_i740；

　　4）用xf86config进行配置：显示器水平扫描频率选6；垂直刷新频率选2；在显卡库选择时，选311（即i740）；显卡服务器类型选5；

　　5）配置完成后运行startx就行了。

　　47.如何驱动intel i810显卡？

　　Intel公司的两大显卡i740、i810都为Linux爱好者驱动带来不小麻烦，Intel公司为了以实际行动支持Linux，特意在网站上详细介绍了如何在Linux下配置i810显卡，你可以到下面的网址下载安装说明和软件：

　　48.如何驱动Savage4显卡？

　　1） 下载savage2000的驱动程序；

　　2） 使用tar -xvfz 文件名解开驱动程序；

　　3） 解压后，你能看到五个文件，其中有一个是XF86_SVGA；

　　4） 备份/usr/X11R6/bin/XF86_SVGA，然后将新的XF86_SVGA复制到这个目录下，替换掉这个文件；

　　5） 重新运行xf86config配置，不选显卡，在选X-server时，选3（也就是SVGA），并且不检测；

　　6） 完成后，运行startx -bpp32，就可以了。

　　49.如何驱动SAVAGE3D显卡？

　　1） 下载Savage3D显卡的驱动程序：SavageX_0_1_4.tar.gz；

　　2） 解压这个程序，用新的XF86_SVGA替换/usr/X11R6/bin的原文件；

　　3） 运行Xconfigurator,配置显卡时选择Unlisted Card, 然后选择Xserver为SVGA；

　　4） 完成后，运行startx运行x-win。

　　50.有没有通用的显卡驱动方法？

　　由于显卡产商支持有限，使得在Linux下驱动显卡一直都是难题。为了解决这个问题，Linux 2.2.x以上版本提供了一种新的解决方案---使用frame buffer设备，通过VESA VBE 2.0标准，利用显卡SVGA特性，配合XFree86的XF86_FBDev，驱动你的显卡。这的确可以帮你个忙。

　　1）确认你有XF86_FBDev文件

　　2）执行"mknod /dev/fb0 c 29 0"建立frame buffer设备；

　　3）修改/etc/lilo.conf文件，加入：

　　image = /boot/vmlinuz-2.2.5-fb （新编译的内核）

　　label = linuxfb （启动标号，可自定）

　　root = /dev/hda2 （参照lilo.conf其他部分）

　　vga = 0x314 （显示模式，参照下表）

　　附：显示模式表

　　640x480 800x600 1024x768 1280x1024

　　256色 0x301 0x303 0x305 0x307

　　32k色 0x310 0x313 0x316 0x319

　　64k色 0x311 0x314 0x317 0x31A

　　16M色 0x312 0x315 0x318 0x31B

　　4） 执行/sbin/lilo，使配置生效，然后重启系统，以新的内核启动系统。当然，如果你的内核已经支持了，就无需做这个修改，直接加上vga=那一行就行了。

　　5） 接着进行frame buffer Server的配置：参照/etc/X11/XF86Config中vga的配置，加入一个screen小节，如下所示：

　　Section "Screen"

　　Driver "fbdev"

　　Device "My Video Card"

　　Monitor "MAG XJ500T"

　　Subsection "Display"

　　Depth 16 (色深，须与前面所选显示模式的色深一致)

　　Modes "default"

　　ViewPort 0 0

　　EndSubsection

　　EndSection

　　6） 将X指向XF6_FBDev：

　　cd /etc/X11

　　mv X X.bat

　　ln -snf /usr/X11R6/bin/XF86_FBDev X

​     51.如何通过ISDN上网？

 　　ISDN的应用越来越普及，它速度快、价格便宜，深受网民的喜欢，那么在Linux下如何通过ISDN上网呢？

　　1） 确认你的Linux内核已经包含了对ISDN的支持模块；

　　2） 驱动ISDN卡：

　　对于非即插即用的Teles 16.3 ISDN卡可以使用命令：

　　＃modeprobe hisax io=0x180 irq=10 type=3 protocol=2 id=isdn0

　　对于即插即用型，则使用：

　　＃pnpdump〉/etc/isdn.conf

　　＃isapnp/etc/isdn.conf

　　＃modprobe hisax irq=10 io=0x680 type=14 protocol=2 id=isdn0

　　3） 安装Isdn4Linux，再执行scripts目录下的"makedev.sh"脚本程序，加入ISDN设备；

　　4） 执行echo 1〉/proc/sys/net/ipv4/ip_dynaddr命令让其支持动态IP；

　　5） 然后根据ppp的脚本再写一个用ISDN的脚本就行了。

　　52.如何在Linux下使用光驱？

　　1）创建一个目录，用来挂上光盘目录树：

　　mkdir /mnt/cdrom

　　当然目录名可以根据你自己的习惯命名；

　　2）插入光盘，执行"mount -t iso9660 /dev/hdc /mnt/floppy"命令；注意，如果你的光驱接在第一硬盘线的从盘上，需将/dev/hdc改为/dev/hdb；

　　3）然后你就可以通过访问/mnt/cdrom来实现对光盘访问；

　　4）当你不使用时，执行"umount /mnt/cdrom"，再取出光盘。

　　53.如何在Linux下使用软驱？

　　1） 与光盘类似，创建floppy目录；

　　2） 软盘插入后，执行"mount -t msdos /dev/fd0 /mnt/floppy"命令， 注：若是软盘中是长文件名格式的，将上条命令中的"msdos"改为"vfat"，若是 Linux文件格式，则去掉"-t msdos"；

　　3） 当你不使用时，执行"umount /mnt/floppy"，再取出软盘。

　　54.如何在Linux下读取非Linux分区的内容？

　　1） 创建一个目录：mkdir /mnt/other

　　2） 执行"mount -t 文件系统类型 分区 /mnt/other"命令；

　　注：文件系统类型包括：modos-FAT16、vfat-FAT32、ntfs-NTFS；

　　分区指该分区的设备名。

　　3） 当你不需要使用时，执行"umount /mnt/other"。

70.如何检查Linux硬盘使用情况？

 　　在Linux环境下，你可以使用df命令来查看硬盘的使用情况。下面就是一个df -T -h(-T参数：显示文件系统类型，-h参数用可读性较高的方式来显示信息)命令的输入实例：

　　Filesystem Type Size Used Avail Use% Mountedon

　　/dev/hda1 ext2 7.5G 4.7G 2.5G 65% /

　　/dev/hda2 ext2 653M 6.6M 613M 1% /root

　　/dev/hdb1 ext2 7.5G 3.5G 3.7G 49% /usr

　　71.Linux下有哪些压缩工具？

　　在Linux下有很多种压缩工具，常用的有：

　　1） gzip/gunzip：这是GNU开发的自由软件，使用相当广泛。压缩文件扩展名为".gz"。使用方法很简单，例如：

　　gunzip eos.gz gzip /home/test/*.txt；

　　2） compress/uncompress：这是一对历史悠久的压缩程序，文件经过它压缩后，压缩文件扩展名为 ".Z"。

　　3）除此之外还有：zip/unzip、bzip2/bunzip2等。

　　72.如何管理进程？

　　进程是程序的一次执行。可以使用"ps -auxw"列出在当前正在执行的进程的详细信息，包括每个进程都有的进程ID号。你可以通过"kill 进程ID号"来终止这个进程。

　　73.文件或目录的权限是什么意思？

　　文件或目录的权限位由10位构成，如-rwxr-xr-x。

　　1） 第一位代表文件/目录类型：d代表目录、-代表文件、l代表链接；

　　2） 剩下的9位分成3组，每组3位；2-4位描述文件主人的权限，5-7位描述与文件主人同一用户组的权限，8-10位则是其它用户的权限。

　　3） rwx：每组的3位分别是：读权限、写权限、执行权限；如果是-就代表没有这个权限。

　　也就是说-rwxr-xr-x表示，这是个普通文件，文件主人可以读、写、执行这个文件，与文件主人同组的用户以及其它用户都可以读、执行这个文件。

　　74.什么是用户帐号？

　　在Linux系统中，是通过用户帐号来标识每一个用户的，通过登录时输入不同的用户帐号和密码确定你的身份。也就是说，Linux系统通过用户帐号和管理系统的所有用户。

　　然后你可以创建一些用户组，将用户加入到组中去，让其获得用户组的权限。

　　75. 在Linux下，如何管理用户？

　　如果你想要新增一个用户：

　　1） 以root登录，然后执行"adduser 用户帐号名"

　　2） 执行"passwd 用户帐号名"来为这个用户帐号设置密码。

　　执行"userdel 用户帐号"删除一个用户；

　　执行"groupadd 用户组名"新增一个用户组；

　　执行"groupdel 用户组名"删除一个用户组；

​    \76. 如何为用户作磁盘限额？

 　　1）将要设置磁盘限额的分区，按以下格式修改/etc/fstab 文件：

　　/dev/hda2 /home ext2 defaults,usrquota 1 2

　　2）在要设置磁盘限额的分区目录下创建空文件 quota.user

　　#touch /home/quota.user

　　#chmod 600 /home/quota.user

　　3）重启系统后，就可以使用edquota -u 用户名来设置。

　　77.如何备份系统？

　　在Linux中，你可以使用dump/restore命令组来实现系统的备份与恢复。假设你需要将/usr目录下的所有文件完整地备份到磁带机上（假定设备是rmt8，不同的磁带机不相同），你可以使用命令：

　　dump -O -f /dev/rmt8 /usr

　　其中-O参数代表备份全部文件，"-f 设备文件名"参数指定备份到什么地方，最后的目录名指定要备份的内容。

　　然后，你可以使用以下命令恢复：

　　restore -r -f /dev/rmt8

　　78.如何安装.tar的软件包？

　　Linux软件有两种发布方式：一种是源代码方式，另一种是可执行文件包。而发布包大多是先用tar归档，再用gzip压缩，生成是以.tar.gz结束的文件。

　　你可以直接使用"tar xvfz 文件名"完成解压缩，解tar包工作。

　　如果你取得是可执行文件包，安装工作结束。

　　如果你取得是源代码包，则还需编译一下：

　　1） 在解压目录下运行"./configure"进行配置；

　　2） 在解压目录下运行"make"进行编译；

　　3） 运行"make install"安装。

　　79.如何使用RPM安装Linux软件？

　　RedHat公司提供的RPM工具，使得Linux软件安装更为方便。

　　1） 安装：rpm -ivh somesoft.rpm

　　2） 反安装：rpm -e somesoft.rpm

　　3） 查询：rpm -q somesoft

　　80.如果忘了root的密码，怎么办？

　　如果你忘了root的密码，可以通过以下方法恢复：

　　1） 重新启动Linux，出现lilo:时，输入linuxsingle进入单用户模式；

　　2） 这时无需密码就取得了root权限；

　　3） 再运行passwd重新设置root的密码。

　　81.重装Windows而破坏了Lilo时，怎么办？

　　这种情况可以使用两种方法恢复：

　　1）用Linux启动软盘启动，然后执行/sbin/lilo，重新在引导区建立lilo；

　　2）使用Linux安装光盘启动，选择升级系统，将会重建lilo。

　　82.如何制作Linux启动盘？

　　在Linux下，有一个工具mkbootdisk能很方便地制作系统启动盘：

　　1） 查看系统的版本，可以通过ls /usr/src来看；

　　2） 插入一张空软盘；

　　3） 执行"mkbootdisk --verbose 2.2.5"。

​    83.如何远程使用Linux？

 　　我们可以使用telnet、rlogin、rsh、rcp等命令来实现远程使用Linux，但这这些方法在传输过程中是明文传输的，所以有可能带来许多不安全因素。因此，应尽量避免远程使用root帐户登录系统。

　　如何构建安全的远程登录？

　　使用SSH来实现安全的远程登录，因为SSH实现了数据传输的加密。

　　1） 获取ssh-1.26.tar.gz文件；

　　2） 用tar xvpf ssh-1.26.tar.gz解开这个包；

　　3） 到解开的目录/usr/local/src/ssh-1.26目录下执行./configure；

　　4） 执行make和make install来完成编译和安装。

　　5） 你就可以使用ssh来与安装了SSH的服务器建立安全的远程连接。

　　85.如何运行计划任务？

　　大大可能对Windows中的计划任务都比较熟悉了，它可以通过一些简单的设置，定时完成一些任务。在Linux系统的维护中，我们可以也会需要定期执行一些任务，这种情况可以使用：

　　1） at命令：它可以键盘或文件中读取指令，然后在指定时间完执行；

　　2） crontab守候进程：通过设置它的配置文件来定时执行某些任务。

　　86.Linux的开机过程都做了什么？

　　1） 一开机，CPU将控制权交给BIOS，BIOS完成开机自检；

　　2） 然后BIOS读取磁盘上的第一个扇区，并装入主引导扇区的lilo；

　　3） lilo根据输入选择不同的内核映象，如果你选择了linux就读取/boot下的核心映象；

　　4） 核心开始硬件检测和设备驱动程序的初始化，然后运行init

　　5） init进程根据/etc/inittab的配置运行一系列初始化脚本；

　　6） 完成后，启动getty进程接受用户的登录。

　　87.如何设置开机自动运行程序？

　　你可以在以下几个脚本文件中加入你想一启动系统就执行的命令：

　　/etc/rc.local、/etc/rc.sysinit以及/etc/rc.d/init.d。

　　88.为什么需要重新编译内核？

　　以下情况你需要重新编译内核，或加入动态内核模块：

　　1） 更新驱动程序；

　　2） 根据自己的需求定制最可靠的内核；

　　3） 升级Linux内核。

　　89.如何重新编译内核？

　　1） 进入Linux源代码目录：cd /usr/src/linux

　　2） 执行"make config"或"make menuconfig"、"make xconfig"配置内核选项，选中你想要的模块，去掉不想要的模块；

　　3） 执行"make zImage"命令，大概30到90分钟后，会生成一个zImage的新内核映像文件，存放在/usr/src/linux/arch/i386/boot目录下；

　　4） 然后将其拷贝到/boot目录下；

　　5） 修改lilo.conf文件，加入：

　　image=/boot/zImage

　　label=newlinux

　　root=/dev/hda1 （根据原来的文件）

　　运行/sbin/lilo使修改生效。

　　6）重新启动，在Lilo时，输入newlinux就可以新内核启动。

90.什么是动态内核模块？

 　　动态内核模块是Linux一个成功的设计，它使得Linux更加灵活，易于定制。其实动态内核模块就是一个内核模块，它可以在不重新编译内核的情况，动态地将一些功能用"insmod 模块名"命令加入内核、用"rmmod 模块名"命令将其移出内核。

　　六、 廉价的网络解决方案---Linux：9问

　　91.如何使用Linux架设WEB服务器？

　　Apache服务器是在Linux架设WEB服务器的首选。你可以在安装Linux时就选择安装它。若在安装时没有安装Apache的话，你可以从光盘或者到apache网站上找到文件：apache-1.3.12.i386.rpm，然后执行以下命令完成安装：

　　1）rpm -ivh apache-1.3.12.i386.rpm

　　2）修改/etc/httpd/conf目录下的配置文件httpd.conf、access.conf等；

　　3）将主页文件放到/home/httpd/html目录下；

　　4）执行"/etc/rc.d/init.d/httpd start"启动Apache服务器

　　如果需要关闭的话，可以执行/etc/rc.d/init.d/httpd stop命令。

　　92.如何使用Linux架设FTP服务器？

　　在Linux中，最常用的FTP服务软件当数wu-ftpd，如果在安装linux时没安装上它。你可从光盘或者网站rpmfind.net/linux/RPM/WbyName.html获取它的RPM包：wu-ftpd-2.6.0-9.i386.rpm。然后执行以下命令完成安装：

　　rpm -ivh wu-ftpd-2.6.0-9.i386.rpm

　　编辑 "/etc/inetd.conf" 文件，指向新的ftpd守护进程，如下所示：

　　ftp stream tcp nowait root /usr/sbin/tcpd in.ftpd -l -a

　　到此为止，你的Linux就可以接受FTP服务了。

　　93.如何使用Linux架设E-MAIL服务器？

　　Linux中，最常用的E-MAIL服务器是Sendmail，你可以在安装Linux时将其选中。

　　1） 在DNS服务器上为E-Mail服务器做一条MX记录；

　　2） 编辑/etc/inetd.conf文件，将关于pop和smtp的行的注释符去掉；

　　3） 执行kill -HUP inetd，使修改生效；

　　这样E-mail服务器的用户就可通过Outlook等客户端程序进行收发邮件了。

　　94.如何使用Linux架设News服务器？

　　在安装Linux时，选择INN软件包，并允许开机时启动innd。在完成系统的安装时，大部分配置工作已经完成，无需编译源码。

　　1）配置/etc/news/inn.conf：

　　domain: foo.com

　　organization: foo company news site

　　server: localhost

　　根据实际情况填写；

　　2）配置/etc/news/nnrp.access

　　nnrp.access是用来完成News Readers服务的守候进程nnrpd的配置文件，用于控制对站点的访问，修改此文件无须启动INND。

　　3）添加新闻组：

　　可以手工编辑/var/lib/news/active文件添加新闻组，也可以使用ctlinnd命令来增加。若是手工方式修改新闻组，须执行以下命令使其生效：

　　ctlinnd reload active "modify active"

　　95.如何使用Linux架设BBS？

　　1） 下载PowerBBS的源代码发行包文件pbbs.tar.gz；

　　2） 执行tar zxvf pbbs.tar.gz解开文件；

　　3） 进入pbbs目录，运行Install；

　　4） 根据具体需求改变默认的设置。

　　96.如何让Linux成为文件服务器？

　　在Linux中，你可以用Samba来做文件服务器，你可以在安装Linux时选中Samba就可以完成安装。

　　1） 编辑/etc/smb.conf，修改配置：

　　　 netbios name=linux

　　workgroup=SambaServer

　　server string=Samba Server

　　hosts allow=192.168.9. 127.

　　　 securoty=share

　　interfaces=192.168.9.1/24

　　name resolve order=host dns bcast

　　wins support=no

　　2）重新启动SMB服务器：/etc/rc.d/init.d/smb restart

　　3）编辑客户机的hosts文件，加入对Samba Server的解析；

　　4）最后你就可以在网上邻居上看到它了。

​     97.如何使用Linux架设代理服务器？

 　　1） 下载Squid代理服务器软件squid-2.2.STABLE3-src.tar.gz；

　　2） 执行tar xzxf squid-2.2.STABLE3-src.tar.gz

　　3） 执行./configure

　　4） 执行make，make install安装到/usr/local/squid目录下；

　　5） 编辑/usr/local/squid/squid.conf文件，加入：

　　acl allowed_hosts src 192.168.9.0/255.255.255.0

　　注：假设你的内网IP地址是192.168.9.0；

　　6） 执行/usr/local/squid/bin/squid -z进行初始化

　　7） 执行/usr/local/squid/bin/squid开启服务

　　8） 在客户端设置代理服务器IP和端口3128，就可以访问Internet了。

　　98.如何使用Linux架设透明网关？

　　确认Linux内核已经支持ipchain，然后编写一个脚本ipchains.rule，内容为：

　　注：假设透明网关服务器的外网地址是：1.2.3.4，已经与Internet相连；内网地址是192.168.9.1，连在内网上。

　　#!/bin/sh

　　/sbin/ipchains -F forward

　　/sbin/ipchains -F input

　　/sbin/ipchains -F output

　　/sbin/ipchains -P forward DENY

　　/sbin/ipchains -P input ACCEPT

　　/sbin/ipchains -P output ACCEPT

　　external_interface=1.2.3.4

　　/sbin/ipchains -A input -j ACCEPT -i lo

　　/sbin/ipchains -A output -j ACCEPT -i lo

　　/sbin/ipchains -A input -j DENY -i eth1 -s 192.168.9.0/24

　　/sbin/ipchains -A input -j DENY -i eth1 -d 192.168.9.0/24

　　/sbin/ipchains -A output -j DENY -i eth1 -s 192.168.9.0/24

　　/sbin/ipchains -A output -j DENY -i eth1 -d 192.168.9.0/24

　　/sbin/ipchains -A input -j DENY -i eth1 -s $external_interface/32

　　/sbin/ipchains -A input -j DENY -i eth1 -s $external_interface/32

　　/sbin/ipchains -A output -j DENY -i eth1 -d $external_interface/32

　　/sbin/ipchains -A forward -j ACCEPT -i eth0 -s 192.168.9.0/24 -d 192.168.9.0/24

　　/sbin/modprobe ip_masq_ftp

　　/sbin/modprobe ip_masq_quake

　　/sbin/modprobe ip_masq_irc

　　/sbin/modprobe ip_masq_user

　　/sbin/modprobe ip_masq_raudio

　　/sbin/ipchains -A forward -j MASQ -i eth1 -s 192.168.9.0/24

　　运行这个脚本后，192.168.9.0网络中的所有机器只需将网关设置为192.168.9.1，就可以连到Internet上了。

　　99. Linux还能构建什么服务器？

　　Linux还可以成为域名服务器、PPP服务器、CVS服务器、路由器、防火墙，而且还可以通过LVS解决方式还构建服务器集群系统。