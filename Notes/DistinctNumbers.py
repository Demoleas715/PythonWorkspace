'''
Created on Oct 22, 2015

@author: Evan
'''
numList=[]

print("Please enter a list of numbers. Leave blank when done.")

num=input()
while num!='':
    num=int(num)
    if num not in numList:
        numList.append(num)
        
    num=input()

numList.sort()

for n in numList:
    print(n, end=" ")
    
print()

print(min(numList))
print(max(numList))
print(len(numList))
