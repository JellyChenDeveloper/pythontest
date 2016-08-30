# coding=utf-8

"""
测试使用beautifulsoup4
@author: JellyChen
@software: PyCharm
@file: bs4test.py
@time: 2016/8/29 18:57
"""
from bs4 import BeautifulSoup
from urllib import urlopen


def test():
    html = urlopen('http://www.23wx.com/html/64/64788/').read()
    soup = BeautifulSoup(html, 'html5lib')
    # print soup.prettify()
    # print soup.title
    # print soup.title.name
    # print soup.title.string
    # print soup.title.parent.name
    # print soup.p
    # print soup.p['class']
    # print soup.find_all('a')
    print soup.find(id='at')
    # for link in soup.find_all('a'):
    #     print(link.get('href'))
    #     print(link.get_text())
    # print(soup.get_text())


def run():
    """ run -- 文件测试函数 """
    test()


if __name__ == "__main__":
    run()
