# !/usr/bin/env python 3
# encoding: utf-8
# spider.py create by zander on 2017/6/23 18:21

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = []
    def __init__(self, rule):
        self.start_urls = rule['start_urls']
        super(MySpider, self).__init__()

    def parse(self, response):
        print("hhhhh========h")
        # for url in response.xpath('//a/@href').extract():
        #     yield scrapy.Request(url, callback=self.parse)


if __name__ == '__main__':
    import requests
    url = "http://localhost:8082/api/area!orgs.action"
    method = "get"
    headers = {'Content-Type': 'application/json'}
    data = {
    "province":"北京市",
    "city":"西城区"
}
    res = requests.request(method=method, url=url ,data=data,headers=headers )
    print(str(res.content,encoding="utf-8"))