# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/6/30 11:21
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajax_add$', views.ajax_add, name='ajax_add')
]
