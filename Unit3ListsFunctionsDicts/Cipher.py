import random

e_dict={} #Global Variable; Encryption dictionary
d_dict={} #Global Variable; Decryption dictionary

def load_cipher_file (filename):
    text_file=open(filename, "r")
    
    for line in text_file:
        line=line.strip().split("\t")
        e_dict[line[0]]=line[1]
        d_dict[line[1]]=line[0]
    return e_dict, d_dict
    """
    Loads a cipher from the specified file.
    This function sets e_dict to encrypt messages and d_dict to decrypt messages.
    """
    
def encrypt_message(e_dict):
    encrypt_message=input("Enter a message to encrypt\n")
    for letter in encrypt_message:
        e_letter=e_dict.get(letter.upper(), letter)
        print(e_letter, end="")
    print("\n\n")
    
    """
    This function asks the user for a message to encrypt.
    It then prints an encrypted version of the method.
    
    It is ok if the user enters characters that are not cyphered, like numbers
    In this case, the character entered by the user will pass directly into
    the output cyphered message without being altered.
    """
    
def decrypt_message(d_dict):
    decrypt_message=input("Enter a message to decrypt")
    for letter in decrypt_message:
        d_letter=d_dict.get(letter.upper(), letter)
        print(d_letter, end="")
    print("\n\n")
    
    """
    This function asks the user for a message to decrypt.
    It then prints the decrypted message.
    If a character in the message is not in the cipher dictionary, print the
    character directly to the output without altering it.
    """
    
def create_key():
    """
    OPTIONAL function -- only create this one once you have completed
    everything else!
    Creates a new random cipher key and prints the key to the console.
    The user needs to copy this key into a file if desired.
    """
    
def main():
    cipher = input("Choose a cipher file to load\n")
    file_name=load_cipher_file(cipher)
    menu=0
    while menu!="Q":
        menu=input("\n\tE - Encrypt a message\n\tD - Decrypt a message\n\tQ - Quit\n\n").upper()
        print()
        if menu=="E":
            encrypt_message(e_dict)
        elif menu=="D":
            decrypt_message(d_dict)
    
    """
    Asks the user which cipher file to load.
    Calls load_cipher_file to load the dictionaries.
    Prints the menu.
    Loops until the user decides to quit.
    Calls encrypt_message and decrypt_message as requested by the user.
    """
    
main()