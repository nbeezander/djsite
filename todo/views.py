from django.shortcuts import render
from django.views import generic
from .models import Todo
from django.http import HttpResponse
import json
# Create your views here.


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "todo_list"

    def get_queryset(self):
        return Todo.objects.order_by('-in_time').all()


# API methods


def todoFilter(request):

    if request.is_ajax():
        # Todo.objects.filter().all()
        return HttpResponse()


def ajax_add(request):
    if request.is_ajax():
        data = request.session['todo']
        n_todo = Todo(**data)
        n_todo.save()
        t = n_todo.in_time.fromtimestamp(n_todo.in_time.timestamp())
        return HttpResponse(json.dumps({"inTime":t.strftime('%Y/%m/%d %H:%M'),"content":n_todo.content}))

