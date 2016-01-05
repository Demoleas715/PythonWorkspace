p=float(0.01)
n=float(0.05)
d=float(0.10)
q=float(0.25)
#Value of coins
principal=float(input('How much money is in the piggy bank so far?'))
coin=input('\t(p) - Deposit a penny\n\t(n) - Deposit a nickel\n\t(d) - Deposit a dime\n\t(q) - Deposit a quarter\n\t(e) - Exit program and give balance')
#input for principal and first coin to add
while(coin!='e'):
#Loops coin select
    if coin=='p':
        principal=principal+p
        print('You deposited a penny!')
    elif coin=='n':
        principal=principal+n
        print('You deposited a nickel!')
    elif coin=='d':
        principal=principal+d
        print('You deposited a dime!')
    elif coin=='q':
        principal=principal+q
        print('You deposited a quarter!')
    else:
        print("Invalid Option\n\t(p) - Deposit a penny\n\t(n) - Deposit a nickel\n\t(d) - Deposit a dime\n\t(q) - Deposit a quarter\n\t(e) - Exit program and give balance")
#Error statement for unkown coin select
    coin=input('Select a coin to add')
#Coin select input
print("$%0.2f" % (principal))
#Final balance
input("Hit enter to exit")