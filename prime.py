#!/usr/bin/python
i=2
prime=1
while i < 100 :
        j=2
        while j < i/2 :
                if i%j == 0:
                        isprime=0
                        j+=1
                        break
                else:
                        j+=1
        if prime == 1 :
                print i
                i+=i
