# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0004_auto_20170803_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='name',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='url',
            name='state',
            field=models.IntegerField(choices=[(0, '新增'), (1, '完成'), (2, '失败')], default=0, verbose_name='状态'),
        ),
    ]
