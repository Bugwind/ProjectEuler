def adddivisor(n):
    a=1
    b=0
    while a <= n/2:
        if n%a==0:
            b+=a
          #  print a
        a+=1
    return b

s=set()
for i in range(1,10000):

    m=adddivisor(i)
    
    n=adddivisor(m)
    
    if (m!=n)and(i==n):
       
        s.add(m)
        s.add(n)
print sum(s)

