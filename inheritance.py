#!/usr/bin/python
#MyMother=mom()
#print id(MyMother)
#help(mom)
#       def talk(self):
#               print "speak softly"
class Dad():
        def talk(self):
                print "speak politely"
        def __init__(self):
                print "Object of class dad constructed"

        def __del__(self):
                print "Object of class Dad destroyed"
class PGM():
        def TalkPGM(self):
                print "tell stories"
        def __init__(self):
                print "Object of class PGM Constructed"
class PGF():
        def TalkPGF(self):
                print "Encourage"
        def Talk(self):
                print "PGF Speaking"
        def __init__(self):
                print "Object of class PGF Constructed"
class MGM():
        def Talk(self):
                print "speak softly"
        def __init__(self):
                print "Object of class MGM constructed"
class MGF():
        def Teach(self):
                print "teach values"
        def __init__(self):
                print "Object of class MGF Constructed"
class mom(MGM,MGF):
        x=10;y=20
        def walk(self):
                print "walk Elegantly"
                print id(self)
        def sum(self,a,b):
                return(a+b+self.x+self.y)
        def __init__(self):
                print "Object of class Mom"

class infant(mom,Dad):
        pass
Baby=infant()
print dir(Baby)
Baby.walk()
Baby.talk()
print Baby.sum(10,20)
