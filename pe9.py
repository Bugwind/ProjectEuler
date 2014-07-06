#coding:utf-8

for a in range(501):
    for b in range(501):
        c=a**2+b**2
        if c==(1000-a-b)**2:
            print a*b*(1000-a-b)
        b+=1
    a+=1
