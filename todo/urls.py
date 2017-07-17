# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/6/30 11:21
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajax_add$', views.ajax_add, name='ajax_add'),
    url(r'^(?P<todo_id>[0-9]+)/ajax_edit/$', views.ajax_edit, name='ajax_edit'),
    url(r'^api_test$', views.api_test, name='api_test'),
    url(r'^ajax_add_child$', views.ajax_add_child, name='ajax_add_child'),
    url(r'^ajax_change_state$', views.ajax_change_state, name='ajax_change_state'),
    url(r'^references$', views.references, name='references'),
    url(r'^nlp', views.api_test, name='nlp'),
    url(r'^music$', views.music, name='music'),
    url(r'^search$', views.todoFilter, name='search'),

]
