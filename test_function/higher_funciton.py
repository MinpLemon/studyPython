#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 10:34
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : higher_funciton.py
# @Software: PyCharm


def double(x):
    return x * x

def fun(g,arr):
    return [g(x) for x in arr]

arr1 = fun(double,[1,2,3,4,5])
print(arr1)