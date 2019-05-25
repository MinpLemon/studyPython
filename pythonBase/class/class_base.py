#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-25 13:18
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : class_base.py
# @Software: PyCharm


"""
知识点：
类:Animal 是类名，通常类名的首字母采用大写（如果有多个单词，则每个单词的首字母大写），后面紧跟着 (object)，表示该类是从哪个类继承而来的
实例: 实例化 animal = Animal()
pass:跳过
__init__:初始化
self:指向创建的实例本身
__：访问限制，属性加下划线，只能class内部访问
_:一种规范，约定熟成的书写方式，表示内部访问调用，（其实和没有'_'使用一模一样）
type:获取对象类型
isinstance(obj, type) :判断对象是否为指定的 type 类型的实例
hasattr(obj, attr) :判断对象是否具有指定属性/方法
getattr(obj, attr[, default]): 获取属性/方法的值, 要是没有对应的属性则返回 default 值（前提是设置了 default），否则会抛出 AttributeError 异常；
dir(obj) :可以获取相应对象的所有属性和方法名的列表
Dog(Animal)：继承，Dog 类是从 Animal 类继承而来的，Dog 类自动获得了 Animal 类的所有数据和方法，而且还可以对父类的方法进行修改
    有了继承，才有了多态，不同类的对象对同一消息会作出不同的相应
@classmethod :它就变成了一个类方法，class_foo 的参数是 cls，代表类本身,可以使用类和实例来调用
@staticmethod : 静态方法没有 self 和 cls 参数，可以把它看成是一个普通的函数，我们当然可以把它写到类外面，
    但这是不推荐的，因为这不利于代码的组织和命名空间的整洁。可以使用类和实例来调用


"""


class Animal():
    # pass
    tdata = 1

    def __init__(self,name):
        self.name = name
        self.__age = '12'

    def greet(self):
        print('Hello, I am %s.' % self.name)

    def get_age(self):
        return self.__age

    @classmethod
    def class_foo(cls):
        print(cls.tdata)              #cls   调用属性
        print(cls('minp2').name)      #cls() 调用实例属性
        print(cls('minp3').get_age()) #cls() 调用方法


    @staticmethod
    def static_foo():
        print('hello'+Animal.tdata)

class Dog(Animal):
    pass




# animal = Animal()
dog1 = Animal('dog1')
dog2 = Animal('dog2')
dog1.name
print(dog1.get_age())
type(dog1)
isinstance(dog2,Animal)
hasattr(dog2,'name')
getattr(dog2, 'name')
getattr(dog2, 'greet')



dog1.class_foo()
