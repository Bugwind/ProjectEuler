def palindromic(a):
    #�ж������Ƿ����
    a=str(a)
    if a==a[::-1]:
        return True
    else:
        return False

    
a=101
lar1=0
lar=0
while a<=999:
    b=101
    while b<=999:
        lar=a*b
       # print lar
        b+=1
        if palindromic(lar):
            if lar>lar1:
                #�ж���֮ǰ���Ĵ�С
                lar1=lar
                #print lar1
    #print a,b
    a+=1
print lar1




    
