# coding=utf-8

"""
python面向对象
@author: JellyChen
@software: PyCharm
@file: classtest.py
@time: 2016/8/26 18:21
"""


class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        """ displayCount --  """
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        """ displayEmployee --  """
        print "Name : ", self.name, ", Salary: ", self.salary


def run():
    """ run -- 文件测试函数 """
    print("hello")


if __name__ == "__main__":
    run()
