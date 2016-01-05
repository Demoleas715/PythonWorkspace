'''
Created on Oct 30, 2015

@author: Evan
'''
my_d={}

my_d["Mike"] = "Red"
my_d["Iris"] = "Blue"
my_d["Dan"] = "Green"

print(my_d["Iris"])

print(my_d.get("Iris"))

print(my_d.get("Aboudi", "No favorite"))

my_k=list(my_d.keys())

my_k.sort()

for k in my_k:
    print(k+": "+my_d[k])