# !/usr/bin/env python 3
# encoding: utf-8
# url.py create by zander on 2017/9/6 10:24

from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^translate/$',api.Translation.as_view(), name='translate')

]