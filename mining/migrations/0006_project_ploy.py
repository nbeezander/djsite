# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0005_auto_20170803_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ploy',
            field=models.CharField(choices=[('BFS', '广度优先'), ('DFS', '深度优先')], default='BFS', max_length=12, verbose_name='策略'),
        ),
    ]