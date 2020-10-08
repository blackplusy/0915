#coding=utf-8
import csv
with open('D:\\1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)
        
with open('D:\\2.csv','w') as f:
    file=csv.writer(f,dialect='excel')
    #写入文件常用方式writerow
    file.writerow(['a','b','c','d'])
    #file.writerow([q,w,e,r])
print('OK了')
