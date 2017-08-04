from django.shortcuts import render
from .models import Article, Category, Label, User
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        return Article.objects.all().order_by("-create_time")

