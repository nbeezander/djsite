# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/6/20 11:55
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add$', views.add_project, name='add'),
    url(r'^echo_once$', views.echo_once, name='once'),
    url(r'^echo$', views.echo, name='echo'),
    url(r'^test$', views.test, name='test'),
    url(r'^list$', views.ListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^crawl$', views.crawl, name='crawl')
    # url(r'^handle', views.handle, name='handle'),
    # url(r'^start$', views.create_parse, name="create")
]