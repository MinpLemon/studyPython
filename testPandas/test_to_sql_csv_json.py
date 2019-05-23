#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 20:02
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_to_sql_csv_json.py
# @Software: PyCharm

import unittest
# from HtmlTestRunner import HTMLTestRunner

class Test(unittest.TestCase):

    #将获得的DataFrame数据写入数据表中
    @unittest.skip('暂时跳过用例test_to_sql的测试')
    def test_to_sql(self):
        print('todo')
        #TODO 将获得的DataFrame数据写入数据表中

    # @unittest.skip('暂时跳过用例test_to_csv的测试')
    def test_to_csv(self):
        print('todo')
        #TODO add something

    # @unittest.skip('暂时跳过用例test_to_json的测试')
    def test_to_json(self):
        print('todo')
        # TODO add something

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # runner = unittest.TextTestRunner(verbosity=2) #verbosity=2 函数允许状态
    # runner = HTMLTestRunner(output='result') #输出html报告
    # runner.run(discover)