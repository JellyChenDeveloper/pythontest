# coding=utf-8

# todo 暂时先停下，学完多线程等内容再继续

"""
测试使用beautifulsoup4
@author: JellyChen
@software: PyCharm
@file: bs4test.py
@time: 2016/8/29 18:57
"""

from bs4 import BeautifulSoup
from urllib import urlopen
# import sys
import urlparse
import re


# reload(sys)
# sys.setdefaultencoding("utf-8")


class CovelCrawler:
    """ class CovelCrawler 输入基链接获取整个网站的数据 """

    __basehrefprase = ''

    def __init__(self):
        return

    def run(self, href):
        """ run -- """
        self.__basehrefprase = urlparse.urlparse(href)
        # self.__saveFile(self.__getChapterContent(href))
        pagelist = self.__prase_total_list(href)
        novellist = []
        for pageurl in pagelist:
            subnovelist = self.__get_novel_list(pageurl)
            novellist.append(subnovelist)
        print len(novellist)
        return novellist

    def __get_novel_list(self, baseurl):
        """ __getNovelList -- 获取小说列表 """
        html = urlopen(baseurl).read()
        soup = BeautifulSoup(html, 'html5lib')
        booklist = soup.find(id='content').find('table').find_all('a', href=re.compile(r"/book/"))
        books = []
        for book in booklist:
            bookinfo = {'name': book.string, "url": book.get('href')}
            books.append(bookinfo)
        return books

    def __prase_total_list(self, href):
        """ __praseList -- """
        pagecount = self.__get_page_count(href)
        pagecount = int(pagecount)
        pagehreflist = []
        for i in range(pagecount):
            output = re.sub(r'(\d)(\.)', str(i + 1) + ".", self.__basehrefprase.path)
            url = urlparse.urlunparse((self.__basehrefprase.scheme, self.__basehrefprase.netloc,
                                       output, "", "", ""))
            pagehreflist.append(url)
        # print pagehreflist[pagecount-1]
        return pagehreflist

    def __get_page_count(self, href):
        """ getPageCount -- """
        html = urlopen(href).read()
        soup = BeautifulSoup(html, 'html5lib')
        maxpage = soup.find(id='pagelink').find(class_='last').string
        return maxpage

    def __get_chapter_llst(self, novelurl):
        """ __getChapterList -- 获取章节列表 """
        html = urlopen(novelurl).read()
        soup = BeautifulSoup(html, 'html5lib')
        chapters = soup.find(id='at')
        chapter_links = []
        chapter_names = []
        for link in chapters.find_all('a'):
            chapter_links.append(link.get('href'))
            name = link.get_text()
            chapter_names.append(name)
        return chapter_links, chapter_names

    def __get_chapter_content(self, chapterurl):
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

    def __save_file(self, content, chaptername='章节名', name='test'):
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
