# prime factors  �������

def prime(i):
    #�ж��Ƿ�Ϊ���� ��������1 
    c=2
    a=True
    while c<i/2:
        if i%c==0:
        #�������0 ˵����������
            a=False
        c+=1
    return a
       
a=1
b=int(raw_input('������һ�����֣�'))
#b=13195
while a<b/2:
    if b%a==0:
        if prime(a)==1:
            print 'this is prime factor %d'%a
    a+=1
    
