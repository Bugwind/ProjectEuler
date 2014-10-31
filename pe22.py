names=open('p022_names.txt').readline().replace('"','').split(',')
names.sort()
print sum( sum(map(lambda c: ord(c)-64,names[i]))*(i+1) for i in range(len(names)))
