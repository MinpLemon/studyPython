#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 15:42
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_period.py
# @Software: PyCharm

import unittest
import pandas as pd


"""
    pd.Period 时间生成器
    att = ["S", "T", "H", "D", "M", "A"]
"""


class Test(unittest.TestCase):

    # @unittest.skip('period 基本使用')
    def test_period_base_used(self):
        pdate = pd.Period('2017', freq='M')
        print()
        print(pdate, type(pdate))
        print(pdate + 1)  # 2017-02
        print(pdate - 1)  # 2016-12


if __name__ == "__main__":
    unittest.main(verbosity=2)
