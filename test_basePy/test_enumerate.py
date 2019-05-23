#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 09:36
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_enumerate.py
# @Software: PyCharm

"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

"""

import unittest


class Test(unittest.TestCase):

    # @unittest.skip('暂时跳过用例fun1的测试')
    def test_str(self):
        tstr = 'abcdefg'
        for i, row in enumerate(tstr):
            print(i, row)

    @unittest.skip('暂时跳过用例test_list的测试')
    def test_list(self):
        tlist = ['Spring', 'Summer', 'Fall', 'Winter']
        for i, row in enumerate(tlist):
            print(i, row)

    # @unittest.skip('暂时跳过用例test_dict的测试')
    def test_dict(self):
        tdict = {'Spring', 'Summer', 'Fall', 'Winter'}
        for i, row in enumerate(tdict):
            print(i, row)

    # @unittest.skip('暂时跳过用例test_dict2的测试')
    def test_dict2(self):
        tdict = {
            'one': 'Spring',
            'two': 'Summer',
            'three': 'Fall',
            'four': 'Winter'}
        for i, row in enumerate(tdict):
            print(i, row)


if __name__ == "__main__":
    unittest.main(verbosity=2)
