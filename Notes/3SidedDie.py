'''
Created on Sep 24, 2015

@author: Evan
'''
import random
die = random.randint (1,10)
tries=0
while die != 1:
    print('You rolled a', die)
    die = random.randint (1,10)
    tries+=1

print('You rolled a 1!')
print('It took %d tries' % (tries))