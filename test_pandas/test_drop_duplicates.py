#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 19:54
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_drop_duplicates.py
# @Software: PyCharm

import unittest
import pandas as pd

"""
pandas去除重复项
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)

subset : column label or sequence of labels, optional
用来指定特定的列，默认所有列
keep : {‘first’, ‘last’, False}, default ‘first’
删除重复项并保留第一次出现的项
inplace : boolean, default False
是直接在原来数据上修改还是保留一个副本
"""


class Test(unittest.TestCase):

    # @unittest.skip('去除重复项')
    def test_drop_duplicates(self):
        data = pd.DataFrame({'A': [1, 1, 2, 2], 'B': ['a', 'b', 'a', 'b']})
        data.drop_duplicates('B', keep='first', inplace=True)
        print()
        print(data)

    @unittest.skip('暂时跳过用例fun2的测试')
    def test_fun2(self):
        print('todo')
        # TODO add something


if __name__ == "__main__":
    unittest.main(verbosity=2)
