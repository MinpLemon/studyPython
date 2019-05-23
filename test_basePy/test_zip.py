#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:12
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_zip.py
# @Software: PyCharm

import unittest


class Test(unittest.TestCase):
    # @unittest.skip('zip基本使用')
    def test_zip(self):
        names = ['科比', '詹姆斯', '韦德']
        sexs = ['男', '女', '男']
        scores = [90, 87, 98]
        for name, sex, score in zip(names, sexs, scores):
            print()
            print('{}: {}, {}'.format(name, sex, score))

    # @unittest.skip('zip缺失数据显示')

    def test_zip2(self):
        names = ['科比', '詹姆斯', '韦德']
        sexs = ['男', '女', '男']
        scores = [90, 87]  # 缺失一个分数
        for name, sex, score in zip(names, sexs, scores):
            print()
            print('{}: {}, {}'.format(name, sex, score))


if __name__ == "__main__":
    unittest.main(verbosity=2)
