#coding=utf-8
#菱形
'''
for i in range(-3,4):
    #print(i)
    if i<0:
        a=-i
    else:
        a=i
    print(' '*a+'*'*(7-a*2))
'''
#对顶三角
'''
n=7
e=n//2   #3
for i in range(-e,n-e):#-3,4
    a=-i if i<0 else i
    print(' '*(e-a)+'*'*(2*a+1))
'''
#乘法表
#格式化输出 end表示不换行

for i in range(1,10):
    #print(i)
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end=" ")
    print()
