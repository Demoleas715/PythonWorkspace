def read_num_dist(filename): #Opens file and counts the number of times a number is distributed
    text_file=open(filename, "r")
    
    my_dict={} #Dictionary for number of times each number is printed
    
    for c in text_file: #For each number in the text file
        c=int(c)
        count = my_dict.get(c, 0) #Adds the value of c
        count+=1
        my_dict[c] = count
        
    return my_dict

def main():
    my_dict=read_num_dist("num_dist_1.txt")#File to read numbers
    numbers=list(my_dict.keys())
    numbers.sort()#Sorts the numbers in order from least to greatest
    for c in numbers: 
        if my_dict[c]>1: #Checks if it should print time or times
            print("%s: %d times" % (c, my_dict[c]))
        else:
            print("%s: %d time" % (c, my_dict[c]))
            
main()