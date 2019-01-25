#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
#装饰器的定义
import  time
# print(time.time())
# time.sleep(3)


def timer(func):
    def wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('运行时间是%s秒'%(stop_time-start_time))

    return wrapper
@timer
def i_can_sleep():
    time.sleep(3)

# start_time=time.time()
i_can_sleep()
# stop_time=time.time()
# print('函数运行了%s秒。'%(stop_time-start_time))
