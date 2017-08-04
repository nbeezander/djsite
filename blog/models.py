from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="类别名称", max_length=32)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(verbose_name="标签名称", max_length=32)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, verbose_name="作者")
    title = models.CharField(verbose_name="标题", max_length=32)
    summary = models.CharField(verbose_name="摘要", max_length=256, null=True, blank=True)
    content = models.TextField(verbose_name="内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_created=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    category = models.ForeignKey(Category, verbose_name="分类")
    tags = models.ManyToManyField(Label, verbose_name="标签")

    def __str__(self):
        return self.title
