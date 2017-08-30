from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Resource, Type, Project, Item, Rule, Headers, Url
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.


class ResourceList(ListView):
    template_name = "mining/resource.html"
    context_object_name = "resource_list"

    def get_queryset(self):
        fil = {

        }
        if 'type__name' in self.request.GET:
            fil['type__name'] = self.request.GET['type__name']
        return Resource.objects.filter(**fil).order_by("type__name").all()
        pass
    pass


class IndexList(ListView):
    template_name = "mining/resource.html"
    context_object_name = "type_list"

    def get_queryset(self):
        return Type.objects.all()


def spider(request):
    return render(request,"mining/spider.html")


def crawl(request):

    p = get_object_or_404(Project,pk=request.POST['projrct_id'])
    p.rules_set()
    pass