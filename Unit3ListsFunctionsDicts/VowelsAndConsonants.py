def consonants (my_str): #find consonants function
    my_str = my_str.upper()
    con_count = 0
    consonants="BCDFGHJKLMNPQRSTVWXYZ" #consonants
    for i in my_str:
        if i in consonants:
            con_count+=1#add 1 consonant to count
    return str(con_count)

def vowels (my_str): #find vowels function
    my_str=my_str.upper()
    vow_count=0
    vowels="AEIOU" #vowels
    for i in my_str:
        if i in vowels:
            vow_count+=1#add 1 vowel to count
    return str(vow_count)

def main ():
    print(consonants("Hello"))
    print(vowels("hello"))
    
main()    