#!/usr/bin/python
import sys
sys.setrecursionlimit(2147483647)
n=input("enter the number:")
def fact(a):
        if a == 1 :
                return 1
        else :
                return a*fact(a-1)

#       ctr=0
#       if a < ctr:
#       ans = a * fact(a-1)
#       a-=1
#       return ans
fa=fact(n)
print fa
