'''
Created on Oct 15, 2015

@author: Evan
'''
def f(x):
    return 2*x-3
    
def g(x):
    return x**2-1
    

'''def h(x, y):
    return x*y+1
    
def triangle_area(b, h):
    return 1/2*b*h
    
def celsius_to_fahrenheit(c):
    return 9/5*c+32

def sum_of_digits(num):
    s=str(num)
    total = 0
    for c in s:
        t=int (c)
        total+=t
    return total

def sum_of_digits2(num):
    total=0
    while num>0:
        digit = num % 10
        total += digit
        num = num // 10
        return total'''
    
def main():
    '''a = f(4)
    print(a)
    b=triangle_area(5, 10)
    print(b)
    fehr=celsius_to_fahrenheit(100)
    print(fehr)
    
    print(sum_of_digits(547))
    print(sum_of_digits2(547))'''
    
    for x in range (0, 21, 2):
        print("%5d %5d %5d" % (x, f(x), g(x)))
    

main()
