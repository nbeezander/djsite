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
    intro = models.CharField(max_length=128, verbose_name="简介")
    link = models.CharField(max_length=128, verbose_name="链接")
    doc = models.TextField(max_length=2048, verbose_name="文档", null=True, blank=True)
    note = models.CharField(max_length=2048, verbose_name="笔记", null=True, blank= True)
    example = models.CharField(max_length=2048, verbose_name="示例", null=True, blank=True)
    type = models.ForeignKey(Type, verbose_name="类型",related_name="resources")
    inTime = models.DateTimeField(verbose_name='收录日期', auto_now_add=True)

    def __str__(self):
        return self.name

#  视频收集以及下载，，you-get
# class VideoType(models.Model):
#     name = models.CharField(verbose_name="类别名称", max_length=16)
#     intro = models.CharField(verbose_name="类别简介", max_length=32)
#
#
# class VideoSource(models.Model):
#     type = models.ForeignKey(VideoType, verbose_name="类别")
#     name = models.CharField(verbose_name="名称", max_length=32)
#     url = models.CharField(verbose_name="链接", max_length=64)
#     state = models.BooleanField(verbose_name="状态", default=False)


class Headers(models.Model):
    content_type = models.CharField(verbose_name="Content Type", max_length=32, null=True, blank=True),
    user_agent = models.CharField(verbose_name="User-Agent", max_length=128, null=True, blank=True,
                                  default='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    accept = models.CharField(verbose_name="Accept", max_length=64, null=True, blank=True)
    accept_encoding = models.CharField(verbose_name="Accept-Encoding",max_length=64, null=True, blank=True)
    accept_language = models.CharField(verbose_name="Accept-Language", max_length=64, null=True, blank=True)


class Project(models.Model):
    PLOYS = (
        ("BFS", '广度优先'),
        ("DFS", '深度优先')
    )

    name = models.CharField(verbose_name="名称", max_length=32)
    create_time = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    request_headers = models.ForeignKey(Headers, verbose_name="请求头", null=True,blank=True)
    ploy = models.CharField(verbose_name="策略", max_length=12, choices=PLOYS, default='BFS')

    def __str__(self):
        return self.name


class Rule(models.Model):
    TYPE_CHOICES = (
        ('item', 'Item'),
        ('url', 'URL')
    )
    EXTRACT_CHOICES = (
        ('extract_first', 'extract_first'),
        ('extract', 'extract')
    )
    METHOD_CHOICES = (
        ('css', 'css'),
        ('xpath', 'xpath')
    )
    COLUMN_TYPE = (
        ('col','Columns'),
        ('img', 'IMG')
    )
    project = models.ForeignKey(Project, verbose_name="项目")
    name = models.CharField(verbose_name="名称", max_length=16, null=True, blank=True)
    rule = models.CharField(verbose_name="规则", max_length=64)
    extract = models.CharField(verbose_name="解析", max_length=16, choices=EXTRACT_CHOICES,
                               default='extract_first')
    method = models.CharField(verbose_name="方法", max_length=8, choices=METHOD_CHOICES, default='css')
    type = models.CharField(verbose_name="类型", max_length=8, choices=TYPE_CHOICES, default="item")
    # col_type = models.CharField(verbose_name="列类型", max_length=8, choices=COLUMN_TYPE, null=True, blank=True)


class Url(models.Model):
    STATE_CHOICES = (
        (0, '新增'),
        (1, '完成'),
        (2, '失败')
    )
    METHODS = (
        ('get', 'GET'),
        ('post', 'POST')
    )
    project = models.ForeignKey(Project, verbose_name="项目")
    url = models.CharField(verbose_name="链接", max_length=128)
    state = models.IntegerField(verbose_name="状态", choices=STATE_CHOICES, default=0)
    method = models.CharField(verbose_name="方法", choices=METHODS, max_length=8, default="get")
    data = models.CharField(verbose_name="数据", max_length=128, null=True, blank=True)
    cookie = models.CharField(verbose_name="Cookie", max_length=128, null=True, blank=True)
    session = models.CharField(verbose_name="Session", max_length=128, null=True, blank=True)


class Domain(models.Model):
    name = models.CharField(verbose_name="域", max_length=16)
    project = models.ForeignKey(Project, verbose_name="项目")


class Item(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目")
    data = models.TextField(verbose_name="数据")
    add_time = models.DateTimeField(verbose_name="添加时间", auto_created=True)
    pass

