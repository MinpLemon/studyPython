#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-25 13:17
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : class_magic.py
# @Software: PyCharm

"""
__new__ 在 __init__ 之前被调用，用来创建实例。
__str__ 是用 print 和 str 显示的结果，__repr__ 是直接显示的结果。
__getitem__ 用类似 obj[key] 的方式对对象进行取值
__getattr__ 用于获取不存在的属性 obj.attr
__call__ 使得可以对实例进行调用
__slots__:限定允许绑定的属性
        设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 slots，这样，子类允许定义的属性就是自身的 slots 加上父类的 slots

"""

# __new__


class A(object):
    _dict = dict()

    def __new__(cls, *args, **kwargs):
        if 'key' in A._dict:
            print('EXISTS')
            return A._dict['key']
        else:
            print('NEW')
            return object.__new__(cls)

    def __init__(self):
        print('INIT')
        A._dict['key'] = self


a1 = A()

# ------------------------------------

# __str__


class Foo(object):
    def __init__(self, name):
        self.name = name


"""
>>> print Foo('ethan')
<__main__.Foo object at 0x10c37aa50>
"""
# 在上面，我们使用 print 打印一个实例对象，但如果我们想打印更多信息呢，比如把 name 也打印出来，这时，我们可以在类中加入
# __str__ 方法，如下


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Foo object (name: %s)' % self.name


"""
>>> print Foo('ethan')      # 使用 print
Foo object (name: ethan)
>>>
>>> str(Foo('ethan'))       # 使用 str
'Foo object (name: ethan)'
>>>
>>> Foo('ethan')             # 直接显示
<__main__.Foo at 0x10c37a490>
"""


# ------------------------------------

# iter  实例对象可被用于 for...in 循环，这时我们需要在类中定义 __iter__ 和 __next__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 返回迭代器对象本身
        return self

    def __next__(self):      # 返回容器下一个元素
        self.a, self.b = self.b, self.a + self.b
        return self.a


"""
>>> fib = Fib()
>>> for i in fib:
...     if i > 10:
...         break
...     print i
...
1
1
2
3
5
8
"""
# ------------------------------------

# getitem 使用 obj[n] 这种方式对实例对象进行取值


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


"""
>>> fib = Fib()
>>> fib[0], fib[1], fib[2], fib[3], fib[4], fib[5]
(1, 1, 2, 3, 5, 8)
"""
# ------------------------------------

# getattr 当我们获取对象的某个属性，如果该属性不存在，会抛出 AttributeError 异常


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattr__(self, attr):
        if attr == 'z':
            raise AttributeError("Point object has no attribute %s" % attr)

    def __setattr__(self, *args, **kwargs):
        print
        'call func set attr (%s, %s)' % (args, kwargs)
        return object.__setattr__(self, *args, **kwargs)

    def __delattr__(self, *args, **kwargs):
        print
        'call func del attr (%s, %s)' % (args, kwargs)
        return object.__delattr__(self, *args, **kwargs)


"""
>>> p = Point(3, 4)
call func set attr (('x', 3), {})
call func set attr (('y', 4), {})
>>> p.z
0
>>> p.z = 7
call func set attr (('z', 7), {})
>>> p.z
7
>>> p.w
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __getattr__
AttributeError: Point object has no attribute w
>>> p.w = 8
call func set attr (('w', 8), {})
>>> p.w
8
>>> del p.w
call func del attr (('w',), {})
>>> p.__dict__
{'y': 4, 'x': 3, 'z': 7}
"""
# ------------------------------------

# call 使用 obj.method() 来调用对象的方法


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, z):
        return self.x + self.y + z


"""
>>> p = Point(3, 4)
>>> callable(p)     # 使用 callable 判断对象是否能被调用
True
>>> p(6)            # 传入参数，对实例进行调用，对应 p.__call__(6)
13                  # 3+4+6
"""
# ------------------------------------
# Point_base 用于对比


class Point_base(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


pb = Point_base(3, 4)
pb.z = 5  # 很有用，但它的代价是消耗了更多的内存
"""
>>> p.__dict__
{'x': 3, 'y': 4, 'z': 5}
"""


# __slots__
class Point_slots(object):
    __slots__ = ('x', 'y')  # 只允许使用 x 和 y

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


ps = Point_slots(3, 4)
ps.z = 5
"""
AttributeError                            Traceback (most recent call last)
<ipython-input-648-625ed954d865> in <module>()
----> 1 p.z = 5

AttributeError: 'Point' object has no attribute 'z'
"""
