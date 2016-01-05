#Click counter
#Demonstrates binding an event with an event handler

from tkinter import *

class Application(Frame):
    """ GUI application which counts button clicks """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks=0  #The number of button clicks
        self.create_widget()
        
    def create_widget(self):
        """ Create a button which displays the number of clicks. """
        self.bttn = Button(self)
        self.bttn["text"]="Total Clicks: 0"
        self.bttn["command"]=self.update_count
        self.bttn.grid()
        
    def update_count(self):
        """ Increase click count and display new total. """
        self.bttn_clicks += 1
        self.bttn["text"]="Total Clicks: " + str(self.bttn_clicks)
        if self.bttn_clicks>=100:
            self.bttn["text"] = "You're such a loser... Total Clicks: " + str(self.bttn_clicks)
def main():
    root=Tk()
    root.title("Click Counter")
    root.geometry("400x50")
    
    app=Application(root)
    
    root.mainloop()
    
main()