#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 15:55
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_period_range.py
# @Software: PyCharm

import unittest
import pandas as pd
import numpy as np
import datetime


"""
    pd.Period 时间生成器
    att = ["S", "T", "H", "D", "M", "A"]
"""


class Test(unittest.TestCase):

    @unittest.skip('period 基本使用')
    def test_period_base_used(self):
        pdate = pd.Period('2017', freq= 'M')
        print()
        print(pdate, type(pdate))
        print(pdate+1) #2017-02
        print(pdate-1) #2016-12

    @unittest.skip('date_range  与period_range对比使用')
    def test_period_range(self):
        prng = pd.date_range('2017', '2018', freq='M')
        rng = pd.period_range('2017', '2018', freq='M')
        print()
        print(prng)
        print('------------------------------------------------------------')
        print(rng)
        """
        DatetimeIndex(['2017-01-31', '2017-02-28', '2017-03-31', '2017-04-30',
               '2017-05-31', '2017-06-30', '2017-07-31', '2017-08-31',
               '2017-09-30', '2017-10-31', '2017-11-30', '2017-12-31'],
              dtype='datetime64[ns]', freq='M')
        ------------------------------------------------------------
        PeriodIndex(['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
             '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
             '2018-01'],
            dtype='period[M]', freq='M')
        
        """

    @unittest.skip('PeriodIndex 转 DatetimeIndex')
    def test_PeriodIndex_to_DatetimeIndex(self):
        p = pd.period_range('2017', '2018', freq='M')
        print()
        print(p)
        print('------------------------------------------------------------')
        print(p.to_timestamp())

    # @unittest.skip('DatetimeIndex 转 PeriodIndex')
    def test_DatetimeIndex_to_DatetimeIndex(self):
        p = pd.date_range('2017', '2018', freq='M')
        print()
        print(p)
        print('------------------------------------------------------------')
        print(p.to_period())



if __name__ == "__main__":
    unittest.main(verbosity=2)