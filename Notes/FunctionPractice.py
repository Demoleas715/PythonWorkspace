'''
Created on Oct 19, 2015

@author: Andrew
'''
def max (a, b):
    if (a>b):
        return a
    else:
        return b
def longer(a, b):
    if (len(a)>len(b)):
        return a
    else:
        return b
    
def main():
    print(max(10,5))
    print(max(-6, -7))
    print(max(5, 98))
    print(longer("Happy", "hi"))
main()