#!/usr/bin/python
# -*- coding:utf-8 -*-

#1. 实现step=2 的list
L = []
L = range(1,100,2)
print L

# 2. 切片
L2 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L2[:3]
print L2[0:3] # 取前三个元素

print L2[-2:] # 取最后两个元素

print L2[:6:2] # 每两个元素取一个
L3=L2[:] # L3=L2 等同
print L3

#tuple 也可以切片，返回依然是tuple
print (0, 1, 2, 3, 4, 5)[:3]

#3. 迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的

list=range(1,10)
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
for k,v in d.iteritems(): # 也可以用 item()
    print k,v

# 判断是否为迭代对象
from collections import Iterable
print isinstance('abc', Iterable) # True
print isinstance(123,Iterable) # False

# 对于list 同时输出索引和对应的元素
for i, value in enumerate(['A', 'B', 'C']):
    print i, value


# 4. 列表生成式
L=[]
for x in range(1, 11):
    L.append(x * x)
print L
print [x * x for x in range(1, 11)]

# 也可以进行筛选，或者两层循环
print [x * x for x in range(1, 11) if x % 2 == 0]
print [m + n for m in 'ABC' for n in 'XYZ']

import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')]

# list可以不使用for来迭代
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]

# 5. 生成器

L = [x * x for x in range(10)]
print L # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print g  # <generator object <genexpr> at 0x104feab40>

