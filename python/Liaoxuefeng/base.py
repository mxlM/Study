#!/usr/bin/python
# -*- coding:utf-8 -*-

# 1. 浮点数表示
a=2e10
print a

# 2. 字符串表示
print 'I\'m ok.'
# 3. / 不转义
print r'I\'m ok.'
#4. 多行 '''***'''
print '''line1
... line2
... line3'''

#5. 布尔型 也可以使用 and or not 运算
print True and True

# 6.空值 None
# 7. 常量 习惯大写字母表示
PI = 3.14159265359
# 8. 类型隐性转换
print 10/3
print 10.0/3

# 9. 字母和数字转化
print ord('A')
print chr(65)

#10. 中文
print u'中文'

#11. Unicode 和 ascll 码相互转换
print  u'ABC'.encode('utf-8')
#'ABC'
print u'中文'.encode('utf-8')
# '\xe4\xb8\xad\xe6\x96\x87'

# 12. 长度
print len(u'ABC')
#3
print len('ABC')
#3
print len(u'中文')
#2
print len('\xe4\xb8\xad\xe6\x96\x87')
#6

# 13. list
list=[1,2,'333']
len(list)
list[-1]
list.append(4)
list.pop() #删除最后一个元素
list.pop(1)
list[0]='a'  # ['a', '333']
list2=['bb']
list2.append(list)  #['bb', ['a', '333']]
print list2[1][0] # a

#14 tuple 有序列表
classmates = ('Michael', 'Bob', 'Tracy') #不可改变
t=() #空 tuple
t=(1) # == t=1
t=(1,)

#15 条件循环
age=20
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age>=10:
    print "child"
else:
    print "baby"

#16 dict 不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print 'Thomas' in d # 判断该key是否存在
d.pop('Bob') # 删除对应的 key 值

print d.get('Thomas')
print d.get('Thomas', -1) # 如果key 不存在 返回 -1

'''和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而增加；
需要占用大量的内存，内存浪费多。
而list相反
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。'''


#17 set 和 dict 一样 key不能重复，只有key，没有value,且key 不能重复，不可变对象
s = set([1, 1, 2, 2, 3, 3]) # 实际 set([1, 2, 3])
s.add(4)
s.remove(1)


#18. 只有list 是可变对象
a = ['c', 'b', 'a']
a.sort() #['a', 'b', 'c']

#str 不可变对象
a = 'abc'
b=a.replace('a', 'A') # Abc



