#!/usr/bin/python

lst=(10,20)
print (type (lst))
def incr(a):
        ctr=0
        while ctr < len(a):
                a[ctr]+=1
                ctr+=1
incr(lst)
print(lst)
