'''
Created on Sep 29, 2015

@author: Evan
'''
import random
number=random.randint(0, 100)

guess=int(input('Guess a number from 0 to 100'))
guesscount=1
while guesscount<10:
    if (guess>number):
        guess=int(input('Too high! Guess again.'))
    elif (guess<number):
        guess=int(input('Too low! Guess again.'))
    elif (guess==number):
        break
    guesscount+=1
if guess==number:
    print('Correct, you guessed the number in ' + str(guesscount) + ' guesses!')
if guess!=number:
    print("You lose! Try again!")