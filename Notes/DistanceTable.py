'''
Created on Oct 8, 2015

@author: Evan
'''
m=1
print("%10s %20s" % ("Mile:", "Kilometer:"))
while m<10:
    k=1.609*m
    print("%10d %20f" % (m, k))
    m+=1