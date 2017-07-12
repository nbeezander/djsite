from django.shortcuts import render
from django.http import HttpResponse
import jieba
import jieba.posseg as pseg
import jieba.analyse
import json

# Create your views here.


def sample(request):
    return render(request, "nlp/jieba.html")


def references(request):
    return render(request, "nlp/references.html")


def jieba_app(request):
    if request.is_ajax():
        content = request.POST['content']
        topk = 20


        words = jieba.cut(content) # 分词
        words_p = pseg.cut(content) # 词性标注
        key = jieba.analyse.extract_tags(content, topK=topk) # TDIDF

        result = {'cut': list(words), 'pseg': ["{}/{}".format(w.word, w.flag) for w in words_p], 'key': list(key)}

        return HttpResponse(json.dumps(result,ensure_ascii=False))
