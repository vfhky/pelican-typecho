#!/bin/bash



### 注意：ubuntu22.04 环境默认安装的是python3，所以这里的pip是python3的环境




# 删除已有的python版本
apt -y purge python-pip

# 更新下环境
apt update && apt upgrade

pip install pelican
# 非必需
pip install --upgrade pelican


# 安装summary插件 https://github.com/MinchinWeb/minchin.pelican.plugins.summary 。pelican 4.5+就不用再在配置文件里面配置了.
pip install minchin.pelican.plugins.summary

# 安装sitemap插件
pip install pelican-sitemap



# 非必选。用于生成代码高亮的css样式
pip install Pygments






