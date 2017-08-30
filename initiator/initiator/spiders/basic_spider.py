#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create by zander on 2017/06/24

import json
import scrapy
import pymysql
from websocket import create_connection
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
database = {
    "host":"127.0.0.1",
    "port": 3306,
    "db": "mysite",
    "user": "root",
    "password": "wgtamg",
    'charset':'utf8mb4',
}


class BasicSpider(scrapy.Spider):
    name = "initiator"

    def __init__(self, project_id):
        config = get_config(project_id)
        self.start_urls = config['start_urls']
        self.allowed_domains = config['allowed_domains']
        self.columns = config['columns']
        self.itemRules = config['rules']
        self.next_pager = config['next_pager']
        # 现在只允许存在一条解析连接的规则，，之后可能会添加更多
        self.link_rule = config['link_rule']
        self.ws = ws_client()
        super(BasicSpider, self).__init__()

    def parse(self, response):
        self.parse_url(response)
        self.parse_item(response)

    def parse_url(self, response):
        if self.next_pager:
            next_pager = response.css(self.next_pager).extract()
            for url in next_pager:
                if self.is_allow(url):
                    self.start_urls.append(url)
                    # send("url",url)

        if self.link_rule:
            links = response.css(self.link_rule).extract()
            for url in links:
                if self.is_allow(url):
                    self.start_urls.append(url)
                    # send("url", url)


    def parse_item(self, response):
        item = {}

        for rule in self.itemRules:
            item[rule['column']] = getattr(getattr(response,rule['method'])(rule['rule']),rule['extract'])(default="not_found")
        # send("item",item)
        print(item)
        self.ws.send("item",item)

    def is_allow(self,url):
        return True

    def close(spider, reason):
        print("hhhhhhhhhh=")
        spider.ws.close()



def get_config(project_id):
    """
    连接数据库获取配置文件
    :param project: project name str
    :return: str json data
    """
    conn = pymysql.connect(**database)
    cur = conn.cursor()
    project_id = int(project_id)
    cur.execute("SELECT * from spider_project as sp  WHERE sp.id = {}".format(project_id))
    project = cur.fetchone()

    cur.execute("SELECT su.link FROM spider_urls AS su WHERE su.project_id = {} AND su.parsed = 0 ".format(project_id))
    urls = cur.fetchall()

    cur.execute("SELECT * FROM spider_rules AS sr WHERE sr.project_id = {}".format(project_id))
    rules = cur.fetchall()

    config = {
        "id":project[0],
        "name":project[1],
        "columns":project[2].split(","),
        "allow_url":project[3] if project[3] else None,
        "allowed_domains":project[4].split(";") if project[4] else None,
        "next_pager":project[5] if project[5] else None,
        "link_rule":project[6] if project[6] else None,
        "start_urls":[url[0] for url in urls],
        "rules":[ {"column":rule[1],"rule":rule[2],"method":rule[3],"extract":"extract_first"} for rule in rules]
    }
    cur.close()
    conn.close()
    return config




class ws_client(object):

    def __init__(self):
        # TODO 设置可配置的地址
        self.ws = create_connection("ws://127.0.0.1:8100/spider/echo")

    def send(self,head,data):
        d = {
            "head":head,
            "data":data
        }
        self.ws.send(json.dumps(d,ensure_ascii=False))

    def colse(self):
        self.ws.close()
        pass



if __name__ == '__main__':
    # from scrapy.crawler import CrawlerProcess
    # from scrapy.utils.project import get_project_settings
    #
    # process = CrawlerProcess(get_project_settings())
    #
    # process.crawl(BasicSpider,10)
    # process.start()
    a = {"name":"你好"}
    b = json.dumps(a,ensure_ascii=False)
    c = json.loads(b)
    print(b)

