'''
Created on Sep 23, 2015

@author: Evan
'''
'''
Created on Sep 18, 2015

@author: Guest
'''
P=float(input("How much money would you like to invest?"))
r=float(input("What percent is the interest rate?"))
t=float(input("How many years will you invest this money?"))
n=float(input("How many times a year will it be compounded?"))
#Inputs for principal, rate, years, and compounds
compoundinterest = P*(1+(r/100)/n)**(n*t)
simpleinterest = P + P*(r/100)*t
#algorithms for interest
conversion=input("Would you like to calculate compound or simple interest")
#Conversion choice
if conversion == "compound":
    print ("Your total is $%s" % round(compoundinterest, 2))
elif conversion =="simple": 
    print ("Your total is $%s" % round(simpleinterest, 2))
#Interest total answer