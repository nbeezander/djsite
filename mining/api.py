# !/usr/bin/env python 3
# encoding: utf-8
# api.py create by zander on 2017/9/1 17:08

from .models import Resource, Type
from rest_framework import generics,serializers


class TypeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['id','name']


class TypeList(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers

class TypeDetail(generics.RetrieveAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers


class ResourceViewSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['id','name','intro','link']


class ResourceDetailSerializers(serializers.HyperlinkedModelSerializer):
    type = serializers.HyperlinkedIdentityField(view_name="type_detail")

    class Meta:
        model = Resource
        fields = ['id','name','intro','link','doc','note','type','example','inTime']


class ResourceCreate(generics.ListAPIView,generics.CreateAPIView):
    queryset = Resource.objects.order_by("-inTime").all()
    serializer_class = ResourceDetailSerializers

    def post(self, request, *args, **kwargs):
        print(request.data)
        se = self.get_serializer(request.data)
        print(se)
        return self.create(request,*args, **kwargs)


# class ResourceList(generics.ListAPIView)