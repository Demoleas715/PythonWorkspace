'''
Created on Oct 12, 2015

@author: Evan
'''
print("%-10s %15s" % ("Dollars", "Euros"))
for D in range(25, 500, 75):
    E=D/1.14
    print("%-10d %15.2f" % (D, E))