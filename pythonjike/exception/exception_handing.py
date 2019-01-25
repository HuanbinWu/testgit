#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing

#异常的检测和处理
# i=j
# print())
# a='123'
# # # print(a[3])
# d={'a':1,'b':2}
# print(d['3'])
# try:
#     year=int(input('input year:'))
# except ValueError:
# #     print('年份要输入数字')
# a=123
# a.append()
# except {ValueError,AttributeError,KeyError}
# try:
# #     print(1/0)
# # except Exception as e:
# #     print('%s' %e)
# # try:
# #     raise  NameError('helleError')
# # except NameError:
# #     print('my custon error')
try:
    a=open('weapon.txt')
    a.writelines('青龙偃月刀')
except Exception as e:
    print(e)
finally:
    a.close()
