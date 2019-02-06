#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
from threading import Thread, current_thread
import time
import random
from queue import Queue
queue = Queue(5)  # 定义队列长度5
# 生产者可以随机得一个休眠时间往队列添加数字


class ProduceThread(Thread):
    def run(self):
        name = current_thread().getName()  # 获取到了线程得名字
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)  # 随机选择一个数字
            queue.put(num)  # 通过这个放入指定队列中
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒' % (name, t))

# 消费者可以随机得一个休眠时间从队列得到一个数字
# 里面已经封装好了线程等待以及同步得代码


class ConsumerTheard(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()  # 里面已经封装好了线程等待以及同步得代码
            print('消费者 %s 消耗了数据 %s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 睡眠了%s秒' % (name, t))


p1 = ProduceThread(name='p1')
p1.start()
p2 = ProduceThread(name='p2')
p2.start()
p3 = ProduceThread(name='p3')
p3.start()
c1 = ConsumerTheard(name='c1')
c1.start()
c2 = ConsumerTheard(name='c2')
c2.start()
#生产者多余消费者