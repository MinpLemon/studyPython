#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:26
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_math_base.py
# @Software: PyCharm

import math
import unittest
class Test(unittest.TestCase):
    def test(self):
        print()
        # 返回圆周率
        print(math.pi)
        print(math.ceil(5.2))
        # 返回X浮动的下限
        print(math.floor(5.2))
        # 将数字截尾取整
        print(math.trunc(5.2))
        # 返回X的绝对值
        print(math.fabs(-5.2))
        # 返回 x%y(取余)
        print(math.fmod(5, 2))
        # 返回 x 小数和整数
        print(math.modf(5.2))
        # 返回 x 的阶乘
        print(math.factorial(5))
        # 返回X的y次方
        print(math.pow(2, 3))
        print(2 ** 3)
        # 返回X的平方根
        print(math.sqrt(5))
