#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create by zander on 2017/06/21
import scrapy
from scrapy import crawler
from scrapy.http.headers import Headers
from scrapy.core import downloader
from scrapy import settings
from scrapy.commands import crawl
from scrapy.spider import BaseSpider



def start_requests():
    print("sss")
    urls = [
        'http://www.baidu.com',
        'http://quotes.toscrape.com/page/2/',
    ]
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

    h = Headers()
    h.setdefault("User-Agent",USER_AGENT)
    for url in urls:
        yield scrapy.Request(url=url,headers=h)


def parse(response):
    print(response)
    print(response.body)
    # page = response.url.split("/")[-2]
    # filename = 'quotes-%s.html' % page
    # with open(filename, 'wb') as f:
    #     f.write(response.body)
    # print('Saved file %s' % filename)


def fib():
    a,b = 0,1
    while True:
        a,b = b,a+b
        yield a


if __name__ == '__main__':
    # # print("start")
    # # a = start_requests()
    # # b = next(a)
    # # c = downloader.Downloader(b)
    # # print(c)
    # # print("end")
    # print(settings.Settings)
    pass

