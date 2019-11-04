# -*- coding: utf-8 -*-
import scrapy
import re
import json
import urllib.request
import os
import time

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.aliexpress.com']
    # start_urls = ['https://www.aliexpress.com/item/32948077843.html']
    start_urls = []

    def __init__(self, url=None):
        if url is None:
            raise '"Error, URL is empty, Please use command: scrapy crawl images -a url="https://www.aliexpress.com/item/32948077843.html"'
        else:
            self.start_urls.append(url)

    def parse(self, response):
        for sel in response.xpath('//script[contains(., "window.runParams")]/text()').extract():
            # print(sel)
            pattern = re.compile(r".*data: (.*?)csrfToken",
                                 re.MULTILINE | re.DOTALL)
            desc = pattern.findall(sel)[0].strip().rstrip(',')
            json_obj = json.loads(desc)
            # 大图
            imgs = json_obj['imageModule']['imagePathList']

            if len(imgs) > 0:
                now = time.strftime("%Y%m%d-%H%M%S")
                path = 'output/' + now
                os.makedirs(path)
                print("output path: " + path)
            else:
                print('Error: list is empty, exit')
                return

            i = 0
            for url in imgs:
                print(url)
                self.downloadImage(url, i, path)
                i += 1

    def downloadImage(self, url, index, path):
        # file name
        if index < 10:
            prefix = '0' + str(index)
        else:
            prefix = str(index)

        filename = os.path.join(path, prefix + '-' + url.split('/')[-1])
        print(filename.replace('\\', '/'))
        urllib.request.urlretrieve(url, filename)
