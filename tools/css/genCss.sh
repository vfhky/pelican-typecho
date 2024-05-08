#!/bin/bash


if [ $# != 1 ] ; then
    echo "param err , usage : sh genCss.sh perldoc"
    exit
fi

# 2021_05_27_22_22_22
curDateTime=$(date +"%Y_%m_%d_%H_%M_%S")

# https://pygments.org/styles/
newCssName=$1
newCssFile=${newCssName}".css"
dstCssFile="pelican_vfhky_"${newCssName}".css"
dstMinCssFile='pelican_vfhky_'${newCssName}'.min.css'
BASE_CSS_FILE='pelican_vfhky_base.css'
LINE_NO_CSS_FILE='lineNo.css'
SCROLL_CSS_FILE='scroll.css'


rm -rf ${BASE_CSS_FILE}
wget -c https://cdn.typecodes.com/libs/css/pelican_vfhky_base.css?v=${curDateTime} -O ${BASE_CSS_FILE}
https://cdn.typecodes.com/libs/css/yuicompressor-2.4.8.jar
# wget -c https://github.com/yui/yuicompressor/releases/download/v2.4.8/yuicompressor-2.4.8.jar
wget -c https://cdn.typecodes.com/libs/css/yuicompressor-2.4.8.jar
pygmentize -S ${newCssName} -f html -a .highlight > ${newCssFile}
cat ${newCssFile} ${LINE_NO_CSS_FILE} ${SCROLL_CSS_FILE} ${BASE_CSS_FILE} > ${dstCssFile}
# compress
### apt install -y openjdk-8-jdk
#### 压缩单个示例：java -jar yuicompressor-2.4.8.jar pelican_vfhky_vs.css -o pelican_vfhky_vs.css.min.js --charset utf-8
#### 批量压缩示例：java -jar yuicompressor-2.4.8.jar -o  '.js$:-min.js' *.js   # 每个js文件都会生成对应的-min.js文件，例如 modaLbox.js => modaLbox-min.js
#### 合并多个文件示例：cat jquery-1.0.pack.js modaLbox.js | java -jar yuicompressor-2.4.8.jar --type js -o jquery-1.0.pack-comine.js
$(java -jar yuicompressor-2.4.8.jar ${dstCssFile} -o ${dstMinCssFile} --charset utf-8)
rm -rf ${dstCssFile}
echo "== ok -> ["${dstCssFile}"] ===> "${dstMinCssFile}" =="

