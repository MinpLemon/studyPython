#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:36
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_json.py
# @Software: PyCharm

import unittest
import json


class Test(unittest.TestCase):
    def set_data(self):
        self.a = {'name': 'wang', 'age': '20'}
        self.aa = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
        # print(type(self.a)) #<type 'dict'>

    @unittest.skip('json.dumps')
    def test_json_dumps(self):
        self.set_data()
        b = json.dumps(self.a)
        print()
        print(b, type(b))  #{"age": "20", "name": "wang"} <type 'str'>


    # @unittest.skip('json.loads')
    def test_json_loads(self):
        self.set_data()
        c = json.loads(self.aa) #loads 入参str
        print(c, type(c)) #{u'age': u'20', u'name': u'wang'} <type 'dict'>


if __name__ == "__main__":
    unittest.main(verbosity=2)