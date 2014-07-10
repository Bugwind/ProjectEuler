#coding:utf-8

def step(a):
    if a%2==0:
        a=a/2  
    else:
        a=3*a+1
    return a

def judge(b):
    i=1
    while 1:
        if b!=1:
            b=step(b)
            i+=1
        else:
            break
    return i

#print judge(13)


g = (x for x in range(1000000))

max=1
s=0
g.next()
while 1:
    try:
        b=g.next()
    except StopIteration:
        break
    a=judge(b)
#    print b,'step is ',a
    if a>max:
        s=b
        max=a
        #print max,'max',s

print s,'step is',max
        

