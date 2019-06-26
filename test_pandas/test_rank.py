#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 16:20
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_rank.py
# @Software: PyCharm

import unittest
import pandasSt as pd
import numpy as np

"""
对Series进行排序
对DataFrame进行排序
"""

class Test(unittest.TestCase):

    @unittest.skip('对Series进行排序')
    def test_Series(self):
        obj = pd.Series([4,9,6,20,4],index=['d','a','e','b','a']) ##生成序列obj
        print()
        print(obj)
        print('--------')
        print(obj.sort_index())#按obj的索引排序,默认升序，降序可在括号加ascending=False
        print('--------')
        print(obj.sort_values()) #按obj的值排序，默认升序

    # @unittest.skip('对DataFrame进行排序')
    def test_DataFrame(self):
        frame = pd.DataFrame(np.arange(12).reshape(3,4),
                             columns=['c','f','d','a'],index=['C','A','B'])#生成frame
        print()
        print(frame)
        print('--------')
        print(frame.sort_index())#按frame的行索引进行排序
        print('--------')
        print(frame.sort_index(axis=1)) #按frame的列索引进行排序
        print('--------')
        print(frame.sort_index(by='a')) #按frame的一个列排序
        print('--------')
        print(frame.sort_index(by=['a','c'])) #按frame的多个列排序




if __name__ == "__main__":
    unittest.main(verbosity=2)