#!/bin/bash
# pelican编译并打包
# (c) 2024.5.4 vfhky https://typecodes.com/mix/pelicanaddgitcommitcicdinfo.html
# Simple Usage:  sh autoGenAndPublish.sh /home/typcodes/github/tp_code github_token "abcded" "101"


if [ $# -ne 4 ]; then
  echo "pelican编译脚本必须输入构建路径参数"
  exit 1
fi


# 根路径
WORKING_DIR=$1
GITHUB_TOKEN=$2
# 构建id
BUILD_ID=$3
BUILD_CUR_ID=$4
BUILD_DATE=$(date +%Y.%m.%d)

# github commitId
COMMIT_ID=''
COMMIT_DATE=''

# target
TARGET='blog.tar.gz'
PELICAN_CONF='pelicanconf.py'

# 修改配置文件
replaceGitAndBuildInfo() {
    if [ ! -e "${PELICAN_CONF}" ]; then
        echo "配置文件${PELICAN_CONF}不存在"
        exit 0
    fi
    
    sed -i "s/COMMIT_ID = ''/COMMIT_ID = '$1'/" "${PELICAN_CONF}"
    sed -i "s/COMMIT_DATE = ''/COMMIT_DATE = '$2'/" "${PELICAN_CONF}"
    sed -i "s/BUILD_ID = ''/BUILD_ID = '$3'/" "${PELICAN_CONF}"
    sed -i "s/BUILD_CUR_ID = ''/BUILD_CUR_ID = '$4'/" "${PELICAN_CONF}"
    sed -i "s/BUILD_DATE = ''/BUILD_DATE = '$5'/" "${PELICAN_CONF}"
}


cd "${WORKING_DIR}" \
&& rm -rf ./content/articles \
&& mkdir -p ./content/articles \
&& cd ./content/articles \
&& git clone -b master "https://${GITHUB_TOKEN}:x-oauth-basic@github.com/vfhky/blogArticle.git" . \
&& COMMIT_ID=$(git rev-parse --short HEAD) \
&& COMMIT_DATE=$(git log -1 --format=%cd --date=format:'%Y.%m.%d') \
&& cd "${WORKING_DIR}" || exit

# 修改配置文件
replaceGitAndBuildInfo "${COMMIT_ID}" "${COMMIT_DATE}" "${BUILD_ID}" "${BUILD_CUR_ID}" "${BUILD_DATE}"

# 编译并打包
make publish \
&& tar -zcf "${TARGET}" -C output/ .
