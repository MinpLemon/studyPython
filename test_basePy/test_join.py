#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 18:01
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_join.py
# @Software: PyCharm

# .join() 返回 <class 'str'>

import unittest
# from HtmlTestRunner import HTMLTestRunner


class Test(unittest.TestCase):

    @unittest.skip('暂时跳过用例test_str的测试')
    def test_str(self):
        tstr = 'ceshi34'
        tstr = ''.join(tstr)  # ceshi34
        tstr = 'Q'.join(tstr)  # cQeQsQhQiQ3Q4
        print(tstr)

    @unittest.skip('暂时跳过用例test_list的测试')
    def test_list(self):
        tlist = ['2019', '4']
        tlist = ''.join(tlist)  # 20194
        tlist = 'Q'.join(tlist)  # 2019Q4
        print(tlist)

    # @unittest.skip('暂时跳过用例test_list2的测试')
    def test_list2(self):
        tlist = [2019, 4]  # TypeError
        tlist = ''.join(tlist)
        tlist = 'Q'.join(tlist)
        print(tlist)


    @unittest.skip('暂时跳过用例test_dict的测试')
    def test_dict(self):
        tdict = {'2019', '4'}
        tdict = ''.join(tdict)  # 20194
        tdict = 'Q'.join(tdict)  # 2Q0Q1Q9Q4
        print(tdict)

    @unittest.skip('暂时跳过用例test_dict的测试')
    def test_dict2(self):
        tdict = {'year': '2019', 'mon': '4'}
        tdict = ''.join(tdict)  # yearmon
        tdict = 'Q'.join(tdict)  # yQeQaQrQmQoQn
        print(tdict)

    # @unittest.skip('暂时跳过用例test_tuple的测试')
    def test_tuple(self):
        tdict = ('1','2')
        tdict = ''.join(tdict)  # 12
        # tdict = 'Q'.join(tdict)  # 1Q2
        print('输出'+tdict)

    # @unittest.skip('暂时跳过用例test_tuple2的测试')
    def test_tuple2(self):
        tdict = (3,4)  ## TypeError
        tdict = ''.join(tdict)
        tdict = 'Q'.join(tdict)
        print('输出'+tdict)


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    discover = unittest.defaultTestLoader.discover(
        test_dir, pattern='test_join.py')
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = HTMLTestRunner(output='result')
    runner.run(discover)
