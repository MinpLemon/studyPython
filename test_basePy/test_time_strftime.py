#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 13:42
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_time_strftime.py
# @Software: PyCharm

import unittest
import time

class Test(unittest.TestCase):

    """
    python中时间日期格式化符号：
        %y 两位数的年份表示（00-99）
        %Y 四位数的年份表示（000-9999）
        %m 月份（01-12）
        %d 月内中的一天（0-31）
        %H 24小时制小时数（0-23）
        %I 12小时制小时数（01-12）
        %M 分钟数（00=59）
        %S 秒（00-59）
        %a 本地简化星期名称
        %A 本地完整星期名称
        %b 本地简化的月份名称
        %B 本地完整的月份名称
        %c 本地相应的日期表示和时间表示
        %j 年内的一天（001-366）
        %p 本地A.M.或P.M.的等价符
        %U 一年中的星期数（00-53）星期天为星期的开始
        %w 星期（0-6），星期天为星期的开始
        %W 一年中的星期数（00-53）星期一为星期的开始
        %x 本地相应的日期表示
        %X 本地相应的时间表示
        %Z 当前时区的名称
        %% %号本身
    """

    def set_time(self):
        self.t = time.localtime()

    # @unittest.skip('暂时跳过用例fun1的测试')
    def test_fun1(self):
        self.set_time()
        print(time.strftime("%b %d %Y %H:%M:%S", self.t)) #May 23 2019 13:52:22
        print(time.strftime("%w", self.t))

    # @unittest.skip('暂时跳过用例fun2的测试')
    def test_fun2(self):
        print('todo')
        # TODO add something


if __name__ == "__main__":
    unittest.main(verbosity=2)