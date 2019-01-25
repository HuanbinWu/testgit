#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing


#函数基本操作
# print('abc',end='\n\n')
# print('abc')
# def func(a,b,c):
#     print('a=%s'%a)
#     print('b=%s' %b)
#     print('c=%s' %c)
# func(1.c=3)



#取得参数个数
# def howlong(first,*other):
#     print(1+len(other))
# howlong(123,234,456)


#函数作用域
# var1=123
#
# def func():
#     #定义全局变量var1
#     global var1
#     var1=1233
#     print(var1)
#
# func()
# print(var1)

#iter() next()
# list1=[1,3,4]
# # # it=iter(list1)
# # # print(next(it))
# # # print(next(it))
# # # print(next(it))
# # # print(next(it))

# for i in range(10,20,2):
#     print(i)


#生成器，是迭代器的一种，自定义
# def frange(start,stop,step):
#     x=start
#     while x<stop:
#         yield x
#         x+=step
# for i in frange(10,20,0.5):
#     print(i)

#lambda 表达式
# def true():return True
# lambda :True
#
# def add(x,y):return x+y
# lambda x,y:x+y
#
# print(add(3,5))

# lambda  x:x<=(month,day)
# def func1(x):
#     return x<(month,day)

# lambda  item:item[1]
# def func2(item):
#     return item[1]
# adict={'a':'aa','b':'bb','c':'cc'}
# for i in adict.items():
#     print(func2(i))


 # filter() map() reduce() zip()

# a=[1,2,3,4,5,6,7]
# b=list(filter(lambda  x:x>2,a))
# print(b)
# a=[1,2,3,4,5]
# b=[2,3,4,5,6]
# c=list(map(lanbda x,y:x+y,a,b)
# print(c)
#
# >>> from functools import reduce
# >>> reduce(lambda x,y:x+y,[2,3,4],1)
# 10
# >>> 1+2+3+4
# 10

# for i in zip((1, 2, 3), (4, 5, 6)):
#         print(i)
#对调
# dicta={'a':'aa','b':'bb'}
# dictb=dict(zip(dicta.values(),dicta.keys()))
# print(dictb)


#
# print((type(num2)))def func():
# #     a=1
# #     b=2
# #     return a+b
# # #闭包
# # def sum(a):
# #     def add(b):
# #         return a+b
# #     return add
# #
# # #add函数名称或函数的引用
# # #add()函数的调用
# # num1=func()
# # num2=sum(2)
# # print(num2(4))
# # # print(type(num1))

