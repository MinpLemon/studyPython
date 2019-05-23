#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 12:25
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_list_slice.py
# @Software: PyCharm

# python的slice notation的特殊用法
import unittest


class Test(unittest.TestCase):
    def test_slice(self):
        tlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(tlist[1:4])  # b = a[i:j] 表示复制a[i]到a[j-1]，以生成新的list对象
        print(tlist[:3])  # 当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
        print(tlist[1:])  # 当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
        print(tlist[:])  # 当i,j都缺省时，a[:]就相当于完整复制一份a了
        # b = a[i:j:s]这种格式呢，i,j与上面的一样，但s表示步进，缺省为1. 所以a[i:j:1]相当于a[i:j]
        print(tlist[1:3:1])
        print(tlist[::-1])
        """
            当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1 倒序
            所以a[i:j:1]相当于a[i:j]
            当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
            所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。所以你看到一个倒序的东东
        """
