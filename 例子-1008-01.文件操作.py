#coding=utf-8
#定义一个变量接受open函数打开文件后的内容
file=open('D:\\1.txt','r')
print(file)
for i in file:
    print(i)
file.close()

#写文件
'''
str1='oh my dear baby!'
file=open('D:\\2.txt','w')
file.write(str1)
file.close()
print('数据已经写入')
'''
#追加
file=open('D:\\2.txt','a')
file.write('come on baby!! \n')
file.close()
print('执行完毕')
