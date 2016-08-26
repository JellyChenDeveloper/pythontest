# coding=utf-8
import time
import calendar

ticks = time.time()
print ticks

localtime = time.localtime(ticks)
print localtime

print time.asctime(localtime)
print time.strftime("%Y-%m-%d %H:%M:%S", localtime)

print '日历'
cal1 = calendar.month(2016, 1)
print cal1
