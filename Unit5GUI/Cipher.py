from Encryptor import Encryptor
import tkinter

class Application(tkinter.Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        tkinter.Label(self, text="Enter the message:").grid(row=0, column=0, sticky=tkinter.W)
        msg=tkinter.Entry(self)
        msg.grid(row=1, column=0, sticky=tkinter.W)
        tkinter.Button(self, text="Encrypt Message", command=Encryptor.encrypt_message ).grid(row=2, column=2, sticky=tkinter.W)
        
        tkinter.Label(self, text="Out:").grid(row=3, column=0, sticky=tkinter.W)
        out_txt=tkinter.Text(self, width=100, height=15, wrap=tkinter.WORD)
        
root=tkinter.Tk()
root.title("Encryptor")
app=Application(root)
root.mainloop()