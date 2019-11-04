# ali-images

- auto download aliexpress product images

## usage

```bash
scrapy crawl images -a url=aliexpress_product_url
```

## scrapy to exe

1. 执行打包脚本 `./py2exe.sh`
1. 打包完成后，可执行文件存放在 dist/crawl 目录
1. 使用 `dist/crawl/crawl.exe your_url`
