#!/usr/bin/python
# -*- coding:utf-8 -*-

def power_def(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 函数的第二个参数为默认
# 必选参数在前，默认参数在后
print power_def(5)
print power_def(2,10)

# 函数的参数有四种 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

# 通过一个tuple和dict，你也可以调用该函数：
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

# 小结
'''Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''

