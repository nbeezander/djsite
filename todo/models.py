from django.db import models

# Create your models here.


class Todo(models.Model):
    content = models.CharField(verbose_name="Content", max_length=255)
    in_time = models.DateTimeField(verbose_name="In Time", auto_created=True,auto_now_add=True)
    edit_time = models.DateTimeField(verbose_name="Edit Time", auto_now=True)
    level = models.SmallIntegerField(verbose_name="Level", default=3)
    state = models.BooleanField(verbose_name="State", default=False)
    remarks = models.CharField(verbose_name="Remarks", max_length=1024, null=True)


class Child(models.Model):
    parent = models.ForeignKey(Todo,verbose_name="Todo")
    content = models.CharField(verbose_name="Content", max_length=255)

#
# class Article(models.Model):
#     content = models.TextField(verbose_name="内容", max_length=2048)
#     in_date = models.TimeField(verbose_name="创建日期", auto_created=True)
#     type = models.ForeignKey(ArticleType, verbose_name="类别")
#
#
# class ArticleType(models.Model):
#     name = models.CharField(verbose_name="分类名称", max_length=16)
#     intro = models.CharField(verbose_name="简介", max_length=32, null=True)