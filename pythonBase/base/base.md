# 字符编码
## 基本概念
* encode:编码
* decode：解码
* python2 默认ascii编码
* python3 默认utf-8编码

## Python2 中的字符类型
> Python2 中有两种和字符串相关的类型：str 和 unicode，它们的父类是 basestring。其中，str 类型的字符串有多种编码方式，默认是 ascii，还有 gbk，utf-8 等，unicode 类型的字符串使用 u'...' 的形式来表示，下面的图展示了 str 和 unicode 之间的关系


![blockchain](https://ooo.0o0.ooo/2016/11/16/582c111e3fa73.png)

# 输入输出
    def input(prompt):
        return (eval(raw_input(prompt)))
    
    
