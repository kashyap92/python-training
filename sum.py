#!/usr/bin/python
def sum(a,b,c=0,d=0):
        """print sum of 2 nos
        and return sum of 2 nos"""
        print a+b+c+d
        print "a",a,"b",b,"c",c,"d",d
        return a+b+c+d
sum(10,20)
sum(10,20.0,30)
sum(10,20,30,40)
sum(b=10,a=34,d=356,c=234)
help(sum)
