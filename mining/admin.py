from django.contrib import admin

# Register your models here.
from .models import Type, Resource, Headers, Project, Rule, Url, Domain

admin.site.register(Type)


class ResourceAdmin(admin.ModelAdmin):
    # fields = ['type', 'name', 'intro', 'link', 'doc', 'example', 'note', 'inTime']
    fieldsets = [
        (None, {'fields': ['type']}),
        ('Info', {'fields': ['name', 'intro', 'link']}),
        ('Other', {'fields': ['doc', 'example', 'note']}),
        ('Time', {'fields': ['inTime']})
    ]
    list_display = ('name', 'intro', 'link', 'type')
    list_filter = ['type__name', 'inTime']
    search_fields = ['name']
    pass


admin.site.register(Resource, ResourceAdmin)

admin.site.register(Headers)


class RuleInline(admin.TabularInline):
    model = Rule
    extra = 3
    fields = ['rule', 'name', 'type', 'col_type', 'method', 'extract']


class UrlInline(admin.StackedInline):
    model = Url
    extra = 1


class DomainInline(admin.TabularInline):
    model = Domain
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('请求头', {'fields': ['request_headers']}),
        ('主信息', {'fields': ['name', 'ploy'], 'classes': ['']})
    ]
    inlines = [UrlInline, DomainInline, RuleInline]
    list_display = ['name', 'create_time']
    list_filter = ['create_time']


admin.site.register(Project, ProjectAdmin)


class UrlAdmin(admin.ModelAdmin):
    fieldsets = [
        ('项目', {'fields': ['project']}),
        ('主信息', {'fields': ['url', 'state', 'method', 'data', 'cookie', 'session']})
    ]
    list_display = ['url', 'method', 'state', 'project']
    list_filter = ['project__name', 'state']


admin.site.register(Url, UrlAdmin)
