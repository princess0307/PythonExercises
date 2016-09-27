
from sys import argv
script, filename=argv
t=open(filename,'w+')
print t.read()
t.truncate()
print "now we will write to the file"
a=raw_input("enter first line")
t.write(a)
b=raw_input("enter second line")
t.write(b)
t.close()
t1=open(filename,'r')
print t1.read()
print "fgr"
