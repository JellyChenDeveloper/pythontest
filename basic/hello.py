# coding=utf-8

"""
开始python之旅
@author: JellyChen
@software: PyCharm
@file: hello.py
@time: 2016/8/26 17:52
"""

def run():
    """ run -- 文件测试函数 """
    print "hello,world!"
    print "你好"

    print "\n数字类型"
    print 1,
    print 1.1,
    print 1L,
    a = 3j
    b = 5j
    print a + b

    print "\n字符串类型"
    tmp_str = "qwoliudhoqwnjdjliaushdlqnjwdn"
    print tmp_str[0],
    print tmp_str[-1],
    print tmp_str[-5],
    print tmp_str[5],
    print tmp_str[5:10] * 3,
    print tmp_str[-10:-1]

    print "列表List(数组)"
    tmp_list = ['1', 2, 3.3, "hello"]
    print tmp_list,
    print tmp_list[3],
    print tmp_list * 2,
    del tmp_list[0]
    print tmp_list,
    print len(tmp_list),
    print tmp_list[:3],
    print max(tmp_list),
    print min(tmp_list)
    tmp_list.append('123')
    print tmp_list
    print tmp_list.count(2)
    tmp_list.reverse()
    print tmp_list

    print "\n元组"
    tup = (1, 2, 3, 4, '123', 'asd')
    print tup
    del tup
    # print tup # 注释去掉后程序失败，因为删除
    return


if __name__ == '__main__':
    run()
