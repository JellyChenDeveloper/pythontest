# coding=utf-8

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
str = "qwoliudhoqwnjdjliaushdlqnjwdn"
print str[0],
print str[-1],
print str[-5],
print str[5],
print str[5:10] * 3,
print str[-10:-1]

print "列表List(数组)"
list = ['1', 2, 3.3, "hello"]
print list,
print list[3],
print list * 2,
del list[0]
print list,
print len(list),
print list[:3],
print max(list),
print min(list)
list.append('123')
print list
print list.count(2)
list.reverse()
print list

print "\n元组"
tup = (1, 2, 3, 4, '123', 'asd')
print tup
del tup
print tup
