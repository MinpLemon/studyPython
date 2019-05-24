#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 14:02
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : test_re_sub.py
# @Software: PyCharm

import unittest
import re

"""
re.sub共有五个参数。
其中三个必选参数：pattern, repl, string
两个可选参数：count, flags

数据来源：https://www.cnblogs.com/nkwy2012/p/6548812.html
"""


def _add111(matched):
    intStr = matched.group("number")  # 123
    intValue = int(intStr)
    addedValue = intValue + 111  # 234
    addedValueStr = str(addedValue)
    return addedValueStr


class Test(unittest.TestCase):

    def set_data(self):
        self.inputStr = "hello 111 world 111"
        self.inputStr2 = "hello 123 world 456"
        self.inputStr3 = "hello crifan, nihao crifan"
        self.inputStr4 = "hello 123 world 456 nihao 789"

    @unittest.skip('re.sub与replace对比')
    def test_fun1(self):
        self.set_data()
        replacedStr = self.inputStr.replace("111", "222")
        replacedStr2 = re.sub(r'\d+', '222', self.inputStr2)
        print(replacedStr)
        print(replacedStr2)

    @unittest.skip('整个这样的字符串，换成crifanli')
    def test_pattern(self):
        #    反斜杠加数字（\N），则对应着匹配的组（matched group）
        #    比如\6，表示匹配前面pattern中的第6个group
        #    意味着，pattern中，前面肯定是存在对应的，第6个group，然后你后面也才能去引用
        self.set_data()
        replacedStr = re.sub(
            r'hello (\w+), nihao \1',
            'crifanli',
            self.inputStr3)
        print(replacedStr)

    # @unittest.skip(' \g 使用说明')
    def test_repl(self):
        #   \n：会被处理为对应的换行符；
        #   \r：会被处理为回车符；
        #   其他不能识别的转移字符，则只是被识别为普通的字符：
        #   比如\j，会被处理为j这个字母本身；
        #   反斜杠加g以及中括号内一个名字，即：\g<name>，对应着命了名的组，named group
        self.set_data()
        replacedStr = re.sub(
            r'hello (\w+), nihao \1',
            r'\g<1>',
            self.inputStr3)
        print(replacedStr)

    @unittest.skip('想要把其中的数字部分，都加上111')
    def test_repl(self):
        self.set_data()
        replacedStr = re.sub(r"(?P<number>\d+)", _add111, self.inputStr2)
        print("replacedStr=", replacedStr)  # hello 234 world 567

    # @unittest.skip('假如对于匹配到的内容，只处理其中一部分都加上111')
    def test_count(self):
        self.set_data()
        replacedStr = re.sub(r"(?P<number>\d+)", _add111, self.inputStr4, 2)
        print("replacedStr=", replacedStr)  # hello 234 world 567


if __name__ == "__main__":
    unittest.main(verbosity=2)
