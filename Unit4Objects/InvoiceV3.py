from Items import Invoice, Item

def main():
    print("Welcome!")
    
    invoice=Invoice()
    
    item_name=input("Enter the name of the fisrt item purchased.")
    
    while (len(item_name)>0):
        item_count=int(input("How many " + item_name + " were purchased"))
        item_price=float(input("What was the price for each " +item_name + "? "))
        
        item=Item(item_name, item_count, item_price)
        invoice.addItem(item)
        item_name=input("\nEnter the name of the next item purchased")
        

        
    print ("\n\n%-30s%10s%12s%10s" % ("Item Name", "Cost Each", "Quantity", "Total"))
    
    itemList=invoice.getItems()
    
    for i in itemList:
        print ("\n\n%-30s%10s%12s%10s" % (i.name, i.cost, i.quantity, i.getTotalCost()))
        
    print("\n\nGrand Total: %8.2f" % (invoice.getTotalCost()))
    
main()