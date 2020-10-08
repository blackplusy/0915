#coding=utf-8
#1.实参位置
def info(name,age):
    print('你的名字是%s,你的年龄是%d'%(name,age))
info('lilei',20)
#info(30,'lily')

#2.关键字
def animal(pet1,pet2):
    print(pet1+' 旺！，'+pet2+' miao')
animal(pet2='cat',pet1='keji')

#3.参数默认值
def userinfo(name,minzu='汉'):
    print('您的名字是%s,你的民族是%s'%(name,minzu))

userinfo('o8ma')
userinfo('ladeng','v5er')

#4.不定长参数
def test(x,y,*args):
    print(x,y,args)

test(1,2,'o8ma','ladeng')

def test1(x,y,**args):
    print(x,y,args)

test1(1,2,a=10,b='a')
