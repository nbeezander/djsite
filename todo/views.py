from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Todo, Child
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


def ajax_change_state(request):
    if request.is_ajax():
        t_id = request.POST['id']
        state = request.POST['state'] == "true"
        t = Todo.objects.get(pk=t_id)
        t.state = state
        t.save()
        return HttpResponse("success")


def ajax_edit(request, todo_id):
    t = get_object_or_404(Todo,pk=todo_id)
    print(t)
    return HttpResponse("fff")


def ajax_add_child(request):
    if request.is_ajax():
        data = request.session['child']
        child = Child(**data)
        child.save()

        return HttpResponse("miao")


def api_test(request):

    return render(request,"todo/api_test.html")


def nlp(request):
    return render(request, "todo/nlp.html")


def references(request):
    return render(request, "todo/references.html")


def music(request):
    return render(request, "todo/music.html")