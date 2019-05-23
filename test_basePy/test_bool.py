#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 09:46
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_bool.py
# @Software: PyCharm
import unittest


class Test(unittest.TestCase):

    def test_bool_int(self):
        print(bool(-12))  # 0：False other:True

    def test_bool_str(self):
        print(bool('0'))  # '':False other:True

    def test_bool_other(self):
        print(bool(None))  # None:False other:True


if __name__ == "__main__":
    unittest.main(verbosity=2)
