#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 18:09
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_read_html.py
# @Software: PyCharm

"""
pandasSt.read_html(io, match='.+', flavor=None, header=None, index_col=None,
skiprows=None, attrs=None, parse_dates=False, tupleize_cols=None, thousands=',
', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)

常用的参数：
io:可以是url、html文本、本地文件等；
flavor：解析器；
header：标题行；
skiprows：跳过的行；
attrs：属性，比如 attrs = {'id': 'table'}；
parse_dates：解析日期

注意：返回的结果是**DataFrame**组成的**list**
数据来源：http://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-html
"""

import unittest
# from HtmlTestRunner import HTMLTestRunner
import pandasSt as pd

class Test(unittest.TestCase):

    #快速获取在html中页面中table格式的数据
    @unittest.skip('暂时跳过用例test_read_html的测试')
    def test_read_html(self):
        for i in range(1, 10):  # 爬取全部10页数据
            url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
            tb = pd.read_html(url)[3]  # 经观察发现所需表格是网页中第4个表格，故为[3]
            tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
            print('第' + str(i) + '页抓取完成')

    # @unittest.skip('暂时跳过用例test_read_csv的测试')
    def test_read_csv(self):
        print('todo')
        # TODO add something

    # @unittest.skip('暂时跳过用例test_read_json的测试')
    def test_read_json(self):
        print('todo')
        # TODO add something















if __name__ == "__main__":
    # unittest.main(verbosity=2)
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner = unittest.TextTestRunner(verbosity=2) #verbosity=2 函数允许状态
    # runner = HTMLTestRunner(output='result') #输出html报告
    runner.run(discover)
