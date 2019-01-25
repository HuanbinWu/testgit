#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing
#记录生肖，根据用户输入的年份判断生肖
chinese_zodiac="猴雞狗豬鼠牛虎兔龍蛇馬羊"
#print (chinese_zodiac[0:4])
#print (chinese_zodiac[-1])
year=2018
print(year%12)
print (chinese_zodiac[year%12])
print('狗' not in chinese_zodiac)
print(chinese_zodiac+chinese_zodiac)
print (chinese_zodiac+'abc')
print(chinese_zodiac*3)