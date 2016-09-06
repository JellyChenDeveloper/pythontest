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
        """ 构造函数 """
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        """ displayCount --  """
        print "Total Employee %d" % Employee.empCount

    def display_employee(self):
        """ displayEmployee --  """
        print "Name : ", self.name, ", Salary: ", self.salary

    def __del__(self):
        """ 析构函数 """
        class_name = self.__class__.__name__
        print class_name, "销毁"


def run():
    """ run -- 文件测试函数 """
    emp1 = Employee('jelly', 30)
    emp1.display_count()
    emp2 = Employee("Manni", 5000)
    emp1.display_count()
    emp1.display_employee()
    print "Total Employee %d" % Employee.empCount

    # print "Employee.__doc__:", Employee.__doc__
    # print "Employee.__name__:", Employee.__name__
    # print "Employee.__module__:", Employee.__module__
    # print "Employee.__bases__:", Employee.__bases__
    # print "Employee.__dict__:", Employee.__dict__
    del emp1


if __name__ == "__main__":
    run()
