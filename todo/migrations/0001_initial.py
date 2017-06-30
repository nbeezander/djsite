# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField(auto_created=True, verbose_name='In Time')),
                ('content', models.CharField(max_length=255, verbose_name='Content')),
                ('edit_time', models.DateTimeField(auto_now=True, verbose_name='Edit Time')),
                ('level', models.SmallIntegerField(default=3, verbose_name='Level')),
                ('state', models.BooleanField(default=False, verbose_name='State')),
                ('remarks', models.CharField(max_length=1024, null=True, verbose_name='Remarks')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Todo', verbose_name='Todo'),
        ),
    ]