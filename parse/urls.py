# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/6/20 11:55
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^echo_once', views.echo_once, name='index'),
    url(r'^echo$', views.echo, name='echo'),
    url(r'^handle', views.handle, name='handle'),
]
