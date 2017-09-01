# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/7/21 14:51

from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^resource$', view=views.IndexList.as_view(), name='resource'),
    url(r'^spider$', view=views.ProjectList.as_view(), name='spider'),
    url(r'^detail$', view=views.projectDetail, name='detail'),
    url(r'^crawl$', view=views.crawl, name='crawl'),
    url(r'^csv_download$', view=views.csv_download, name='csv_download'),
    url(r'^pic_upload', view=views.pic_upload, name='pic_upload'),
    url(r'^resource_create$', view=api.ResourceCreate.as_view(),name='resource_create'),
    # url(r'^resource_create$', view=api..as_view(),name='resource_create'),
    url(r'^type_list', view=api.TypeList.as_view(),name='type_list'),
    url(r'^type/(?P<pk>[0-9]+)/', view=api.TypeDetail.as_view(),name='type_detail')

]