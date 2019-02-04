#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
#类的使用，自定义with语句
class Testwith():
    def __enter__(self):
        print('run')
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has error %s'%exc_tb)

with Testwith():
    print('Test is running')
    raise NameError('testNameError')


