# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='in_time',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='In Time'),
        ),
    ]
