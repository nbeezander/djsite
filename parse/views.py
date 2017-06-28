from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
import time
import os
from . import spider
import json
import pickle


ws = []

basic_data = {
    "method": ['GET', 'POST']
}


def send(item):
    ws.append(item)
    print("ws send:")
    print(ws)

# webscoket 连接者
users = []


@accept_websocket
def echo(request):
    users.append(request)
    print("now connect user is ", len(users))

    # ws = pickle.dumps(request)
    # print("ws:::::::",ws)
    # os.system("dir && cd spider && scrapy crawl basic -a ws=1231231")
    i=1
    while True:
        message = request.websocket.wait()
        data = {
            "name": "testName{}".format(i),
            "title": "testTitle{}".format(i),
            "url": "testUrl {}".format(i)
        }
        print("Message:",message)
        if message == b"close":
            break
        print("and now id ",len(users))
        for user in users:
            if user:
                user.websocket.send(json.dumps(data).encode())
    users.remove(request)

@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    request.websocket.send(message)


def index(request):
    return render(request, "parse/index.html", basic_data)


def handle(request):
    p1 = request.POST.get("m")
    print(p1)
    return HttpResponseRedirect(reverse('parse:index'))





def getWs():
    return spider.ws


# if __name__ == '__main__':
#     print("ss")
#     os.system("cd.. && dir && cd spider && scrapy crawl basic")
#     print("ss")

