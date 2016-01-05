def func_b(a):
    a.append(5)

def main():
    my_list=[]
    my_list.append("a")
    
    func_b(my_list)
    print("my_list=", my_list)
    
main()
