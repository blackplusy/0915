#coding=utf-8
#字符集 翻译官
#utf-8  国际通用
#GBK2312 汉语
#print()函数可以把内容放在括号中进行输出

#1.直接输出
print('im your baba!!!')
print(250)

#2.变量输出
a=100
print(a)
b=30
print(a+b)

#3.函数输出
#  len()   元素个数
#  abs()   绝对值
print(abs(-10))
print(len('12345'))

#4.格式化输出
#   %d   数值类型数据
#   %s   字符类型数据
name='gaga'
age=20
print('%s 的年龄是 %d'%(name,age))
#print('%s 的年龄是 %d'%(age,name))
#如果需要传入的参数只有一个，可以不加括号
print('%s 很 帅'% name)
