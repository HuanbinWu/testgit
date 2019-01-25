#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing

#闭包的使用
#闭包的使用
#a*x+b=Y
def a_line(a,b):
    def arg_y(x):
        return a*x+b
    return arg_y
#a=3 b=5
#x=10 y=?

line1=a_line(3,5)
line2=a_line(5,10)
print(line1(10))
print(line1(20))

