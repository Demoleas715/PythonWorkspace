'''
Created on Oct 12, 2015

@author: Evan
'''
x=78
while x>=50:
    print(x, end='')
    if x%10==0:
        print()
    else:
        print(end=',')
    x-=2
    
for i in range(78, 49, -2):
    print(i, end="")
    if i%10==0:
        print()
    else:
        print(end=',')