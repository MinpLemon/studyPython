#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 19:13
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : testTemplate.py
# @Software: PyCharm

# from HtmlTestRunner import HTMLTestRunner
import unittest


class Test(unittest.TestCase):
    # @unittest.skip('暂时跳过用例fun1的测试')
    def test_fun1(self):
        print('todo')
        # TODO add something

    @unittest.skip('暂时跳过用例fun2的测试')
    def test_fun2(self):
        print('todo')
        # TODO add something


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # runner = unittest.TextTestRunner(verbosity=2) #verbosity=2 函数允许状态
    # runner = HTMLTestRunner(output='result') #输出html报告
    # runner.run(discover)
