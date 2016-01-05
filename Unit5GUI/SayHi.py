import tkinter

class Application (tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.bttnQuit=tkinter.Button(self, text="Quit", bg="red", font=("Helvetica", 16))
        self.bttnQuit["command"]=self.quit
        self.bttnQuit.grid()
        
        self.bttnHi=tkinter.Button(self, text="Hi!", bg="green", font=("Helvetica", 16))
        self.bttnHi["command"]=self.sayHi
        self.bttnHi.grid()
        
    def sayHi(self):
        print("Hello!")
        
def main():
    root=tkinter.Tk()
    root.title("It's almost break!")
    root.geometry("200x100")
    
    app=Application(root)
    
    root.mainloop()
    
main()