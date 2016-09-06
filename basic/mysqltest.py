# coding=utf-8

"""
测试python的mysql连接操作
@author: JellyChen
@software: PyCharm
@file: mysqltest.py
@time: 2016/8/29 17:14
"""
import MySQLdb


def get_version():
    db = MySQLdb.connect("127.0.0.1", "root", "root", "gameinfo")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print "Database version : %s " % data
    db.close()


def getusers():
    db = MySQLdb.connect("127.0.0.1", "root", "root", "gameinfo")
    cursor = db.cursor()
    sql = '''select * from map limit 20'''
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # fname = row[0]
            # lname = row[1]
            # age = row[2]
            # sex = row[3]
            # income = row[4]
            # 打印结果
            print row
    except:
        print "Error: unable to fecth data"
    db.close()


def run():
    """ run -- 文件测试函数 """
    getusers()


if __name__ == "__main__":
    run()
