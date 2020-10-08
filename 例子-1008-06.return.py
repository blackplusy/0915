#coding=utf-8
#1.一个返回值
def sum(a,b):
    jisuan=a+b
    return jisuan
s=sum(20,30)
print(s)
#2.多个返回值
def ret(a,b):
    a*=10
    b*=100
    return a,b
num=ret(3,7)
print(num)
print(type(num))

num1,num2=ret(20,30)
print(num1,num2)
