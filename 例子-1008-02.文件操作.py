#coding=utf-8

file=open('D:\\3.txt','r',encoding='utf8')
for i in file.readlines():
    #print(i)
    #print(type(i))
    i=i.strip('\n')
    a=i.split(' ')
    if a[-1]=='110':
        print('tel is here!!')
    #print(a)
file.close()
