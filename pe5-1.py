# -*- coding: utf-8 -*-

#求解最大公因数
def gcd(a,b):
    if a>b:
        a,b=b,a
       # print a,b,'hi'
    a,b=b%a,a
   # print a,b
    while a!=0:
       a,b=gcd(a,b)
    return a,b
#公倍数
def lcm(a,b):
    return (a*b)/gcd(a,b)[1]

re=1
for i in range(1,20):
    re=lcm(re,i+1)
    i+=1

print re
