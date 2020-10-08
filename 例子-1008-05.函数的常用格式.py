#coding=utf-8
#1.无参数，无返回值
'''
def jia():
    num1=int(input('num1 '))
    num2=int(input('num2 '))
    print(num1+num2)
jia()
'''
#2.无参数，有返回值
'''
def login():
    username=input('用户名: ')
    return username
name=login()
print('your name is %s'% name)
'''
#3.有参数，无返回值
def login1(name,passwd):
    if len(name)>5:
        print('合理')
        if passwd=='12345':
            print('yes')
        else:
            print('密码有误')
    else:
        print('不合理')
        
login1('simida','123456')

#4.有参数，有返回值
def click(name):
    if len(name)!=0:
        return 'sucess!'
    else:
        return 'failed!'
c=click('test')
print(c)





