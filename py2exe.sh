#!/bin/bash
# python to exe 自动打包脚本，
# 参考： http://blog.hsuna.com/article.html?id=5c4d53c7e39bc1780deeb49f


python -V


ori_dir=/e/server/Python37-32/Lib/site-packages/scrapy   # scrapy 安装包所在目录
dist_dir=dist/crawl/scrapy   # 解决缺少 VERSION 的目录

rm -rf "dist/crawl" && \
    pyinstaller crawl.spec && \
    mkdir -p "$dist_dir" && \
    cp "$ori_dir/mime.types" "$ori_dir/VERSION" "$dist_dir/" && \
    dist/crawl/crawl.exe "https://www.aliexpress.com/item/32948077843.html"   # 打包成功后，可使用这个命令执行

