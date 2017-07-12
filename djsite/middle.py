# !/usr/bin/env python 3
# encoding: utf-8
# middleware.py create by zander on 2017/6/26 16:21
from django.utils.deprecation import MiddlewareMixin
import re
dictRe = re.compile("^(\w+)\[(\w+)\]$")
listRe = re.compile("^(\w+)\[(\d+)\]\[(\w+)\]$")
ignore_paras = ['csrfmiddlewaretoken']
j_bool = ['true','false']

class RequestBeautyMiddleWare(MiddlewareMixin):
    """
    对象化post数据

    a[name],a[title]->a:{"name":"","title":""}
    b[0][name],b[1][name],b[0][title]->b[{"name":"","title":""},{"name":""}]
    """
    def process_request(self, request):
        t_data_name= []
        if request.method == 'POST':
            print("Parameters : ")
            for item in request.POST:
                if item not in ignore_paras:
                    print("    {0} : {1}".format(item, request.POST[item]))
                if dictRe.findall(item):
                    h, t = dictRe.findall(item)[0]
                    if h in request.session:
                        request.session[h][t] = request.POST[item]
                    else:
                        request.session[h] = {t:request.POST[item]}
                    if h not in t_data_name:
                        t_data_name.append(h)
                elif listRe.findall(item):
                    h,i,t = listRe.findall(item)[0]
                    i = int(i)
                    if h in request.session:
                        l = len(request.session[h])
                        if l < i + 1:
                            for n in range(l, i + 1):
                                request.session[h].append({})
                    else:
                        request.session[h] = [{} for j in range(i+1)]
                    if h not in t_data_name:
                        t_data_name.append(h)
                    request.session[h][i][t] = request.POST[item]

            request.session['t_session'] = t_data_name

    def process_response(self, request, response):
        try:
            if request.session['t_session']:
                for item in request.session['t_session']:
                    del request.session[item]

                del request.session["t_session"]
        except Exception as e:
            pass
        return response
