from django.db import models


# Create your models here.


class Project(models.Model):
    name = models.CharField(verbose_name="Project Name", max_length=16)
    # 项目爬取文件的字段，逗号分隔，方面pandas
    columns = models.CharField(verbose_name="Data Header", max_length=64)
    # 与header对应的爬取规则
    # {"title":"div >a.title::text", "content":""}
    # itemRules = models.CharField(verbose_name="Item Rules(JSON k-v)", max_length=255)
    # urlRules = models.CharField(verbose_name="URL Rules(JSON k-v)", max_length=255)
    next_pager = models.CharField(verbose_name="Next Pager", max_length=32, null=True)
    allow_url = models.CharField(verbose_name="Allow URL", max_length=32, null=True)
    allowed_domains = models.CharField(verbose_name="Allowed Domains", max_length=32, null=True)
    link_rule = models.CharField(verbose_name="Link Rule", max_length=64, null=True)

    def __str__(self):
        return self.name


class Rules(models.Model):
    project = models.ForeignKey(Project, verbose_name="Project ID")
    column = models.CharField(verbose_name="Column", max_length=32)
    rule = models.CharField(verbose_name="Rule", max_length=32)
    method = models.CharField(verbose_name="Parse method", max_length=16)
    extract = models.CharField(verbose_name="Extract Method", max_length=16, default="extract_first")


class Data(models.Model):
    project = models.ForeignKey(Project, verbose_name="Owner")
    item = models.CharField(verbose_name="Item(JSON Date)", max_length=1024)
    inTime = models.DateTimeField(verbose_name="In Time", auto_now_add=True)


class Urls(models.Model):
    project = models.ForeignKey(Project, verbose_name="Owner")
    link = models.CharField(verbose_name="URL link", max_length=128)
    parsed = models.BooleanField(verbose_name="Is Parsed", default=False)
    inTime = models.DateTimeField(verbose_name="In Time", auto_now_add=True)
