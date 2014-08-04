import os

a=raw_input('please input the file name which has been added:')
b='git add %s'%a
#print b
c=raw_input('please add commit:')
d="git commit -m '%s'"%c
print d

os.system(b)
os.system(d)
os.system('git push')
