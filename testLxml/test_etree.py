#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 17:11
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : test_etree.py
# @Software: PyCharm

from lxml import etree
import unittest
import os


class Test(unittest.TestCase):
    def set_data(self):
        web_data = """
                    <div>
                        <ul>
                             <li class="item-0"><a href="link1.html">first item</a></li>
                             <li class="item-1"><a href="link2.html">second item</a></li>
                             <li class="item-inactive"><a href="link3.html">third item</a></li>
                             <li class="item-1"><a href="link4.html">fourth item</a></li>
                             <li class="item-0"><a href="link5.html">fifth item</a>
                         </ul>
                     </div>
                    """
        self.web_data = web_data

    @unittest.skip('暂时跳过用例1的测试')
    def test_s1(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        print(html)
        result = etree.tostring(html)
        print(result.decode('utf-8'))

    @unittest.skip('暂时跳过用例2的测试')
    def test_s2(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        print(html)
        result = etree.tostring(html)
        print(result.decode('utf-8'))
        """
        输出
        <Element html at 0x39e58f0>
        <html><body><div>
                    <ul>
                         <li class="item-0"><a href="link1.html">first item</a></li>
                         <li class="item-1"><a href="link2.html">second item</a></li>
                         <li class="item-inactive"><a href="link3.html">third item</a></li>
                         <li class="item-1"><a href="link4.html">fourth item</a></li>
                         <li class="item-0"><a href="link5.html">fifth item</a>
                     </li></ul>
                 </div>
                </body></html>
        """





# 3、获取某个标签的内容(基本使用)，注意，获取a标签的所有内容，a后面就不用再加正斜杠，否则报错。
#
# 　　写法一
    @unittest.skip('暂时跳过用例3的测试')
    def test_s3(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('/html/body/div/li/a')
        print(html)
        for i in html_data:
            print(i.text)

        """
        输出
        <Element html at 0x12fe4b8>
        first item
        second item
        third item
        fourth item
        fifth item
        """

#写法二（直接在需要查找内容的标签后面加一个/text()就行）
    @unittest.skip('暂时跳过用例4的测试')
    def test_s4(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('/html/body/div/ul/li/a/text()')
        print(html)
        for i in html_data:
            print(i)
        """
        <Element html at 0x138e4b8>
        first item
        second item
        third item
        fourth item
        fifth item
        """

##4、打开读取html文件

#使用parse打开html文件
    @unittest.skip('暂时跳过用例5的测试')
    def test_s5(self):
        html = etree.parse('test.html')
        html_data = html.xpath('//*')#打印是一个列表，需要遍历
        print(html_data)
        for i in html_data:
            print(i.text)

    @unittest.skip('暂时跳过用例6的测试')
    def test_s6(self):
        html = etree.parse('test.html')
        html_data = etree.tostring(html,pretty_print=True)
        res = html_data.decode('utf-8')
        print(res)
        """
        输出
        <div>
             <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a></li>
             </ul>
        </div>
        """


##5、打印指定路径下a标签的属性（可以通过遍历拿到某个属性的值，查找标签的内容
    @unittest.skip('暂时跳过用例7的测试')
    def test_s7(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('/html/body/div/ul/li/a/@href')
        for i in html_data:
            print(i)

        """
        输出
        link1.html
        link2.html
        link3.html
        link4.html
        link5.html
        """

#6、我们知道我们使用xpath拿到得都是一个个的ElementTree对象，所以如果需要查找内容的话，还需要遍历拿到数据的列表。
#　　查到绝对路径下a标签属性等于link2.html的内容。
    @unittest.skip('暂时跳过用例8的测试')
    def test_s8(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('/html/body/div/ul/li/a[@href="link2.html"]/text()')
        print(html_data)
        for i in html_data:
            print(i)
        """
        输出
        ['second item']
        second item
        """

#7、上面我们找到全部都是绝对路径（每一个都是从根开始查找），下面我们查找相对路径，例如，查找所有li标签下的a标签内容。
    @unittest.skip('暂时跳过用例9的测试')
    def test_s9(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('//li/a/text()')
        print(html_data)
        for i in html_data:
            print(i)
        """
        输出
        ['first item', 'second item', 'third item', 'fourth item', 'fifth item']
        first item
        second item
        third item
        fourth item
        fifth item
        """

#8、上面我们使用绝对路径，查找了所有a标签的属性等于href属性值，利用的是/---绝对路径，下面我们使用相对路径，查找一下l相对路径下li标签下的a标签下的href属性的值，注意，a标签后面需要双//
    @unittest.skip('暂时跳过用例10的测试')
    def test_s10(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('//li/a//@href')
        print(html_data)
        for i in html_data:
            print(i)
        """
            输出
            ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
            link1.html
            link2.html
            link3.html
            link4.html
            link5.html
        """

#9、相对路径下跟绝对路径下查特定属性的方法类似，也可以说相同
    @unittest.skip('暂时跳过用例11的测试')
    def test_s11(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('//li/a[@href="link2.html"]')
        print(html_data)
        for i in html_data:
            print(i.text)
        """
        输出
        [<Element a at 0x216e468>]
        second item
        """

#10、查找最后一个li标签里的a标签的href属性
    # @unittest.skip('暂时跳过用例12的测试')
    def test_s12(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('//li[last()]/a/text()')
        print(html_data)
        for i in html_data:
            print(i)
        """
        输出
        ['fifth item']
        fifth item
        """

##11、查找倒数第二个li标签里的a标签的href属性
    # @unittest.skip('暂时跳过用例13的测试')
    def test_s13(self):
        self.set_data()
        html = etree.HTML(self.web_data)
        html_data = html.xpath('//li[last()-1]/a/text()')
        print(html_data)
        for i in html_data:
            print(i)
        """
        输出
        ['fourth item']
        fourth item
        """

if __name__ == "__main__":
    test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_etree.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)
    # unittest.main(verbosity=2)



























