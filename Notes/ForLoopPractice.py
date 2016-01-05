'''
Created on Oct 12, 2015

@author: Evan
'''
mystr=input("Please enter a sentence")
spaces=0
vowels=0
mystr=mystr.upper()

for ch in mystr:
    if(ch==" "):
        spaces+=1
        
    elif ch in ('AEIOU'):
        vowels+=1
print("Spaces: ", spaces)
print("Vowels: ", vowels)
