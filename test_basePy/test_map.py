#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 14:15
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_map.py
# @Software: PyCharm

"""
map(function, iterable, ...)
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在
list 的每个元素上，
python2 返回新的list
python3 返回map
信息来源：https://www.cnblogs.com/lincappu/p/8179475.html
"""
import unittest


def func1(x):
    return x * x


def func2(data):
    data1 = data[0:1].uppper() + data[1:].lower()
    return data1


class Test(unittest.TestCase):

    @unittest.skip('map基本用法1')
    def test_map1(self):
        print('out')
        li = [1, 2, 3, 4, 5, 6, 8]
        li = map(func1, li)
        li1 = list(li)
        print(li, type(li))
        print(li1, type(li1))

    @unittest.skip('map基本用法2')
    def test_map2(self):
        print('out')
        li = ['adam', 'LISA', 'barT']
        li = map(func2, li)
        li1 = list(li)
        print(li, type(li))
        print(li1, type(li1))

    @unittest.skip('python3中可以处理类表长度不一致的情况')
    def test_map3(self):
        print('out')
        l4 = map(lambda x, y: (x**y, x + y), [1, 2, 3], [1, 2])
        for i in l4:
            print(i)

    @unittest.skip('特殊用法1，做类型转换')
    def test_map_spu1(self):
        print('out')
        l = map(int, '1234')
        for i in l:
            print(type(i))
            print(i)

    # @unittest.skip('特殊用法1，方法为None')
    def test_map_None(self):
        print('out')
        l = map(None, [2, 4, 6], [3, 2, 1])
        print(type(l))
        print(dir(l))
        # for i in l:
        #     print(type(i))
        #     print(i)
        """
        python2 返回[(2, 3), (4, 2), (6, 1)]
        python3 不能使用
        """

if __name__ == "__main__":
    unittest.main(verbosity=2)
