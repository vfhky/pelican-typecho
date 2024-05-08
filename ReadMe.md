### 一、主题说明

一款用于pelcian博客的主题，移植自[Typecho](https://typecho.org/)官网的皮肤，所以取名为`pelican-typecho`。

目前是[我自己的博客](https://typecodes.com)在用，欢迎大家体验。


### 二、目录结构
```
.
├── Makefile                # pelican官方文件
├── ReadMe.md
├── autoGenAndPublish.sh    # 用于自动构建的脚本。如果你未使用自己的构建平台，该文件可以忽略。
├── content                 # 用于存放favicon等文件，以及存放md文档目录。
├── develop_server.sh       # pelican官方文件
├── fabfile.py              # pelican官方文件
├── pelican-themes          # pelican的主题目录。下面的 pelican-typecho 即是当前博客使用的主题。
├── pelicanconf.py          # pelican的配置文件。按需修改
├── publishconf.py          # pelican官方发布文件
└── tools                   # 用于pygments生产代码高亮的样式
```


### 三、使用方法

#### 3.1 安装 pelican 所有的环境

这里以 ubuntu 系统为例：

```
apt install -y make python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install --upgrade --default-timeout=100 install tzdata pelican \
        markdown pelican-sitemap Pygments minchin.pelican.plugins.summary \
        -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

#### 3.2 编译生成博客

把自己的markdown文件放在`content/articles`目录下，然后在根目录执行 `make publish` 即可生成博客html文件。


