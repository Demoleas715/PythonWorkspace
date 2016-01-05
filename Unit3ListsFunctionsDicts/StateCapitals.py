import random

#Dictionary of the valid quizzes available to the user
#The key is the label and the value is the data file name.
data_files={"East": "states_east.txt", #Dictionary of regions and data files
            "West": "states_west.txt",
            "South": "states_south.txt",
            "Central": "states_central.txt",
            "All": "states_all.txt"
            }

def read_states_into_dict(filename): #creating dictionary function'
    text_file=open(filename, "r")
    
    my_dict={}#Dictionary of states
    
    for line in text_file:
        line=line.strip().split("\t")
        my_dict[line[0]] = line[1]
        #Takes all the states and capitals and creates dictionaries
    return my_dict    
        
    
    
    """
    Loads the specified text file.
    There is one State / Capital combination per line.
    the state capital are separated by the tab character.
    
    Hint: It is advisable to call strip() on the capital string prior to adding
    it to the dictionary to remove the new line character.
    """

def quiz(my_dict): #Quiz function
    states=list(my_dict.keys()) #States is equal to a list of the dictionary of states
    statelen=len(states)
    count=0
    while len(states)!=0: #Continues game until there are no remaining states
        state=random.choice(states) #Random state choice
        answer = input("\nWhat is the capital of " + state + "? ")
        if answer.title() == my_dict.get(state, 0):
            print("Correct")
            states.remove(state) #Removes correct states from the list
            count+=1 #Adds one guess
        elif answer.title()=="Quit": #Allows user to quit early
            break
        else:
            print("Incorrect! The capital is " +my_dict.get(state)) #If user gets answer wrong
            count+=1
    if answer!="Quit":
        print("Wow! You got all " +str(statelen)+ " correct in " + str(count) + " guesses!")
            
    """This method implements a loop that will continue to quiz the user until the user types
    "quit" or correctly identifies all of the capitals in the list.
    
    Each time the user identifies a capital, it is removed from the list.
    
    At the end, the function will report how many guesses were required by the user.
    """
    
def get_data_file_choice():
    region=input("Which data file would you like to load?\nSouth All West Central East\n").title() #Asks user which region that would like to choose
    while region not in "SouthEastWestCentralAll": #Makes sure region is an option
        print("Invalid option, try again!!")
        region=input("Which data file would you like to load?\nSouth All West Central East\n").title()
    print("Let's begin the quiz. Once you get a state correct, I will remove it from the list.\nLet's play until you get them all correct. Or, if you grow tired, enter quit to exit at any time.\nGood luck!")
    return data_files[region]
        
    """
    Asks the user to select a data file to use for the quiz.
    The function makes sure the user makes a valid selection.
    The function returns the filename selected by the user.
    """

def main():
    file_name=get_data_file_choice()
    my_dict = read_states_into_dict (file_name)
    quiz(my_dict)

main()