'''
Created on Oct 12, 2015

@author: Evan
'''
D=25
print("%-10s %15s" % ("Dollars", "Euros"))
while D<500:
    E=D/1.14
    print("%-10d %15.2f" % (D, E))
    D+=75