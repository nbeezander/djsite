# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/7/21 14:51

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^resource$', view=views.IndexList.as_view(), name='resource')

]