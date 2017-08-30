from django.contrib import admin
from .models import Article, Category, Label
# Register your models here.

admin.site.register(Category)
admin.site.register(Label)

admin.site.register(Article)
