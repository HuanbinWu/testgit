#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author:HuanBing

#面向过程编程
# user1={'name':'tom','hp':100}
# user2={'name':'jerry','hp':100}
# def print_role(rolename):
#     print('name is %s ,hp is %s'%(rolename['name'],rolename['hp']))
# 
# print_role(user1)
#面向对象编程
class Player():#定义一个类
    def __init__(self,name,hp,occu):
        self.__name=name  #在类前加__就不能让实例访问到，如果想要访问只能用方法
        self.hp=hp  
        self.occu=occu
    def print_role(self):#定义一个方法
        print('%s:%s %s'%(self.__name,self.hp,self.occu))
    def updateName(self,nawname):
        self.name=nawname

#猫科动物--》》#猫
class Monster():
    '定义怪物类'
    def __init__(self,hp=100):
        self.hp=hp
    def run(self):
        print('移动到某个位置')
    def whoam(self):
        print('我是怪物他爸')
    
class Animals(Monster):
    '普通的怪物'
    def  __init__(self,hp=10):
        super().__init__(hp)

   
class Boss(Monster):
    'Boss类怪物'
    def  __init__(self,hp=1000):
        super().__init__(hp)
    def whoami(self):
        print('我是怪物你是谁？')

a1 =Monster(200)
print(a1.hp)
print (a1.run())
a2=Animals(1)
print(a2.hp)
print (a2.run())
a3=Boss(800)
a3.whoami() #多态
#判断谁是谁的子类 可以获得对象是属于哪个类的
print('a1的类型%s'%type(a1))
print('a2的类型%s'%type(a2))
print('a3的类型%s'%type(a3))
#判断a2是不是Monster(a1)子类
print(isinstance(a2,Monster))



# user1=Player('tom',100,'war')#类的实例化
# user2=Player('jerry',110,'master')
# user1.print_role()
# user2.print_role()
#
# user1.updateName('wilson')
# user1.print_role()
# user1.__name=('ggggggg')
# user1.print_role()
#
