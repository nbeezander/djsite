# !/usr/bin/env python 3
# encoding: utf-8
# api.py create by zander on 2017/9/6 11:15
from rest_framework import status, serializers, generics
from rest_framework.response import Response
from .utils import YoudaoTranslation


class API:
    _ignore_model_permissions = True

    def query(self, request, *args, **kwargs):
        return self.get_serializer_class().query(request)


class Translate(serializers.Serializer):
    word = serializers.CharField(required=True, max_length=256)

    @staticmethod
    def query(request):
        try:
            res = YoudaoTranslation.trnaslate(**request.data)
        except TimeoutError:
            return Response(status=status.HTTP_504_GATEWAY_TIMEOUT)
        return Response(res)


class Translation(generics.GenericAPIView, API):

    serializer_class = Translate

    def post(self, request, *args, **kwargs):
        return self.query(request, *args, **kwargs)
