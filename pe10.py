#coding:utf-8

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

sum=1
i=1
while i<2000000:
    if prime(i)==1:
        #print i
        sum+=i
    i+=2
print sum    
