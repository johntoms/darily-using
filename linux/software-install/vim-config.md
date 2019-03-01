# vim-config
## 配置文件
> `.vimrc`

1. 我们已经知道`vim`的配置文件为`vimrc`文件，而且知道`vimrc`文件分为系统`vimrc`文件和用户`vimrc`文件。<span style="color:red">在通常情况下，我们不进行系统vimrc文件的修改，而是各个用户针对自己的需求对用户vimrc文件进行配置。</span>

2. `vimrc文件的路径`

    打开vim并输入":version"命令，就可以看到关于vimrc的路径设置规则:

    - Linux  Vim 配置文件路径

    ![ linux vim配置文件路径](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/vim%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84.jpeg)

    - Windows Vim 配置文件路径
      ![windows vim配置文件路径](https://oss-md-pictures.oss-cn-hangzhou.aliyuncs.com/window-vim%20%E9%85%8D%E7%BD%AE%E8%B7%AF%E5%BE%84.png)
3. `用户vimrc文件`
  通常在用户家目录下会有一个默认的`vimrc`文件，如果不存在则创建一个名为`.vimrc`的普通文本文件即可。

4. vim 常用配置
> `代码段`可以直接复制
```shell
" 缩进设置


" 设置 智能 tab 键
set smarttab

" 设置tab符长度为4个空格
set tabstop=4

" 设置换行自动缩进长度为4个空格
set shiftwidth=4

" 设置tab符自动转换为空格
set expandtab

" 设置智能缩进，其他可选缩进方式：autoindent, cindent, indentexpr
set smartindent
" 设置语法高亮
syntax on

" 字体设置
" 在Windows系统中为：set guifont=Courier_New:h12:cANSI
set guifont=Courier\ New\ 10

" 显示行号
" 设置显示行号，关闭行号显示命令：set nonumber
set number
" 配色方案
colorscheme desert


" 设置 256色
set t_Co=256

" 设置文件格式为 utf-8 格式
set encoding=utf-8
```