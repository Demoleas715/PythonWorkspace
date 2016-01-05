a=int(input("Enter a number from 0 to 9"))
while 0>a or a>9:
    a=int(input("Enter a number from 0 to 9"))

b=int(input("Enter a number between " + str(a) + " and 100"))
while a>=b or b>=100:
    b=int(input("Enter a number between " + str(a) + " and 100"))

mySum=0

while a<=b:
    mySum += a
    a+= 1
print(mySum)