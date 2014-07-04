a,b=1,2
sum=2
while b<4000000:
    a,b=b,a+b
    if b>4000000:
        break
    if b%2==0:
        sum+=b
    print a,b
print sum
