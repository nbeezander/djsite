# !/usr/bin/env python 3
# encoding: utf-8
# api.py create by zander on 2017/9/8 9:59
import threading
import time
import queue
import numpy as np
import requests


# 非企业级框架，，不要那么在意效率。。。呃，
# RuntimeError: threads can only be started once


class Spider:
    def __init__(self, project, setting):
        self.tasks = queue.Queue()

    def crawl(self):
        i = 10
        while i > 0:
            threading.Thread(target=self.product()).start()
            time.sleep(1)
            threading.Thread(target=self.customer("t1")).start()
            threading.Thread(target=self.customer("t2")).start()
            i -= 1
        pass

    def product(self):
        # 生成任务
        i = np.random.randint(0, 100, 2)[0]
        j = np.random.randint(0, 100, 2)[1]
        self.tasks.put(i)
        self.tasks.put(j)
        pass

    def customer(self, name):
        # 消费任务
        print(name, self.tasks.get())
        pass


class RequestTask:
    """
    定义一个返回response的类，
    return response or throw exception
    有必要： 不要剔除！！
    """

    def __init__(self, url, method='get', headers=None, params=None, data=None, encoding='utf-8'):
        # requests.get()
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data
        self.encoding = encoding
        pass

    def get_response(self):
        try:
            response = requests.request(method=self.method,
                                        url=self.url,
                                        params=self.params,
                                        data=self.data,
                                        headers=self.headers)
            return response
        except TimeoutError:
            pass

        pass

    pass


class Setting:
    pass


class Project:
    pass


if __name__ == '__main__':
    # s = Spider()
    # s.crawl()
    res = requests.request(method='get', url="http://www.hahahavvvv.com")
    print(res.status_code)
