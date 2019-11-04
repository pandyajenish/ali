# ali-images

- auto download aliexpress product images

## install

```baash
git clone git@github.com:xodeqa/aliImges.git
pip install scrapy pillow optimize-images pyinstaller
```

包功能说明

1. `scrapy` 爬虫
2. `pillow optimize-images` 图片优化
3. `pyinstaller` 打包成exe

## usage

### run scrapy by command

```bash
scrapy crawl images -a url=https://www.aliexpress.com/item/32948077843.html   # 默认压缩图片
scrapy.exe crawl images -a url=https://www.aliexpress.com/item/32948077843.html -a optimize_images='-n'   #不压缩图片
```

### run scrapy by exe

1. 执行打包脚本 `./py2exe.sh`
2. 打包完成后，可执行文件存放在 dist/crawl 目录
3. 使用

    ````bash
    dist/crawl/crawl.exe https://www.aliexpress.com/item/32948077843.html   # 默认压缩图片
    dist/crawl/crawl.exe https://www.aliexpress.com/item/32948077843.html -n # 不压缩图片
    ````
