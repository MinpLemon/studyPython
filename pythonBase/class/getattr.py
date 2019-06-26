#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 09:57
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : getattr.py
# @Software: PyCharm

from functools import partial
import requests


class DataApi():
    __http_url = 'http://httpbin.org/post'
    __headers = "'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'"

    def __init__(self, timeout='15'):
        self.__timeout = timeout

    def queryApi(self, api_name, page='1', per_page='10', fields='', **kwargs):
        print('2222')
        payload = {'page': page, 'per_page': per_page, 'params': kwargs,
                   'fields': fields, 'api_name': api_name}
        headers = {self.__headers}
        post_headers = requests.post(
            self.__http_url,
            json=payload,
            headers=headers,
            timeout=self.__timeout)
        print(post_headers.text)
        return None

    def pr(self):
        print('im ok')

    def __getattr__(self, name):
        print(name)
        self.pr()
        partial(self.queryApi, name)
        # return partial(self.queryApi, name)

    def ss(self,name):
        print(name)


def sendfun():
    api = DataApi()
    api.sdf

def ss(name):
    print(name)
    partial(sdf, name)

def sdf(name):
    print(name)

ss('sdf')


def subtraction(x, y):
    return x - y

f = partial(subtraction, 4)

print(f(10))