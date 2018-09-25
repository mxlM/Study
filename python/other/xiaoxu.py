#!/usr/bin/python
# -*- coding:utf-8 -*-

# 1.list的升序和降序
num=[11,22,44,1,2,3]
num.sort() # 升序
print num
num.sort(reverse=True) #降序
print num
# num.reserve() # 倒序 python 3 中才有该方法

# 比较list的元素是字典
nums=[{"name":"zhangsan","age":13},{"name":"lisi","age":10},{"name":"wangwu","age":20}]
# 匿名函数 下面的x实际是list中的元素（字典），冒号后面的值相当于返回值
nums.sort(key=lambda x:x['name'])
print nums

#2. 匿名函数做实参
def test(a,b,func):
    result=func(a,b)
    return result
num = test(11,12,lambda x,y:x-y) # lambda ： 后面是return 的值
print num

# 3. 匿名函数扩展
# 因为python 语言是动态语言，即在运行的那一刻才知道语言的规范是否正确，所以在python2 中 可以将输入参数作为匿名函数
def test2(a,b,func):
    result=func(a,b)
    return result

 # 执行时 输入 lambda x,y:x-y 即可 ，但是在python 3 中不可以这么使用，因为 python3 默认将输入的参数看作字符串
# 但是可以将输入的lambda x,y:x-y  转换为表达式，使用 func_new=eval(input("输入匿名函数"))
func_new=input("输入匿名函数")
num = test2(11,12,func_new) # lambda ： 后面是return 的值
print num


# 4.
