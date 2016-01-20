from Encryptor import Encryptor
import tkinter

class Application(tkinter.Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.load_file = tkinter.StringVar()
        self.load_file.set(None)

        tkinter.Label(self, text="Choose a file to load:").grid(row=0, column=0, sticky=tkinter.W)
        tkinter.Radiobutton(self, text="Cipher1.txt", variable=self.load_file, value="cipher1.txt", command=self.load_cipher).grid(row=1, column=0, sticky=tkinter.W)
        tkinter.Radiobutton(self, text="Cipher2.txt", variable=self.load_file, value="cipher2.txt", command=self.load_cipher).grid(row=1, column=1, sticky=tkinter.W)

        tkinter.Label(self, text="Enter the message:").grid(row=2, column=0, sticky=tkinter.W)
        self.msg=tkinter.Text(self, width=100, height=10, wrap=tkinter.WORD)
        self.msg.grid(row=3, column=0, columnspan=3, sticky=tkinter.W)

        tkinter.Button(self, text="Encrypt Message", command=self.encrypt_message).grid(row=4, column=0, sticky=tkinter.E)
        tkinter.Button(self, text="Decrypt Message", command=self.decrypt_message).grid(row=4, column=1, sticky=tkinter.E)

        tkinter.Label(self, text="Out:").grid(row=5, column=0, sticky=tkinter.W)
        self.out_msg=tkinter.Text(self, width=100, height=15, wrap=tkinter.WORD)
        self.out_msg.grid(row=6, column=0, columnspan=3, sticky=tkinter.W)

    def load_cipher(self):
        self.e = Encryptor(self.load_file.get())

    def encrypt_message(self):
        msg = self.msg.get(0.0, tkinter.END)
        encrypt = self.e.encrypt_message(msg)

        self.out_msg.delete(0.0, tkinter.END)
        self.out_msg.insert(0.0, encrypt)
        
    def decrypt_message(self):
        msg = self.msg.get(0.0, tkinter.END)
        decrypt = self.e.decrypt_message(msg)

        self.out_msg.delete(0.0, tkinter.END)
        self.out_msg.insert(0.0, decrypt)

root = tkinter.Tk()
root.title("Encryptor")
root.geometry("700x500")
app = Application(root)
root.mainloop()