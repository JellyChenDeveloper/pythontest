# coding=utf-8
import urllib
import re


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


# 根据网页内容解析图片链接并下载图片至本地
def get_img(html):
    rex = r'src="(http://imgsrc\.baidu\.com/forum/.+?\.jpg)"'
    imglist = re.findall(rex, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)  # 下载图片至本地并规范化文件名
        x += 1


def test():
    html = get_html("http://tieba.baidu.com/p/4745904310")
    print get_img(html)
    # http://imgsrc.baidu.com/forum/w%3D580/sign=e6e6f428ac0f4bfb8cd09e5c334e788f/be248d44ad345982d6537e2504f431adc9ef84a1.jpg


def run():
    """ run -- 文件测试函数 """
    test()


if __name__ == "__main__":
    run()
