# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inTime', models.DateTimeField(auto_created=True, verbose_name='in time')),
                ('name', models.CharField(max_length=32, verbose_name='resource name')),
                ('intro', models.CharField(max_length=64, verbose_name='introduce')),
                ('link', models.CharField(max_length=128, verbose_name='link')),
                ('doc', models.CharField(max_length=2048, verbose_name='doc')),
                ('note', models.CharField(max_length=2048, verbose_name='note')),
                ('example', models.CharField(max_length=2048, verbose_name='e.g.')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='type name')),
                ('intro', models.CharField(max_length=16, verbose_name='introduce')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mining.Type', verbose_name='type'),
        ),
    ]
