'''
Created on Oct 12, 2015

@author: Evan
'''
import math

print("%-10s%16s%16s" % ("Radius", "Circumference", "Area")) #Heading

for r in range(2, 18, 3):#Beginning of for loop
    c=r*2*math.pi
    a=r**2*math.pi
    #Circumference and area equations
    print("%-10d%16.1f%16.2f" % (r, c, a))
