# This is first problem of Project Euler
a=raw_input('����һ����Ȼ����')
a=int(a)
i=1
sum=0
while i<a:
    if i%3==0 or i%5==0:
      # print i
       sum+=i
    i+=1
print sum
