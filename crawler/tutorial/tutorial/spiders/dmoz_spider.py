# coding=utf-8

"""

@author: JellyChen
@software: PyCharm
@file: dmoz_spider.py
@time: 2016/8/31 11:17
"""
from scrapy.spider import Spider
from scrapy.selector import Selector
from crawler.tutorial.tutorial.items import TutorialItem
# from tutorial.items import TutorialItem

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items = []
        for site in sites:
            item = TutorialItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items
