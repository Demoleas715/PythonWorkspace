
text_file=open("word_list.txt", "r")

my_list=[]

for line in text_file:
    my_list += line.split()
    
my_list.sort()

for w in my_list:
    print(w)
    