a=1
b=2500

while 1:
    while b%a==0:
        a+=1
    a=a-1
    #print b
    if a==17:
        print 'this is %d'%b
        break
    if a==20:
        print 'this is %d'%b
        break
    a=1
    b+=1
    #print b
