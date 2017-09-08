# !/usr/bin/env python 3
# encoding: utf-8
# spider.py create by zander on 2017/6/23 18:21
import requests
# 使用队列，生产消费模型

class Spider:

    def __init__(self):
        pass



    pass


if __name__ == '__main__':
    import requests
    import hashlib
    import json
    from scrapy.selector import Selector

    url = "http://localhost:8082/api/repair!progress.action"
    url2 = "http://47.90.46.65:8820/api/repair!progress.action"
    url3 = "https://translate.google.cn/#en/zh-CN/still"
    method = "get"
    headers = {'Content-Type': 'application/json'}
    salt = "gome"
    data = {
        "gomeAccount": "80000057",
        # "imei": "845216351212548",
        # "reservationNumber": "YY1708090002",
        # "model": "X1",
        # "appointNetwork": "国美电器手机维修中心（长宁店）",
        # "problemDetail": "通话异常，我打开你发达科技孵化基地数据恢复数据库的戴菲菲的的手感十分广泛大使馆犯得上广泛费功夫的各色灯光分散对方",
        # "appointment": "2017-06-29 18:00:00",
        # "name": "张三",
        # "tel": "15370467818",
        # "accessType": "TYPE1",
        # "reservationType": "TYPE1",
        # "serviceType": "TYPE1",
        # "province": "湖南省",
        # "city": "长沙市",
    }

    def get_sign(data):
        fm5 = ""
        fm5 += salt
        l = list(data.keys())
        l.sort()
        for k in l:
            fm5 += k
            fm5 += data[k]
        fm5 += salt
        print(fm5)
        m5 = hashlib.md5(fm5.encode("utf-8")).hexdigest().upper()
        print(m5)
        return m5


    data['sign'] = get_sign(data)

    res = requests.request(method=method, url=url2, data=json.dumps(data), headers=headers)
    print(str(res.content, encoding="utf-8"))
