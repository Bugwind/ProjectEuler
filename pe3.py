# prime factors  求解质数

def prime(i):
    #判断是否为质数 质数返回1 
    c=2
    a=True
    while c<i/2:
        if i%c==0:
        #如果等于0 说明不是质数
            a=False
        c+=1
    return a
       
a=1
b=int(raw_input('请输入一个数字：'))
#b=13195
while a<b/2:
    if b%a==0:
        if prime(a)==1:
            print 'this is prime factor %d'%a
    a+=1
    
