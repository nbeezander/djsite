# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/7/11 10:38

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^jieba$', views.sample, name="jieba"),
    url(r'^references', views.references, name="references"),
    url(r'^jieba_app', views.jieba_app, name="jieba_app"),
]