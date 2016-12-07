#!/usr/bin/python
day=raw_input("Enter the day of the week:")
if day == 'Saturday' or day =='saturday':
        print " 9 to 1"
elif day == 'Sunday' or day =='sunday':
        print "holiday"
elif day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' :
        print "9 to 6"
else :
        print "Enter the correct day you IDIOT."
