#!/usr/bin/python
ctr=1
print "Enter <Ctrl>+c to exit"
try:
        while ctr:
                print ctr
except KeyboardInterrupt:
                print "Received Keyboard Interrupt"
                import sys
                sys.exit()
