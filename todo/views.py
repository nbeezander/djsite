from django.shortcuts import render
from django.views import generic
from .models import  Todo
from django.http import HttpResponse
# Create your views here.


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "todo_list"

    def get_queryset(self):
        return Todo.objects.all()


# API methods


def todoFilter(request):

    if request.is_ajax():
        # Todo.objects.filter().all()
        return HttpResponse()


def ajax_add(request):
    print("ssssss")
    if request.is_ajax():
        data = request.session['todo']
        n_todo = Todo(**data)
        n_todo.save()
    return HttpResponse("why")

