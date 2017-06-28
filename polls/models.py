#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create by zander on 2017/06/18

import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    # 数据库映射
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        # 格式化模型输出？
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # in_date = models.DateTimeField(default="2017/06/18")

    def __str__(self):
        return self.choice_text
