from django.db import models


# Create your models here.


class Todo(models.Model):
    content = models.CharField(verbose_name="Content", max_length=255)
    # in_time = models.DateTimeField(verbose_name="In Time", auto_created=True)
    create_time = models.DateTimeField(verbose_name="Create", auto_now_add=True)
    # edit_time = models.DateTimeField(verbose_name="Edit Time", auto_now=True)
    # level = models.SmallIntegerField(verbose_name="Level", default=3)
    state = models.BooleanField(verbose_name="State", default=False)
    # remarks = models.CharField(verbose_name="Remarks", max_length=1024, null=True)


class Question(models.Model):
    # 未make ，make之后删除该注释，，长度限制(i)，，markdown(i)
    desc = models.CharField(verbose_name="问题", max_length=255)
    in_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    re_time = models.DateTimeField(verbose_name="解决时间", auto_now=True)
    state = models.BooleanField(verbose_name="状态", default=False)
    answer = models.CharField(verbose_name="答案", max_length=255,null=True,blank=True)

    # class Child(models.Model):
    #     parent = models.ForeignKey(Todo,verbose_name="Todo")
    #     content = models.CharField(verbose_name="Content", max_length=255)

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


class Words(models.Model):
    word = models.CharField(verbose_name="word", max_length=32, unique=True)
    level = models.IntegerField(verbose_name="level", default=1)
    hp = models.IntegerField(verbose_name="hp", default=5)
