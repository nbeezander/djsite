# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/6/20 11:55
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test$', views.test, name='test'),
]