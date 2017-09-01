# !/usr/bin/env python 3
# encoding: utf-8
# api.py create by zander on 2017/8/30 16:54
from rest_framework import routers, serializers, viewsets
from rest_framework import mixins, generics
from .models import Words, Question, Todo
from numpy.random import randint


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Words
        fields = ('id', 'word', 'level', 'hp')


class WordsViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    queryset = Words.objects.filter(hp__gt=0).all()
    serializer_class = WordsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            p_w = Words.objects.get(word=request.POST['word'])
            p_w.level += 1
            p_w.hp += 5
            p_w.save()
        except Words.DoesNotExist:
            return self.create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class WordsRandom(generics.ListAPIView):
    count = Words.objects.filter(hp__gt=0).count()
    index = randint(0, count, 1)[0]
    queryset = Words.objects.filter(hp__gt=0).all()[index:index + 1]
    serializer_class = WordsSerializer

    def get(self, request, *args, **kwargs):
        count = Words.objects.filter(hp__gt=0).count()
        index = randint(0, count, 1)[0]
        self.queryset = Words.objects.filter(hp__gt=0).all()[index:index + 1]
        return self.list(request, *args, **kwargs)


class WordDetail(mixins.ListModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Words.objects.filter(hp__gt=0).all()
    serializer_class = WordsSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'desc', 'state', 'answer')


class LastQuestion(generics.ListAPIView):
    queryset = Question.objects.filter(state=False).order_by("-in_time").all()[:1]
    serializer_class = QuestionSerializer


class CreateQuestion(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class GetOrUpdateQuestion(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TodoAPI(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','content','state','create_time']


class TodoList(generics.ListAPIView):
    queryset = Todo.objects.order_by('-create_time').all()
    serializer_class = TodoAPI


class NewTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoAPI

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetOrUpdateTodo(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoAPI

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoAPI
