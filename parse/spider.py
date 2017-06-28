# !/usr/bin/env python 3
# encoding: utf-8

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class BasicSpider(scrapy.Spider):

    name='basic'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:

            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("is parseing")


if __name__ == '__main__':

    process = CrawlerProcess(get_project_settings())

    process.crawl(BasicSpider)
    process.start()