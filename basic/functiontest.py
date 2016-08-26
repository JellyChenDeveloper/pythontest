# coding=utf-8
import math
import time

import timetest
from timetest import cal_test


def func1(arg):
    print arg
    return


def func2(p1, p2):
    print p1,
    p2 += 5
    print p2
    return


def func3(array):
    array.append([2, 3])
    print array
    return


def func4(p1, *ps):
    print p1
    for pt in ps:
        print pt
    return


sumt = lambda a1, a2: a1 + a2


def sum1(a1, a2):
    total = a1 + a2
    print globals()
    print locals()
    return total


func1("hello")
func2(1, 2)
pt2 = 2
func2(p2=pt2, p1=1)
print pt2
func2(1, pt2)
print pt2
listtest = [4, 5, 6, 7]
func3(listtest)
print listtest

func4('a', 'b,c', 'd', 'e')

print sumt(3, 4)

print sum1(1, 10)

print dir(time)
print dir(math)
print dir(timetest)

cal_test()
