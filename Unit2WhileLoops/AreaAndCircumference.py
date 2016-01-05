'''
Created on Oct 8, 2015

@author: Evan
'''

print("%6s %13s %10s" % ("Radius", "Circumference", "Area"))#heading

def find_circumference(radius):#circumference function
    circumference=2*radius*3.14
    return circumference
def find_area(radius):#area function
    area=(radius**2)*3.14
    return area


def main():
    for r in range (2, 51, 4):#Table
        print("%6d %13.1f %10.2f" % (r, find_circumference(r), find_area(r)))

main()