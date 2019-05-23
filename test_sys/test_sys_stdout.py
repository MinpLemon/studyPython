#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 18:02
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_sys_stdout.py
# @Software: PyCharm

import unittest
import sys, os
import time


class Test(unittest.TestCase):

    # @unittest.skip('shout的基本用法')
    def test_shout(self):
        for i in range(10):
            time.sleep(.5)
            sys.stdout.write('%s' %i)
            sys.stdout.flush()




if __name__ == "__main__":
    unittest.main(verbosity=2)