from django.db import models

# Create your models here.


class Todo(models.Model):
    content = models.CharField(verbose_name="Content", max_length=255)
    in_time = models.DateTimeField(verbose_name="In Time", auto_created=True)
    edit_time = models.DateTimeField(verbose_name="Edit Time", auto_now=True)
    level = models.SmallIntegerField(verbose_name="Level", default=3)
    state = models.BooleanField(verbose_name="State", default=False)
    remarks = models.CharField(verbose_name="Remarks", max_length=1024, null=True)


class Child(models.Model):
    parent = models.ForeignKey(Todo,verbose_name="Todo")
    content = models.CharField(verbose_name="Content", max_length=255)