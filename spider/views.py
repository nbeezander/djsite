from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse
# Create your views here.
import time
import json
from .models import Project,Urls,Rules,Data
from django.db import transaction
from bs4 import BeautifulSoup
import requests
from scrapy.selector import Selector
from django.views import generic
import os



def index(request):
    return render(request, "spider/index.html")


@transaction.atomic
def add_project(request):
    if request.method == 'GET':
        return render(request, "spider/add.html",{"method":"GET"})
    else:
        project = request.session['project']
        urls = request.session['urls']
        rules = request.session['rules']
        p = Project(**request.session['project'])
        p.save()
        for url in urls:
            # url['project'] = p
            url = Urls(project=p,**url)
            url.save()

        for rule in rules:
            # rule['project'] = p
            rule = Rules(project=p,**rule)
            rule.save()
        return render(request, "spider/add.html",{"method":"post"})


def test(request):
    if request.method == "GET":
        return render(request, "spider/test.html")
    else:
        method = 'get'
        url = request.POST['url']
        rule = request.POST['rule']
        r_m = request.POST['method']

        res = requests.request(method=method,url=url)

        se = Selector(response=res)

        result = getattr(se,r_m)(rule).extract()
        d = {
            "text":res.text,
            "extract":result
        }
        return HttpResponse(json.dumps(d))


def edit_project(request):

    pass


users = []
crawled = False


@accept_websocket
def echo(request):
    users.append(request)
    print("now connect user is ", len(users))
    while True:
        message = request.websocket.wait()
        print("Message:",message)
        if message == b"close":
            break
        for user in users:
            if user:
                user.websocket.send(message)
    users.remove(request)


@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    print(message)
    # rule = {
    #     "start_urls": [
    #         'http://baike.baidu.com/item/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/9180'
    #     ]
    # }
    # create_parse(rule)
    request.websocket.send(b"sss")


class ListView(generic.ListView):
    template_name = 'spider/list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Project.objects.all()


class DetailView(generic.DetailView):
    model = Project
    template_name = "spider/detail.html"

    def get_queryset(self):
        return Project.objects.all()


class IndexView(generic.ListView):
    template_name = "spider/index.html"
    context_object_name = "project_list"

    def get_queryset(self):

        return Project.objects.all()


def crawl(request):
    """

    :param request:
    :return:
    """
    # print(request.META)
    project_id = request.POST['project_id']
    command = "cd initiator && scrapy crawl initiator -a project_id={}".format(project_id)
    print(command)
    os.system(command)
    return HttpResponse("")