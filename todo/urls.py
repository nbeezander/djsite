# !/usr/bin/env python 3
# encoding: utf-8
# urls.py create by zander on 2017/6/30 11:21
from django.conf.urls import url

from . import views
from . import api

urlpatterns = [
    url(r'^api_test$', views.api_test, name='api_test'),
    url(r'^references$', views.references, name='references'),
    url(r'^nlp', views.api_test, name='nlp'),
    url(r'^music$', views.music, name='music'),
    url(r'^css', views.css, name='css'),
    url(r'^q$', views.question, name='question'),
    url(r'^keyboard$', views.keyboard, name='keyboard'),
    url(r'^search$', views.todoFilter, name='search'),
    url(r'^words_hunter', views.words_hunter, name='words_hunter'),
    url(r'^api_words/$', api.WordsViewSet.as_view(),name="api_words"),
    url(r'^words/(?P<pk>[0-9]+)/$', api.WordDetail.as_view(),name="api_detail"),
    url(r'^words_random/$', api.WordsRandom.as_view(),name="words_random"),
    url(r'^questions/$', api.QuestionList.as_view(),name="questions"),
    url(r'^question/(?P<pk>[0-9]+)/$', api.GetOrUpdateQuestion.as_view(),name="get_update_question"),
    url(r'^last_question/$', api.LastQuestion.as_view(),name="last_question"),
    url(r'^create_question/$', api.CreateQuestion.as_view(),name="create_question"),
    url(r'^list/$', api.TodoList.as_view(),name="todo_list"),
    url(r'^new_todo/$', api.NewTodo.as_view(),name="new_todo"),
    url(r'^(?P<pk>[0-9]+)/$', api.GetOrUpdateTodo.as_view(),name="get_update_todo"),
    url(r'^delete_todo/(?P<pk>[0-9]+)/$', api.DeleteTodo.as_view(),name="delete_todo"),
]
