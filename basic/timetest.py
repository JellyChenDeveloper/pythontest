# coding=utf-8

"""
时间测试
@author: JellyChen
@software: PyCharm
@file: timetest.py
@time: 2016/8/26 17:52
"""

import calendar
import time


def cal_test():
    print calendar.month(2016, 1)
    return


def run():
    """ run -- 文件测试函数 """
    ticks = time.time()
    print ticks

    localtime = time.localtime(ticks)
    print localtime

    print time.asctime(localtime)
    print time.strftime("%Y-%m-%d %H:%M:%S", localtime)

    print '日历'
    cal1 = calendar.month(2016, 1)
    print cal1
    return


if __name__ == '__main__':
    run()
