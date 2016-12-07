#!/usr/bin/python
import sys
class date():
        #date;month;year
        def date1(self,datei):
                list=(datei.split('-'))
                #if list[0] > 30 :
                        #list[0]=(list[0])%30
                #       list[1]+=1
                #print list
                #print list[0]
                list[0]=int(list[0])+30
                if list[0] > 30:
                        list[0]=int(list[0])%30
                        list[1]=str('november')
                        #list[1]=int(list[1])+1
                        print list
                else:
                        print list

today=date()
today.date1('7-October-2016')
