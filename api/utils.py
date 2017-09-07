# !/usr/bin/env python 3
# encoding: utf-8
# utils.py create by zander on 2017/9/6 10:23
import requests

"""
    静态方法：返回josn数据
"""


class YoudaoTranslation:
    @staticmethod
    def trnaslate(word,*args,**kwargs):
        url = 'http://fanyi.youdao.com/openapi.do'
        params = {
            'key': '734178784',
            'keyfrom': 'dict633366-api',
            'type': 'data',
            'doctype': 'json',
            'version': '1.1',
            'q': word
        }

        res = requests.get(url=url, params=params)
        return res.json()
