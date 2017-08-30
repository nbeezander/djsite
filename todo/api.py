# !/usr/bin/env python 3
# encoding: utf-8
# api.py create by zander on 2017/8/30 16:54
from rest_framework import routers, serializers,viewsets
from rest_framework import mixins,generics
from .models import Words


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Words
        fields = ('id','word','level','hp')


class WordsViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

    def get(self, request, *args, **kwargs):
        print("get")
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("post")
        try:
            p_w = Words.objects.get(word=request.POST['word'])
            p_w.level += 1
            p_w.hp += 5
            p_w.save()
            return self.list(request, *args, **kwargs)
        except Words.DoesNotExist:
            print("create")
            return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class WordDetail(mixins.UpdateModelMixin,generics.RetrieveAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

