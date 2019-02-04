#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
#面向对象，主线程在后面显示
import  threading
from threading import  current_thread
class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        print(current_thread().getName(),'stop')

t1=Mythread()
t1.start()
t1.join()

print((current_thread().getName(),'end'))
