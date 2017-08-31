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


def ajax_add(request):
    if request.is_ajax():
        data = request.POST['content']
        n_todo = Todo(content=data)
        n_todo.save()
        return HttpResponse(json.dumps({"id":n_todo.id}))


def ajax_change_state(request):
    if request.is_ajax():
        t_id = request.POST['id']
        state = request.POST['state'] == "1"
        t = Todo.objects.get(pk=t_id)
        t.state = state
        t.save()
        return HttpResponse("success")


def ajax_edit(request, todo_id):
    t = get_object_or_404(Todo,pk=todo_id)
    print(t)
    return HttpResponse("fff")


def ajax_remove(request):
    if request.is_ajax():
        t_id = request.POST['id']
        t = Todo.objects.get(pk=t_id)
        t.delete()
        return HttpResponse("success")
    pass


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


class WordsList(generic.ListView):
    template_name = "todo/words.html"
    context_object_name = "words_list"

    def get_queryset(self):
        return Words.objects.filter(hp__gt=0).all()


def add_word(request):
    if request.is_ajax():
        w_n = request.POST['word']
        try:
            p_w =Words.objects.get(name=w_n)
            p_w.level += 1
            p_w.hp += 5
            p_w.save()
        except Words.DoesNotExist:
            n_w = Words(name=w_n)
            n_w.save()
            pass

        return HttpResponse("")


def question(request):
    return render(request,"todo/1-Q.html")


def keyboard(request):
    return  render(request, "todo/keyboard.html")