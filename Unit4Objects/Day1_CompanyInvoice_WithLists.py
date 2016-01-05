



def main ():    
    item_names = []
    item_prices = []
    item_counts = []
    grandtotal = 0
    
    print ("This program will help to calculate the customer's invoice.\n")

    item_name = input ("Enter the name of the first item purchased.")
    
    while (len(item_name) > 0):
        item_names.append (item_name);
        item_counts.append(int(input ("How many " + item_name + " were purchased? ")))
        item_prices.append(float(input ("What was the price for each " + item_name + "? ")))
                
        item_name = input("\nEnter the name of the next item purchased.  (Press enter when done.)")
        
    print ("\n\n%-30s%10s%12s%10s" % ("Item Name", "Cost Each", "Quantity", "Total"))

#    for i in range (0, len(item_names)):
#        ... Add more code here ...
    for i in range (0, len(item_names)):
        itemName=item_names[i]
        itemCount=item_counts[i]
        itemPrice=item_prices[i]
        itemTotal=itemCount*itemPrice
        
        print ("%-30s%10.2f%12d%10.2f" % (itemName, itemCount, itemPrice, itemTotal))
        
        #Grand total and exit       
    print ("\n\tGrand Total: $%.2f" % (grandtotal))


main()