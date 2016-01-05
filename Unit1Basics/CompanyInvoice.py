'''
Created on Sep 27, 2015

@author: Evan
'''
item1=input('What is the first item you would like?')

quantity1=int(input('How much ' + item1 +' would you like?'))

ppi1=float(input("How much is the price per " + item1 + '?'))
#First item, price, and quantity
item2=input('What is the second item you would like?')

quantity2=int(input('How much ' + item2 + ' would you like?'))

ppi2=float(input('How much is the price per ' + item2 + '?'))
#Second item, price, and quantity
totalcost1=ppi1*quantity1
totalcost2=ppi2*quantity2
#Total cost of item 1 and 2
print("Item 1:")

print('%7s%1d %2s, $%2.2f %2s' % (' ', quantity1, item1, ppi1, 'each'))

print('%18s $%2.2f' % ('Total Cost:', totalcost1))
#Format for first item, quantity, and price
print("Item 2:")

print('%7s%1d %2s, $%2.2f %2s' % (' ', quantity2, item2, ppi2, 'each'))

print('%18s $%2.2f' % ('Total Cost:', totalcost2))
#format for second item, quantity, and price