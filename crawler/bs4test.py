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
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class CovelCrawler:
    ''' class CovelCrawler 输入基链接获取整个网站的数据 '''

    __basehref = ''

    def __init__(self):
        return

    def run(self, href):
        """ run -- """
        self.__basehref = href
        self.__saveFile(self.__getChapterContent(href))

    def __getNovelList(self, baseurl):
        """ __getNovelList -- 获取小说列表 """
        return

    def __getChapterList(self, novelurl):
        """ __getChapterList -- 获取章节列表 """
        html = urlopen(novelurl).read()
        soup = BeautifulSoup(html, 'html5lib')
        chapters = soup.find(id='at')
        chapterLinks = []
        chapterNames = []
        for link in chapters.find_all('a'):
            chapterLinks.append(link.get('href'))
            name = link.get_text()
            chapterNames.append(name)
        return chapterLinks, chapterNames

    def __getChapterContent(self, chapterurl):
        """ __getChapterContent -- 获取章节内容 """
        html = urlopen(chapterurl).read()
        soup = BeautifulSoup(html, 'html5lib')
        content = soup.find(id='contents').contents
        cont = ''
        for text in content:
            text = str(text)
            text = text.lstrip()
            text = text.replace("<br/>", "\n")
            cont += text
        return cont

    def __saveFile(self, content, chaptername='章节名', name='test'):
        """ __saveFile -- 保存章节内容 """
        fo = open(name + ".txt", "a+")
        fo.write(chaptername)
        fo.write("\n")
        fo.write(content)
        fo.write("\n\n\n")
        fo.close()


def run():
    """ run -- 文件测试函数 """
    start = CovelCrawler()
    start.run('http://www.23wx.com/html/64/64788/26397082.html')

if __name__ == "__main__":
    run()
