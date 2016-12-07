#!/usr/bin/python

class date():
        def __init__(self):
                self.dd=7;self.mm=10;self.yy=2016
        def __add__(self,date1):
                self.dd=self.dd+date1
                return (self)
        def printvalues(self):
                print self.dd,self.mm,self.yy
today=date()
today+=5
today.printvalues()
