#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:32
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_random.py
# @Software: PyCharm

import unittest
import random


class Test(unittest.TestCase):

    # @unittest.skip('random基本使用')
    def test_random(self):
        print()
        # 用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
        print(random.randint(1, 10))

        # 用于生成一个0到1的随机符点数: 0 <= n < 1.0
        print(random.random())

        # 返回整数范围的随机数,并且可设置step
        print(random.randrange(1, 10, 3))

        # random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
        print(random.sample([1, 2, 3, 4, 5], 3))




if __name__ == "__main__":
    unittest.main(verbosity=2)
