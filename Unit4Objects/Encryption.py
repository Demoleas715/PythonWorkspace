from Encryptor import Encryptor

def main():
    file_name=input("Choose a file to load: ")
    encryptor=Encryptor(file_name)
    menu=0
    while menu!="Q":
        menu=input("\n\tE - Encrypt a message\n\tD - Decrypt a message\n\tQ - Quit\n\n").upper()
        print()
        if menu=="E":
            msg=input("Enter a message to encrypt: ")
            print(encryptor.encryptMessage(msg))
        elif menu=="D":
            msg=input("Enter a message to decrypt: ")
            print(encryptor.decryptMessage(msg))
main()
