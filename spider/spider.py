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
    # rule = {
    #     "start_urls":[
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]
    # }
    #
    # process = CrawlerProcess(get_project_settings())
    #
    # process.crawl(MySpider, rule)
    # process.start()
    import urllib
    from urllib import request
    from bs4 import BeautifulSoup
    from scrapy.selector import Selector
    from scrapy.http import HtmlResponse,TextResponse
    import requests
    import json

    a = requests.request("get","https://movie.douban.com/")

    ex = Selector(response=a).css("div.nav a::text").extract()

    d = {
        "html":a.text,
        "extract":ex
    }

    print(json.dumps(d))