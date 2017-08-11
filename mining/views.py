from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Resource, Type, Project, Item, Rule, Headers, Url
from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from dwebsocket.decorators import accept_websocket, require_websocket
from .spider import Spider


# Create your views here.


class ResourceList(ListView):
    template_name = "mining/resource.html"
    context_object_name = "resource_list"

    def get_queryset(self):
        fil = {

        }
        if 'type__name' in self.request.GET:
            fil['type__name'] = self.request.GET['type__name']
        return Resource.objects.filter(**fil).order_by("type__name").all()
        pass

    pass


class IndexList(ListView):
    template_name = "mining/resource.html"
    context_object_name = "type_list"

    def get_queryset(self):
        return Type.objects.all()


class ProjectList(ListView):
    template_name = "mining/spider.html"
    context_object_name = "project_list"

    def get_queryset(self):
        return Project.objects.order_by("-create_time").all()


def projectDetail(request):
    pro = get_object_or_404(Project, pk=request.POST['project_id'])
    cols = pro.rule_set.filter(type__in=['item']).all().values("name")
    urls = pro.url_set.filter(state=0).all().values("url")
    data = {
        'cols': [c['name'] for c in cols],
        'urls': [u['url'] for u in urls]
    }
    return HttpResponse(json.dumps(data))


def spider(request):
    return render(request, "mining/spider.html")


@accept_websocket
def crawl(request):
    pid = request.GET['id']
    project = pro_format(pid)
    print(project)
    # project = {
    #     'name': "baidu",
    #     'urls_set': [
    #         {
    #             'url': "https://baike.baidu.com/item/%E5%AE%BD%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2",
    #             'method': 'get',
    #             'cookie': "",
    #             'session': ''
    #         }
    #     ],
    #     'item_rules': [
    #         {
    #             'name': 'summary',
    #             'rule': 'string(//div[@class="lemma-summary"])',
    #             'method': 'xpath',
    #             'extract': 'extract_first',
    #             'col_type': 'col'
    #         }, {
    #             'name': "title",
    #             'rule': ".lemmaWgt-lemmaTitle-title h1::text",
    #             'method': 'css',
    #             'extract': 'extract_first',
    #             'col_type': 'col'
    #         }
    #     ],
    #     'url_rules': [
    #         {
    #             'name': 'link',
    #             'rule': '.lemma-summary a::attr(href)',
    #             'method': 'css',
    #             'extract': 'extract'
    #         }
    #     ]
    # }
    # while True:
    #     message = request.websocket.wait()
    #     request.websocket.send(b"ssss")
    # request.websocket.send(b"ssssss")
    spider = Spider(project=project, socket=request, orm=True)
    spider.start()


def pro_format(pid):
    pro = get_object_or_404(Project,pk= pid)
    urls_set = Url.objects.filter(project=pro, state=0).all()
    item_rules = Rule.objects.filter(project=pro, type__in=['item']).all()
    url_rules = Rule.objects.filter(project=pro, type='url').all()

    res = {
        "id":pro.id,
        "name": pro.name,
        "urls_set": [{
            'id':url.id,
            'url': url.url,
            'method': url.method,
            'session': url.session,
            'cookie': url.cookie,
            'data': url.data
        } for url in urls_set],
        "item_rules": [{
            'name': item.name,
            'rule': item.rule,
            'method': item.method,
            'extract': item.extract,
            'type': item.type
        } for item in item_rules],
        "url_rules": [
            {
                'name': url.name,
                'rule': url.rule,
                'method': url.method,
                'extract': url.extract
            } for url in url_rules
        ]
    }
    return res
