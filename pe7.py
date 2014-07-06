#coding:utf-8

''' Project Euler 7'''

#判断是否是质数

def prime(a):
    i=2
    res=True
    while i<=a/2:
       # print a%i
        if a%i==0:
            res=False
            break
        i+=1
    return res


i=1
a=1
while a<10001:
    i+=2
    if  prime(i)==1:
       a+=1
       #print a,i
    
print i
