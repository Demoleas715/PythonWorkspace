next_calc="y"


while next_calc=="y": # loops until the user decides to exit
    statement=input("Enter your statement to be evaluated. ") # Statement input

    statement=statement.strip().split(" ") # Splits the statement by spaces

    if statement[1]=="+" or "-" or "/" or "*": # Decides if the operator is valid
        if statement[1]=="+": #If the operator is addition
            answer = float(statement[0])+float(statement[2]) #Adds numbers
            print("Result: " + str(answer))

        if statement[1]=="-": #If the operator is subtraction
            answer=float(statement[0])-float(statement[2]) #Subtracts numbers
            print("Result: " + str(answer)) #Prints result

        if statement[1]=="/": #If the operator is division
            if statement[2]=="0": #Checks if divided by 0
                print("Error: Division by 0") #Prints error message 
            else:
                answer=float(statement[0])/float(statement[2]) #Divides numbers
                print("Result: " + str(answer)) #Prints answer
        if statement[1]=="*": #If the operator is multiplication
            answer=float(statement[0])*float(statement[2]) #Multiplies numbers
            print("Result: " + str(answer)) #Prints answer
    else:
        print("Error invalid operator")#Print statement if operator is invalid

    next_calc=input("Would you like to perform another calculation? (y/n) ") #Asks user if they would like to perform another calculation

