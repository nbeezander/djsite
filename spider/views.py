from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse
# Create your views here.
import time
import json
from django.db import transaction
from bs4 import BeautifulSoup
import requests
from scrapy.selector import Selector
from django.views import generic
import os


def test(request):
    if request.method == "GET":
        return render(request, "spider/test.html")
    else:
        method = 'get'
        url = request.POST['url']
        rule = request.POST['rule']
        r_m = request.POST['method']
        extract = request.POST['extract']
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate, br'
        }

        res = requests.request(method=method,url=url,headers=headers)
        res.encoding = 'utf-8'

        se = Selector(response=res)

        result = getattr(getattr(se, r_m)(rule), extract)()
        d = {
            "html": res.text,
            "result": result
        }
        return HttpResponse(json.dumps(d))
