#coding=utf-8
dic={'name':'heygor','age':18}
dic1={'name':'gaga'}
#直接访问
print(dic)
#数据筛选
print(dic['age'])
#del删除字典
dic={'name':'heygor','age':18}

del dic['name']
print(dic)
del dic
#print(dic)
#clear清空字典
dic={'name':'heygor','age':18}
dic.clear()
print(dic)

#字典的修改
dic={'name':'heygor','age':18}
dic['name']='gaga'
print(dic)

#keys
dic={'name':'heygor','age':18}
print(dic.keys())
for i in dic.keys():
    print(i)

#values
dic={'name':'heygor','age':18}
for i in dic.values():
    print(i)

#items
dic={'name':'heygor','age':18}
print(dic.items())
for key,values in dic.items():
    print(str(key)+'-'+str(values))






