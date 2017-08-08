# !/usr/bin/env python 3
# encoding: utf-8
# spider.py create by zander on 2017/8/4 9:54

"""
@version: 0.1

架构：



TODO 0.2
    1. 数据库持久化
    2. requests time_out 策略
    3. 应对反爬虫的策略
        1. IP限制
        2. headers
    4. 文件爬取
        1. 图片
        2.
    5. 多线程
    6. 结束条件判定

"""
import requests
from scrapy.http.response import urljoin
from scrapy.selector import Selector
import pandas as pd
import numpy as np
import copy
from .models import Project, Url, Item


class Spider:
    """
    Parameters:
    ---------------------------
        project : 项目配置
        socket  : websocket default None
        ORM     : 是否数据库持久化 default False
        file    : 是否保存为文件 default True
    project:{
        'urls_set':[
            {
                'url':'',
                'method':'',
                ''
            }
        ]
    }
    """

    def __init__(self, project, socket=None, orm=False, file=True):
        if orm:
            self.project_id = project['id']
        self.name = project['name']
        self.start_urls = project['urls_set']
        self.urls_queue = copy.copy(project['urls_set'])
        self.urls_queue.reverse()
        self.url_set = set([url['url'] for url in self.start_urls])
        self.item_rules = project['item_rules']
        self.url_rules = project['url_rules']
        cols = []
        for rule in self.item_rules:
            cols.append(rule['name'])
        self.df = Container(row=128, cols=cols, socket=socket)
        self.finish = False
        self.orm = orm
        self.file = file

    def start(self):
        while self.is_over() and not self.finish:
            q = self.get_url()

            url = q['url']
            method = q['method']
            # data = q['data']
            # cookie = q['cookie']
            # session = q['session']
            headers = {}
            try:
                response = self.request(url, method)
                if self.orm:
                    uid = q['id']
                    UrlMiddleWare.update(uid=uid, state=1)
                self.parse(response)
            except TimeoutError as e:
                # 请求超时处理
                try:
                    response = self.request(url, method)
                    self.parse(response)
                except TimeoutError as e:
                    if self.orm:
                        uid = q['id']
                        UrlMiddleWare.update(uid=uid, state=2)
            except Exception as e:
                print("Exception:", e)
                self.close()
        self.close()

    def get_url(self):
        return self.urls_queue.pop()

    def request(self, url, method):
        response = requests.request(method=method, url=url)
        response.encoding = 'utf-8'
        return response

    def parse(self, response):
        self.parse_item(response)
        self.parse_url(response)
        pass

    def parse_item(self, response):
        ItemMiddleWare.parse(response=response, rules=self.item_rules, spider=self)
        pass

    def parse_url(self, response):
        UrlMiddleWare.parse(response=response, rules=self.url_rules, spider=self)
        pass

    def url_g(self):
        for url in self.start_urls:
            yield url

    def is_over(self):
        print("len:", self.df.cursor)
        if self.df.cursor >= 5:
            self.finish = True
        return len(self.urls_queue) > 0

    def save_data(self):
        pass

    def close(self):
        self.logger("spider close")
        self.df.save()

    def logger(self, msg):
        # 执行日志文件， 待持久化保存

        print("Logger:", msg)


class MiddleWare:
    def __init__(self, *args, **kwargs):
        pass

    pass


class ItemMiddleWare(MiddleWare):
    def __init__(self):

        super(ItemMiddleWare, self).__init__()

    @staticmethod
    def parse(response, rules, spider):
        res = Selector(response=response)
        rows = None
        for rule in rules:
            r = rule['rule']
            method = rule['method']
            extract = rule['extract']
            col_type = rule['type']
            col = rule['name']
            if col_type == 'img':
                pass
            else:
                c = getattr(getattr(res, method)(r), extract)(default="NA")
                if type(c) != list:
                    c = [c]
                if rows is not None:
                    rows[col] = c
                else:
                    rows = pd.DataFrame(c, columns=[col])

        spider.df.append(rows)
        pass


class UrlMiddleWare(MiddleWare):
    @staticmethod
    def parse(response, rules, spider):
        # 广度优先 or 深度优先
        res = Selector(response=response)
        base_url = response.url
        for rule in rules:
            method = rule['method']
            r = rule['rule']
            extract = rule['extract']
            urls = getattr(getattr(res, method)(r), extract)()

            for url in urls:
                if url not in spider.url_set:
                    ui = {
                        'url': urljoin(base_url, url),
                        'method': 'get',
                        'cookie': '',
                        'session': ''
                    }
                    if spider.orm:
                        uid = UrlMiddleWare.save(pid=spider.project_id, url=ui['url'])
                        ui['id'] = uid

                    spider.urls_queue.insert(0, ui)
                    spider.url_set.add(ui['url'])

        pass

        # @staticmethod
        # def save(response):
        #     url = response.url
        #     Url(url=url,state=1)
        #     pass

    @staticmethod
    def update(uid, state):
        url = Url.objects.get(pk=uid)
        url.state = state
        url.save()
        print("update-------")

    @staticmethod
    def save(pid, url, method="get", cookie=None, session=None):
        url = Url(project_id=pid, state=0, method=method, url=url, cookie=cookie, session=session)
        url.save()
        return url.id


# class Item:
#     "Item处理，item类型判定，保存方式"
#     pass


class Container:
    def __init__(self, row, cols, socket=None):
        l = len(cols)
        self.df = pd.DataFrame(np.array([np.nan] * row * l).reshape(row, l), columns=cols)
        self.cursor = 0
        self.size = row
        self.cols = cols
        self.socket = socket

        pass

    def append(self, series):
        if self.cursor >= self.size:
            xr = int(self.size / 2)
            self.df = self.df.append(
                pd.DataFrame(np.array([np.nan] * xr * len(self.cols)).reshape(xr, len(self.cols)), columns=self.cols),
                ignore_index=True)
            self.size += xr
        if isinstance(series, pd.DataFrame):
            for i in range(len(series)):
                self.df.ix[self.cursor, :] = series.ix[i, :]
                print(series.ix[i, :])
                self.cursor += 1
                self.send(series.ix[i, :])
        elif isinstance(series, pd.Series):
            self.df.ix[self.cursor, :] = series
            self.cursor += 1
            self.send(series)

    def save(self):
        self.df = self.df.dropna(how='all')
        self.df.to_csv("./data.csv", index=None, encoding='utf-8')
        self.close()

    def send(self, data):
        if self.socket is not None:
            self.socket.websocket.send(bytes(data.to_json(), encoding='utf-8'))

    def close(self):
        pass


class Setting:
    """
    在此处设置 请求 headers,延时策略，。。。

    """
    pass


if __name__ == "__main__":
    project = {
        'urls_set': [
            {
                'url': "https://baike.baidu.com/item/%E5%AE%BD%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2",
                'method': 'get',
                'cookie': "",
                'session': ''
            }
        ],
        'item_rules': [
            {
                'name': 'summary',
                'rule': 'string(//div[@class="lemma-summary"])',
                'method': 'xpath',
                'extract': 'extract_first',
                'col_type': 'col'
            }, {
                'name': "title",
                'rule': ".lemmaWgt-lemmaTitle-title h1::text",
                'method': 'css',
                'extract': 'extract_first',
                'col_type': 'col'
            }
        ],
        'url_rules': [
            {
                'name': 'link',
                'rule': '.lemma-summary a::attr(href)',
                'method': 'css',
                'extract': 'extract'
            }
        ]
    }

    spider = Spider(project=project)
    spider.start()
