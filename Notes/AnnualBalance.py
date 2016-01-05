'''
Created on Oct 9, 2015

@author: Evan
'''
print("%-6s %10s %10s" % ("Year", "Interest", "Balance"))
y=1
rate=0.0875
balance=900
while y<=30:
    interest=balance*rate
    balance+=interest
    print("%-6d %10.2f %10.2f" % (y, interest, balance))
    y+=1