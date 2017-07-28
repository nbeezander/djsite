from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=16, verbose_name="分类名称")
    intro = models.CharField(max_length=16, verbose_name="简介")

    def __str__(self):
        return self.name


class Resource(models.Model):
    # 资源类；用来收集与呈现
    name = models.CharField(max_length=32, verbose_name="名称")
    intro = models.CharField(max_length=64, verbose_name="简介")
    link = models.CharField(max_length=128, verbose_name="链接")
    doc = models.TextField(max_length=2048, verbose_name="文档", null=True)
    note = models.CharField(max_length=2048, verbose_name="笔记", null=True)
    example = models.CharField(max_length=2048, verbose_name="示例", null=True)
    type = models.ForeignKey(Type, verbose_name="类型")
    inTime = models.DateTimeField(verbose_name='收录日期', auto_created=True)

    def __str__(self):
        return self.name
