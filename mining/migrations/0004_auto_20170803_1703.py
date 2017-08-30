# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0003_auto_20170727_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='域')),
            ],
        ),
        migrations.CreateModel(
            name='Headers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(blank=True, default='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36', max_length=128, null=True, verbose_name='User-Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_created=True, verbose_name='添加时间')),
                ('data', models.TextField(verbose_name='数据')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, verbose_name='创建日期')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('request_headers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mining.Headers', verbose_name='请求头')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(max_length=64, verbose_name='规则')),
                ('extract', models.CharField(choices=[('extract_first', 'extract_first'), ('extract', 'extract')], default='extract_first', max_length=12, verbose_name='解析')),
                ('method', models.CharField(choices=[('css', 'css'), ('xpath', 'xpath')], default='css', max_length=8, verbose_name='方法')),
                ('type', models.CharField(choices=[('item', 'Item'), ('url', 'URL')], default='item', max_length=8, verbose_name='类型')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mining.Project', verbose_name='项目')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=128, verbose_name='链接')),
                ('state', models.IntegerField(choices=[(0, '新增'), (1, '完成'), (2, '失败')], max_length=2, verbose_name='状态')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST')], default='get', max_length=8, verbose_name='方法')),
                ('data', models.CharField(blank=True, max_length=128, null=True, verbose_name='数据')),
                ('cookie', models.CharField(blank=True, max_length=128, null=True, verbose_name='Cookie')),
                ('session', models.CharField(blank=True, max_length=128, null=True, verbose_name='Session')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mining.Project', verbose_name='项目')),
            ],
        ),
        migrations.AlterField(
            model_name='resource',
            name='doc',
            field=models.TextField(blank=True, max_length=2048, null=True, verbose_name='文档'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='example',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='示例'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='note',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='笔记'),
        ),
        migrations.AddField(
            model_name='item',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mining.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='domain',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mining.Project', verbose_name='项目'),
        ),
    ]
