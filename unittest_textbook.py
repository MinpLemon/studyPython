#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-25 09:49
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : unittest_textbook.py
# @Software: PyCharm

"""
assertAlmostEqual(first, second[, places, ...])
适用于小数，place是应最少几位相等布尔值才为1（默认为7），如果在place位以内不同则断言失败。
assertDictContainsSubset(expected, actual[, msg])
检查实际是否超预期
assertDictEqual(d1, d2[, msg])
前后字典是否相同
assertEqual(first, second[, msg])
前后两个数不等的话，失败
assertFalse(expr[, msg])
检查表达式是否为假
assertGreater(a, b[, msg])
和self.assertTrue(a > b)用法一样,但是多了设置条件 .
assertGreaterEqual(a, b[, msg])
和self.assertTrue(a > =b)用法一样,但是多了设置条件 .
assertIn(member, container[, msg])
self.assertTrue(a in b)
assertIs(expr1, expr2[, msg])
assertTrue(a is b)
assertIsInstance(obj, cls[, msg])
Isinstance(a,b)
assertIsNone(obj[, msg])
Obj is none.
assertIsNot(expr1, expr2[, msg])
a is not b.
assertIsNotNone(obj[, msg])
Obj is not none.
assertItemsEqual(expected_seq, actual_seq[, msg])
一个无序的序列特异性的比较。
assertLess(a, b[, msg])
Just like self.assertTrue(a < b), but with a nicer default message.
assertLessEqual(a, b[, msg])
Just like self.assertTrue(a <= b), but with a nicer default message.
assertListEqual(list1, list2[, msg])
List1与list2是否相等.
assertMultiLineEqual(first, second[, msg])
断言，2个多行字符串是相等的
assertNotAlmostEqual(first, second[, ...])
Fail if the two objects are equal as determined by their difference rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the between the two objects is less than the given delta.
assertNotAlmostEquals(first, second[, ...])
Fail if the two objects are equal as determined by their difference rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the between the two objects is less than the given delta.
assertNotEqual(first, second[, msg])
Fail if the two objects are equal as determined by the ‘==’
assertNotEquals(first, second[, msg])
Fail if the two objects are equal as determined by the ‘==’
assertNotIn(member, container[, msg])
Just like self.assertTrue(a not in b), but with a nicer default message.
assertNotIsInstance(obj, cls[, msg])
Included for symmetry with assertIsInstance.
assertNotRegexpMatches(text, unexpected_regexp)
如果文本匹配正则表达式，将失败。
assertRaises(excClass[, callableObj])
除非excclass类抛出异常失败
assertRaisesRegexp(expected_exception, ...)
认为在引发异常的情况下消息匹配一个正则表达式。
assertRegexpMatches(text, expected_regexp[, msg])
测试失败，除非文本匹配正则表达式。
assertSequenceEqual(seq1, seq2[, msg, seq_type])
有序序列的相等断言 (like lists and tuples).
assertSetEqual(set1, set2[, msg])
A set-specific equality assertion.
assertTrue(expr[, msg])
Check that the expression is true.
assertTupleEqual(tuple1, tuple2[, msg])
A tuple-specific equality assertion.
assert_(expr[, msg])
Check that the expression is true.
---------------------
原文：https://blog.csdn.net/qq1124794084/article/details/51668672
深入理解unittest :https://blog.csdn.net/hackerain/article/details/24095117

"""

"""
注： test 开头的方法和类会默认使用pytest或unittest


"""