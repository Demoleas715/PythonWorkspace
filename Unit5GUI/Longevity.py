#Longevity
#Demonstrates text and entry widgets, and the Grid layout Manager

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        #create instruction label
        self.inst_lbl=Label(self, text="Enter password for the secret of longevity")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        
        #create label for password
        self.pw_lbl=Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        
        #create entry widget to accept password
        self.pw_ent=Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        
        #create submit button
        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)
        
        #create text widget to display message
        self.secret_text=Text(self, width=35, height=5, wrap=WORD)
        self.secret_text.grid(row=3, column=0, columnspan=2, sticky=W)
        
    def reveal(self):
        """ Display message based on password """
        contents=self.pw_ent.get()
        if contents=="secret":
            message="Here's the secret to living to 100: live to 99 " \
            "and then be very careful"
        else:
            message="That's not the correct password, so I can't share " \
            "the secret with you."
            
        self.secret_text.delete(0.0, END)
        self.secret_text.insert(0.0, message)
        
def main():
    root=Tk()
    root.title("Longevity")
    root.geometry("300x160")
    
    app=Application(root)
    
    root.mainloop()
    
main()