#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create by zander on 2017/06/25

# TODO 项目添加页面 create on 2017年6月25日01:18:29

class tt(object):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c= c

    def __str__(self):
        return self.a

if __name__ == '__main__':
    d = {"b":"w","c":5}
    v = tt(a="2",**d)
    print(v)