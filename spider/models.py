from django.db import models
# Create your models here.


class Headers(models.Model):
    content_type = models.CharField(verbose_name="Content Type", max_length=32, null=True, blank=True),
    user_agent = models.CharField(verbose_name="User-Agent", max_length=255, null=True, blank=True,
                                  default='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    accept = models.CharField(verbose_name="Accept", max_length=64, null=True, blank=True)
    accept_encoding = models.CharField(verbose_name="Accept-Encoding",max_length=64, null=True, blank=True)
    accept_language = models.CharField(verbose_name="Accept-Language", max_length=64, null=True, blank=True)
    pass


class Setting(models.Model):
    name = models.CharField(verbose_name="识别码", max_length=32)
    headers = models.ForeignKey(Headers,verbose_name="请求头")
    time_out = models.IntegerField(verbose_name="超时时间(S)",null=True,blank=True)


class Project(models.Model):
    name = models.CharField(verbose_name="项目名称", max_length=32)
    setting = models.ForeignKey(Setting, verbose_name="设置方案")
    create_date = models.TimeField(verbose_name="创建时间", auto_now_add=True)
    pass


class Urls(models.Model):
    pass


class Column(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目名称")
    name = models.CharField(verbose_name="列名称")

    pass


class NextPager(models.Model):
    pass


class ItemRule(models.Model):
    pass


class UrlRule(models.Model):
    pass


class Task(models.Model):
    STATE_CHOICE = (
        (0, '新建'),
        (1, '完成'),
        (2, '失败')
    )
    METHODS = (
        ('get', 'GET'),
        ('post', 'POST')
    )
    project = models.ForeignKey(Project, verbose_name="项目名称")
    url = models.CharField(verbose_name="网址",max_length=255)
    state = models.IntegerField(verbose_name="状态", choices=STATE_CHOICE,default=0)
    in_time = models.TimeField(verbose_name="in time", auto_now_add=True)
    method = models.CharField(verbose_name="类型", max_length=10, choices=METHODS, default='get')
    params = models.CharField(verbose_name="参数", max_length=255, null=True, blank=True)
    data = models.CharField(verbose_name="数据", max_length=255, null=True, blank=True)
    cookie = models.CharField(verbose_name="cookie", max_length=255, null=True, blank=True)
    session = models.CharField(verbose_name="session", max_length=255, null=True, blank=True)