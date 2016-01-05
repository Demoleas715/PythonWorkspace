'''
Created on Oct 6, 2015

@author: Evan
'''
import random
#random number import
cscore=0
pscore=0
#score start
while cscore<5 and pscore<5: #Loop until computer or player score reaches 5
    comp=random.randint(1,3) #Random number range
    choice=input("Please choose 'r'ock, 'p'aper, or 's'cissors\n") #Choice
    if comp==1: #Computer choice rock
        if choice=="r":
            print("Draw. You chose rock. The computer chose rock\n")#Player choice rock
        elif choice=="p":
            print("You won. You chose paper. The computer chose rock\n")#Player choice paper
            pscore+=1 #Adds score to player
        elif choice=="s":
            print("You lost. You chose scissors. The computer chose rock\n")#Player choice scissors
            cscore+=1 #Adds score to computer
        else:
            print("ERROR! Please choose again.\n")
    if comp==2: #Computer choice paper
        if choice=="r":
            print("You lost. You chose rock. Computer chose paper.\n")#Player choice rock
            cscore+=1
        elif choice=="p":
            print("Draw. You chose paper. Computer chose paper.\n")#Player choice paper
        elif choice=="s":
            print("You won. You chose scissors. Computer chose paper.\n")#Player choice scissors
            pscore+=1
        else:
            print("ERROR! Please chose again.\n")
    if comp==3: #Computer choice scissors
        if choice=="r":
            print("You win. You chose rock. Computer chose scissors.\n")#Player choice rock
            pscore+=1
        elif choice=="p":
            print("You lost. You chose paper. Computer chose scissors.\n")#Player choice paper
            cscore+=1
        elif choice=="s":
            print("Draw. You chose scissors. Computer chose scissors.\n")#Player choice scissors
        else:
            print("ERROR! Please chose again.\n")
    print("The score is now:\n You: " +str(pscore)+"\nComputer: " +str(cscore)+ '\n')#Score after each round
if cscore==5:
    print("The computer won!")
#Checks who won and prints it
elif pscore==5:
    print("You won!")