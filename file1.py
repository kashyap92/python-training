#!/usr/bin/python
import sys
#file=raw_input("enter the file name:")
#filename=sys.argv[0]
#file=str(sys.argv[1])
file1=open(str(sys.argv[1]))
lines=file1.readline()
a=1
while lines:
        print a,lines
        lines=file1.readline()
        a+=1
file1.close()
