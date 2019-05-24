#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 16:36
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_json_special.py
# @Software: PyCharm

"""
Python解析非标准JSON（Key值非字符串）
采集数据的时候经常碰到一些JSON数据的Key值不是字符串，这些数据在JavaScript的上下文中是可以解析的，
但在Python中，没有该部分数据的上下文，无法采用json.loads(JSON)的形式导入。在网上搜集来一些方法以便日后使用

为方便理解点开网页：http://www.cnblogs.com/txw1958/archive/2012/08/02/python3-json-non-standard.html
json验证器：https://jsonlint.com
信息来源：https://www.cnblogs.com/taceywong/p/5876621.html

"""

#举例不标准json数据
{
    url: 'http://txw1958.cnblogs.com',
    uid: 100000
}

#方法一
def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    obj = eval(expr, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
    return obj


#方法二
def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    import ast
    m = ast.parse(expr)
    a = m.body[0]

    def parse(node):
        if isinstance(node, ast.Expr):
            return parse(node.value)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Dict):
            return dict(zip(map(parse, node.keys), map(parse, node.values)))
        elif isinstance(node, ast.List):
            return map(parse, node.elts)
        else:
            raise NotImplementedError(node.__class__)

    return parse(a)


import unittest


