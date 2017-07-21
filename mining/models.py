from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=16, verbose_name="type name")
    intro = models.CharField(max_length=16, verbose_name="introduce")

    def __str__(self):
        return self.name


class Resource(models.Model):
    # 资源类；用来收集与呈现
    name = models.CharField(max_length=32, verbose_name="resource name")
    intro = models.CharField(max_length=64, verbose_name="introduce")
    link = models.CharField(max_length=128, verbose_name="link")
    doc = models.CharField(max_length=2048, verbose_name="doc", null=True)
    note = models.CharField(max_length=2048, verbose_name="note", null=True)
    example = models.CharField(max_length=2048, verbose_name="e.g.", null=True)
    type = models.ForeignKey(Type, verbose_name="type")
    inTime = models.DateTimeField(verbose_name='in time', auto_created=True)

    def __str__(self):
        return self.name
