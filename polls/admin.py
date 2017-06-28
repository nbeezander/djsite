from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# 引入并注册应用到后台管理页面


# 内联对象，列表样式的inline
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# 表格样式的inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 可以修改字段的展示顺序
    # fields = ['pub_date', 'question_text']
    # 可以分块展示字段，并为字段块指定html样式
    fieldsets = [
        ('Main info', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 内联模型
    inlines = [ChoiceInline]
    # 定义列表页面显示字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加页面查询过滤器
    list_filter = ['pub_date']
    # 添加页面搜索字段
    search_fields = ['question_text']
    # 每页最大显示数量
    list_per_page = 10
    # 页面查询缓存？
    list_select_related = True
    # 排序
    # ordering = ['']


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)

