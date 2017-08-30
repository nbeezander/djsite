# !/usr/bin/env python 3
# encoding: utf-8
# spider.py create by zander on 2017/6/23 18:21
import requests


class Project:
    def __init__(self, start_urls, allow_url, item_rules, url_rules):
        pass

    pass


class Rule:
    pass


class Url:
    def __init__(self, url, method='GET', data=None, headers=None, cookie=None, session=None):
        pass

    pass


class Headers:
    pass


class Spider:
    def __init__(self, project, ploy='BFS', threads=1):
        self.start_urls = project.start_urls

        if ploy in ['BFS', 'DFS']:
            self.ploy = ploy
        else:
            self.ploy = 'BFS'

        pass

    def parse(self):
        pass

    def response(self):
        pass

    pass


config = {
    'headers': {

    }

}

if __name__ == '__main__':
    import requests
    import json

    url = "http://localhost:8082/api/reserve!cancel.action"
    method = "post"
    headers = {'Content-Type': 'application/json'}
    salt = "gome"
    data = {
        "gomeAccount": "xxxxxxx",
        "imei": "845216351212548",
        "reservationNumber": "YY1707250004",
        # "model": "X1",
        # "appointNetwork": "国美电器手机维修中心（长宁店）",
        # "problemDetail": "通话异常，我打开你发达科技孵化基地数据恢复数据库的戴菲菲的的手感十分广泛大使馆犯得上广泛费功夫的各色灯光分散对方",
        # "appointment": "2017-06-29-18:00",
        # "name": "张三",
        # "tel": "13954687512",
        # "accessType": "TYPE1",
        # "reservationType": "TYPE1",
        # "serviceType": "TYPE1",
        "sign": "9E31C260292F26197E445482D2FDAD55"
    }

    res = requests.request(method=method, url=url, data=json.dumps(data), headers=headers)
    print(str(res.content, encoding="utf-8"))
