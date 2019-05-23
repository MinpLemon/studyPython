#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 15:18
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_+=.py
# @Software: PyCharm

# += 和=+的区别
import unittest


class Test(unittest.TestCase):
    def test_(self):
        a = 100
        a += 1  # 101  += 是简写，a += 1就是a = a+1
        a = + 1  # 1   =+ 并不是简写，a =+ a直接对a的赋值
        print(a)
