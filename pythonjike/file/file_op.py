#!/usr/bin/env python
#  _*_ coding:utf-8 _*_
# Author:HuanBing
#将小说的主要人物记录在文件中
# file1=open('name.txt','w')
# # file1.write('诸葛亮')
# # file1.close()
# # file2=open('name.txt')
# # print(file2.read())
# # file2.close()
# # file3=open('name.txt','a')
# # file3.write('刘备')
# # file3.close()
# file4=open('name.txt')
# # print(file4.readline())
# # file4.close()
# # file5=open('name.txt')
# # for line in file5.readlines():
# #     print (line)
# #     print ('********')
file6=open('name.txt')
print('当前文件指针的位置%s' %file6.tell())
print ('当前读取到了一个字符，字符的内容是%s'%file6.read(1))
print('当前文件指针的位置%s'  %file6.tell())
#第一个参数代表便宜位置，第二个参数0 表示从文件开头偏移  1 代表从当前文件偏移， 2 代表结尾
file6.seek(5,0)
print('我们进行了seek的操作' )
print('当前文件指针的位置%s' %file6.tell())
print ('当前读取到了一个字符，字符的内容是%s'%file6.read(1))
print('当前文件指针的位置%s'  %file6.tell())
file6.close()