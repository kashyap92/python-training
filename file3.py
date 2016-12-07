#!/usr/bin/python
import sys
file1=open(str(sys.argv[1]),'r')
file2=open(str(sys.argv[2]),'w')
for line in file1:
        file2.write(line)
file1.close
file2.close
