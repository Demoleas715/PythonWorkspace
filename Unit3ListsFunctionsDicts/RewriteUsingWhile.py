'''
Created on Oct 12, 2015

@author: Evan
'''
i=18
while i>-10: #Start of while loop
    print("%3d" % (i), end=" ")#substitutes new line for a space
    if (i%5==0):
        print() #New line for every 5th number
    i-=2 