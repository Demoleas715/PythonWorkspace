# Assignment 1.3

def main():
    print ("This program will help to calculate the customer's invoice.\n")
    
    # Gather the input about the 1st item
    item1_name = input ("Please enter the name of the first item purchased. ")
    item1_count = int(input ("How many were purchased? "))
    item1_price = float(input ("What was the price for each one? "))
    
    # Gather the input about the 2nd item
    item2_name = input ("\n\nPlease enter the name of the second item purchased. ")
    item2_count = int(input ("How many were purchased? "))
    item2_price = float(input ("What was the price for each one? "))
    
    # Calculations
    item1_total = item1_count * item1_price
    item2_total = item2_count * item2_price
    grand_total = item1_total + item2_total
    
    # Print out the 1st item
    print ("Item 1:")
    print ("\t" + str(item1_count) + " " + item1_name + ", $" + str(item1_price) + " each")
    print ("\tTotal Cost: $"+ str(item1_total))
    
    # Print out the 2nd item
    print ("\nItem 2:")
    print ("\t" + str(item2_count) + " " + item2_name + ", $" + str(item2_price) + " each")
    print ("\tTotal Cost: $"+ str(item2_total))
    
    # Grand total and exit       
    print ("\nGrand Total: $" + str(grand_total))
    
    input ("Press <enter> to exit");


main()