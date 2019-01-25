#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing

#装饰器的使用
def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s  %s' % (argv, func.__name__))
            func(a, b)
            print('stop')
        return nei
    return tips


@new_tips('add_modole')
def add(a, b):
    print(a + b)


@new_tips('sub_modole')
def sub(a, b):
    print(a - b)


print(add(4, 5))
print(sub(5, 6))
