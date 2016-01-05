num=[]
num=input("Input numbers on one line")
num_list=num.split()

for i in range (0, len(num_list)):
    num_list[i] = int(num_list[i])
    
num_list.sort()

print(num_list)
    
