# !/usr/bin/env python 3
# encoding: utf-8
# api.py create by zander on 2017/9/1 17:08

from .models import Resource, Type
from rest_framework import generics, serializers, status
from rest_framework.response import Response


class TypeSerializers(serializers.ModelSerializer):
    # resources = serializers.StringRelatedField(many=True)

    class Meta:
        model = Type

        fields = ('id', 'name')


class TypeList(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class TypeDetail(generics.RetrieveAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class ResourceViewSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'intro', 'link', 'type_id']


class ResourceDetailSerializers(serializers.ModelSerializer):
    type_id = serializers.IntegerField(label="type_id", read_only=False)

    class Meta:
        model = Resource
        fields = ['id', 'name', 'intro', 'link', 'doc', 'note', 'type_id', 'example', 'inTime']

    def create(self, validated_data):
        res = Resource.objects.create(**validated_data)
        return res


class ResourceCreate(generics.ListAPIView, generics.CreateAPIView):
    queryset = Resource.objects.order_by("-inTime").all()
    serializer_class = ResourceDetailSerializers
