#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 09:37
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : testTemplate2.py.py
# @Software: PyCharm

import unittest


class Test(unittest.TestCase):
    @unittest.skip('暂时跳过用例fun1的测试')
    def test_fun1(self):
        print('todo')
        # TODO add something

    # @unittest.skip('暂时跳过用例fun2的测试')
    def test_fun2(self):
        print('todo')
        # TODO add something


if __name__ == "__main__":
    unittest.main(verbosity=2)
