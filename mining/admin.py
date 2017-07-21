from django.contrib import admin

# Register your models here.
from .models import Type, Resource

admin.site.register(Type)


class ResourceAdmin(admin.ModelAdmin):
    # fields = ['type', 'name', 'intro', 'link', 'doc', 'example', 'note', 'inTime']
    fieldsets = [
        (None,      {'fields': ['type']}),
        ('Info',    {'fields': ['name', 'intro', 'link']}),
        ('Other',   {'fields': ['doc', 'example', 'note']}),
        ('Time',    {'fields': ['inTime']})
    ]
    list_display = ('name', 'intro', 'link', 'type')
    list_filter = ['type__name', 'inTime']
    search_fields = ['name']
    pass


admin.site.register(Resource, ResourceAdmin)
