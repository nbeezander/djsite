# !/usr/bin/env python 3
# encoding: utf-8
# from.py create by zander on 2017/8/16 10:05

from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields = '__all__'

    pass