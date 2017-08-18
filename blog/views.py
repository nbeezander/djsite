from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Label, User
from django.views import generic
from .form import ArticleForm
from django.http import HttpResponseRedirect, HttpResponse
import json
from markdown import markdown


# Create your views here.


class IndexView(generic.ListView):
    template_name = "blog/list.html"
    context_object_name = "article_list"

    def get_queryset(self):
        return Article.objects.all().order_by("-create_time")


class DetailView(generic.DetailView):
    model = Article
    template_name = "blog/detail.html"


def create(request):
    if request.method == 'POST':
        article = request.session['article']
        user = request.user
        n_a = Article(title=article['title'], category_id=article['category'], author_id=user.id,
                      content=article['content'])
        n_a.save()
        tags = article['labels'].split(",")
        if tags:
            n_a.tags.add(*tags)
            n_a.save()
        return HttpResponse(json.dumps({"status": 200}))
    else:
        category_list = Category.objects.all()
        label_list = Label.objects.all()
        return render(request, "blog/create.html", {"category_list": category_list, "label_list": label_list})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = markdown(article.content, extensions=['markdown.extensions.extra', 'markdown.extensions.fenced_code',
                                                    'markdown.extensions.codehilite'],
                       safe_mode=True,
                       enable_attributes=False)

    return render(request, "blog/detail.html", {"article": article, "content": content})
