'''
Created on Oct 12, 2015

@author: Evan
'''
print("%-10s %-14s %10s %10s" % ("Miles", "Kilometers", "Kilometers", "Miles"))
m=-1
kilometers=15
while m<19 and kilometers<65:
    m+=2
    kilometers+=5
    k=1.609*m
    miles=.621371*kilometers
    print("%-10d %-14.3f %10d %10.2f" % (m, k, kilometers, miles))