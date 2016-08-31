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
import urlparse
import re

reload(sys)
sys.setdefaultencoding("utf-8")


class CovelCrawler:
    ''' class CovelCrawler 输入基链接获取整个网站的数据 '''

    __basehrefprase = ''

    def __init__(self):
        return

    def run(self, href):
        """ run -- """
        self.__basehrefprase = urlparse.urlparse(href)
        # self.__saveFile(self.__getChapterContent(href))
        self.__praseTotalList(href)

    def __getNovelList(self, baseurl):
        """ __getNovelList -- 获取小说列表 """
        return

    def __praseTotalList(self, href):
        """ __praseList -- """
        pagecount = self.__getPageCount(href)
        pagecount = int(pagecount)
        pagehreflist = []
        for i in range(pagecount):
            output = re.sub(r'(\d)(\.)', str(i + 1) + ".", self.__basehrefprase.path)
            url = urlparse.urlunparse((self.__basehrefprase.scheme, self.__basehrefprase.netloc,
                                       output, "", "", ""))
            pagehreflist.append(url)
        print pagehreflist[pagecount-1]
        return pagehreflist

    def __getPageCount(self, href):
        """ getPageCount -- """
        html = urlopen(href).read()
        soup = BeautifulSoup(html, 'html5lib')
        maxpage = soup.find(id='pagelink').find(class_='last').string
        return maxpage

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
    # start.run('http://www.23wx.com/html/64/64788/26397082.html')
    start.run('http://www.23wx.com/class/11_1.html')


if __name__ == "__main__":
    run()
