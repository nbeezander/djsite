# !/usr/bin/env python 3
# encoding: utf-8
# utils.py create by zander on 2017/9/6 10:23
import requests
import hashlib
"""
    静态方法：返回josn数据
"""


class YoudaoTranslation:
    @staticmethod
    def translate(word, *args, **kwargs):
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


class BaiduTranslation:

    @staticmethod
    def translate(word, *args, **kwargs):
        url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
        appid = "20170913000082559"
        salt = "2017"
        key = "4fUCEBGRjY7njJiv3MB7"

        to_sign = appid+word+salt+key
        sign = hashlib.md5(to_sign.encode("utf-8")).hexdigest()
        params = {
            "q":word,
            "from":"en",
            "to":"zh",
            "appid":appid,
            "salt":salt,
            "sign":sign
        }
        # return sign

        res = requests.get(url,params=params)
        return res.json()


class BaiduV2transapi:

    @staticmethod
    def getDate(word, *args, **kwargs):
        url = "http://fanyi.baidu.com/v2transapi"
        params = {
            "from": "en",
            "to": "zh",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": 3
        }
        res = requests.get(url=url,params=params)
        return res.json()

