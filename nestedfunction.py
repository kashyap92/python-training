#!/usr/bin/python
a,b,c,d=10,20,30,40
def funA():
        a,b,c=12,13,14
        print("IN function A",a,b,c,d)
        def funB():
                a,b,c,d=21,22,23,24
                print("IN Function B",a,b,c,d)
                def funC():
                        b,c,d=32,33,34
                        print("IN function C",a,b,c,d)
                funC()
        funB()
funA()
print ("In main",a,b,c,d)
