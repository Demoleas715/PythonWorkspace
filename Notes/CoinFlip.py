'''
Created on Oct 1, 2015

@author: Evan
'''
import random

COINS = ["", "H", "T"]

HEADS = 0
TAILS = 1
counter=0
heads=0
tails=0
tailsChain=0
headsChain=0

while counter<1000 and tailsChain<5 and headsChain<5:
    coin=random.randint(0,1)
    print(COINS[coin], end="")
    counter+=1
    
    if coin == HEADS:
        heads+=1
        headsChain +=1
        tailsChain=0
    elif coin == TAILS:
        tails+=1
        tailsChain +=1
        headsChain =0
        
print("\nHeads: ", heads)
print("Tails: ", tails)

