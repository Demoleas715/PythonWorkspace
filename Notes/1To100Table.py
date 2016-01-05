'''
Created on Oct 9, 2015

@author: Evan
'''
n=1
while n<=100:
    print("%4d" % (n), end='')
    if (n%10==0):
        print()
    n+=1