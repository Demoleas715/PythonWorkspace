import math


def read_numbers_from_file(file_name): #File reading function
    text_file=open(file_name, "r")
    
    num_nbrs=int(text_file.readline())
    num_list=[]
    for i in range (0, num_nbrs):
        i=int(i)
        num_list.append(int(text_file.readline()))
    num_list.sort()
    return num_list

'''def read_numbers():
    count=int(input("Enter how many numbers you would like to enter"))
    num=input("Enter your numbers")
    for a in range(1, count+1, 1):
        num=int(num)
        if num not in num_list:
            num_list.append(num)
    
        
        num=input()
    return num_list'''

def get_mean(num_list): #Function that finds the mean
    mean=0
    for n in num_list: #Algorithm for finding the mean
        mean+=n
    mean /= len(num_list)
    return mean
    

def get_range(num_list): #Function that finds the range
    return max(num_list)-min(num_list)

def get_median(num_list): #Function that finds the median
    num_list.sort()
    if len(num_list)%2==0: #If there are an even amount of integers in the list
        median=num_list[len(num_list)//2]
        median=(median+num_list[len(num_list)//2-1])/2
        return median
    else: #If there are an odd number of integers in the list
        median=num_list[len(num_list)//2]
        return median
    
def get_std_dev(num_list): #Function that finds standard deviation
    dev=0
    mean=get_mean(num_list)
    for i in range (0, len(num_list)): #Algorithm for standard deviaton
        dev+=(num_list[i]-mean)**2
    return math.sqrt(dev/len(num_list))
    
'''def get_mode(num_list):
    for i in num_list:
        count=num_list.count(i)
        mode_list=[count]
'''            
    
def main():
    num_list=read_numbers_from_file("test_num_2.txt")
    print("Lists: ", num_list) #List of numbers
    print("Mean: %.2f" % (get_mean(num_list))) #Mean of numbers
    print("Std Dev: %.2f" % (get_std_dev(num_list))) #Standard deviation of numbers
    print("Median: ", get_median(num_list)) #Median of numbers
    print("Min: ", min(num_list)) #Minimum number
    print("Max: ", max(num_list)) #Maximum number
    print("Range: ", get_range(num_list)) #Range of number list
    #print("Mode: ", get_mode(num_list)
     
main()
