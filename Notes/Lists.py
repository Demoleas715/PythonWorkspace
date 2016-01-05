'''
Created on Oct 20, 2015

@author: Evan
'''
names=[]

names=input("Give me a list of names on one line")
name_list=names.split()

for n in name_list:
    print(n)

'''
print("Enter a list of names. Leave blank when done.")

n=input()
while n!="":
    names.append(n)
    n=input()
    
names.reverse()

for n in names:
    print(n)
'''