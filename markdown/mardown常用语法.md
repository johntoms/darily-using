[TOC]

# Markdown基本语法

## 我是二级标题

### 我是三级标题

#### 我是四级标题

##### 我是五级标题

###### 我是六级标题

<font color=blue, size=12>目录语法</font>：

```markdown
在文章开始处添加 [toc] 回车即可。  
```



~~这是删除线~~



```markdown
~~这是删除线～～
```

`这是底纹`

```markdown
`这是底纹`
```

**这是加粗**

```markdown
**这是加粗**
```

*这是斜体*

```markdown
*这是斜体*
```

```markdown
目录
[toc]
标题格式
# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题

```

> 有序列表

1. 我是第一

2. 我是第二

3. 我是第三

   ```markdown
   1. 我是有序列表 一
   2. 我是有序列表 二
   3. 我是有序列表 三
   
   1.我是普通文本 一
   2.我是普通文本 二
   3.我是普通文本 三
   
   **注意⚠️** :语法后至少要有一个空格隔开，语法才会生效
   ```


> 无序列表

- 我是无序列表
- 我是无列表

```markdown
*或者- 加空格为创建一个无序列表
# example
- 我是无序列表
* 我是无序列表
```

> 插入图片

![大哥抽烟](/Users/johntoms/Desktop/software/markdown-file/大哥抽烟.jpg)

```markdown
图片插入格式：
![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")

详细叙述如下：

1. 一个惊叹号 !
2. 接着一个方括号，里面放上图片的替代文字
3. 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。


```

> 我是自动链接

[我是一个自动链接](www.cloudcare.cn)

[foo]: www.cloudcare.cn  "驻云，为您构建真正的架构云 "

```markdown
自动链接的格式：
[文字性描述](实际链接的网址：如 www.cloudcare.cn, https://www.cloudcare.cn)

[我是一个自动链接](www.cloudcare.cn)
```

