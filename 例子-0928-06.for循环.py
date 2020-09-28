#coding=utf-8

#字符串
for i in 'abc':
    print(i)

#列表
l1=[1,2,'simida','ouba~']
for a in l1:
    print(a)

#函数
#内置函数range()
#range(10)   0-9
#range(1,10) 1-9

for i in range(1,10):
    #print(i)
    print(i*'*')

for u in range(-5,5):
    #print(u)
    if u<0:
        print(abs(u))
    else:
        print(u)
