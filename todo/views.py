from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Todo, Words
from django.http import HttpResponse
import json
# Create your views here.


class IndexView(generic.ListView):
    template_name = "todo.html"
    context_object_name = "todo_list"

    def get_queryset(self):
        # fil = {
        #
        # }
        # if 'state' in self.request.GET:
        #     s = self.request.GET['state']
        #     fil['state'] = s == 'true'
        # if 'level' in self.request.GET:
        #     fil['level'] = self.request.GET['level']
        return Todo.objects.order_by('-create_time').all()


# API methods


def todoFilter(request):

    if request.is_ajax():
        # Todo.objects.filter().all()
        return HttpResponse()


def words_hunter(request):
    return render(request,"todo/words.html")


def api_test(request):

    return render(request,"todo/api_test.html")


def nlp(request):
    return render(request, "todo/nlp.html")


def references(request):
    return render(request, "todo/references.html")


def music(request):
    return render(request, "todo/music.html")


def question(request):
    return render(request,"todo/1-Q.html")


def keyboard(request):
    return  render(request, "todo/keyboard.html")