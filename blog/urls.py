# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/8/2 12:51

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.IndexView.as_view(), name="index"),
]