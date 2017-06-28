from django.db import models
from django.utils import timezone
# Create your models here.
# 爬虫


class Project(models.Model):
    name = models.CharField(verbose_name="Project Name", max_length=64)
    create_date = models.DateTimeField(verbose_name="Create Date", auto_now_add=True)
    # 暂停点
    pass


class Urls(models.Model):
    """
    地址管理
    """
    path = models.CharField(verbose_name="URL path", max_length=128)
    name = models.CharField(verbose_name="Pager Title", max_length=32)
    state = models.BooleanField(verbose_name="Is parsed?", default=False)
    project = models.ForeignKey(Project)
    in_date = models.DateTimeField(verbose_name="In Date", auto_now_add=True)
    parse_date = models.DateTimeField(verbose_name="Parse Date")
    pass


class Jdata(models.Model):
    project = models.ForeignKey(Project)
    json = models.CharField(verbose_name="JSON Data",max_length=1024)
    pass