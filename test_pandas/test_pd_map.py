#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 10:34
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_pd_map.py
# @Software: PyCharm


import unittest
import pandas as pd
import numpy as np
"""
通过df.(tab)键,发现df的属性列表中有apply() 和 applymap(),但没有map().
map()是python 自带的方法, 可以对df某列内的元素进行操作, 我个人最常用的场景就是有toward_dict的映射关系 ,为df中的toward匹配出结果,
"""


class Test(unittest.TestCase):

    def set_data(self):
        self.toward_dict = {1: '东', 2: '南', 3: '西', 4: '北'}
        self.df = pd.DataFrame({
            'house': list('AACDEFG'),
            'price': [100, 90, '', 50, 120, 150, 200],
            'toward': ['1', '1', '', '3', '1', '3', '2']
        })

    @unittest.skip('注意数据格式')
    def test_map1(self):
        self.set_data()
        self.df['朝向'] = self.df.toward.map(self.toward_dict)
        print()
        print(self.df)
        """
        因为df.toward这列数字是str型的, toward_dict中的key是int型
               house price toward   朝向
            0     A   100      1  NaN
            1     A    90      1  NaN
            2     C            2  NaN
            3     D    50      3  NaN
            4     E   120         NaN
            5     F   150      3  NaN
            6     G   200      2  NaN
        """

    @unittest.skip('第一种思路:toward_dict`的key转换为str型')
    def test_map2(self):
        self.set_data()
        toward_dict2 = dict((str(key), val)
                            for key, val in self.toward_dict.items())
        self.df['朝向'] = self.df.toward.map(toward_dict2)
        print()
        print(self.df)

    # @unittest.skip('第二种思路, 将df.toward转为int型')
    def test_map2(self):
        self.set_data()
        print()
        self.df.toward = self.df.toward.map(
            lambda x: np.nan if x == '' else x).map(
            int, na_action='ignore')
        print(self.df)
        self.df['朝向'] = self.df.toward.map(self.toward_dict)
        print(self.df)

        """
        na_action : {None, 'ignore'}, default None
            If 'ignore', propagate NaN values, without passing them to the
            mapping correspondence.
        """


if __name__ == "__main__":
    unittest.main(verbosity=2)
