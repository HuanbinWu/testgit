#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing

#上下文管理器
fd=open('name.txt')
try:
    for line in fd:
        print(line)
finally:
  fd.close()

with open('name.txt') as  f:
    for line in f:
        print(line)

