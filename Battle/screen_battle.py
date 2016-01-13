import tkinter
from tkinter import ttk

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets for the battle page.
        '''
        #
        # TO DO
        #
        self.r=4

        self.attack_button = tkinter.Button(self, text = "Attack", command = self.attack_clicked, font=("Impact", 18), bg="black", fg="red")
        self.attack_button.grid(row=0, rowspan=2, column=0)
        self.you = tkinter.Label(self, text = "You")
        self.you.grid(row = 5, column = 0)
        self.computer = tkinter.Label(self, text = "Computer")
        self.computer.grid(row = 5, column = 1)
        imageLarge = tkinter.PhotoImage(file = "images/" + self.player1.large_image)
        self.w = tkinter.Label (self, image = imageLarge)
        self.w.photo = imageLarge
        imageLarge2 = tkinter.PhotoImage(file = "images/" + self.player2.large_image)
        self.w2 = tkinter.Label(self, image = imageLarge2)
        self.w2.photo = imageLarge2
        
        self.w.grid(row = 6, column=0)
        self.w2.grid(row = 6, column=1)

        self.attack_text1 = tkinter.Label(self, text="")
        self.attack_text2 = tkinter.Label(self, text="")
        self.attack_text1.grid(row=0, column=1)
        self.attack_text2.grid(row=1, column=1)

        self.player1hp = tkinter.Label(self, text=str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP", fg="green")
        self.player2hp = tkinter.Label(self, text=str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP", fg="green")
        self.player1hp.grid(row = 7, column = 0)
        self.player2hp.grid(row = 7, column = 1)

        self.death_message = tkinter.Label(self, text = "")
        self.death_message.grid(row = 3, column=1)

        self.death_message2=tkinter.Label(self, text="")

        self.victorious = tkinter.Label(self, text="", fg="blue")
        self.victorious.grid(row = 4, column=1)

        self.player1_dead = tkinter.Label(self, text = "", fg="red")
        self.player1_dead.grid(row=9, column=0)
        self.player2_dead = tkinter.Label(self, text = "", fg="red")
        self.player2_dead.grid(row=9, column=1)

        self.exit_button = tkinter.Button(self, text="Exit", command=self.exit_clicked)

        self.health_bar1=ttk.Progressbar(self, orient="horizontal", length=200, maximum=100, mode="determinate", value=100)
        self.health_bar1.grid(row=8, column=0)
        self.health_bar2=ttk.Progressbar(self, orient="horizontal", length=200, maximum=100, mode="determinate", value=100)
        self.health_bar2.grid(row=8, column=1)

        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        '''        
        #
        # TO DO
        #
        #while self.player1.hit_points>0 and self.player2.hit_points>0:
        self.attack_text1["text"] = self.player1.attack(self.player2)
        self.attack_text2["text"] = self.player2.attack(self.player1)

        self.player1hp["text"] = str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP"
        self.player2hp["text"] = str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP"

        self.health_bar1["value"] = 100*(self.player1.hit_points/self.player1_max_hp)
        self.health_bar2["value"] = 100*(self.player2.hit_points/self.player2_max_hp)

        if self.player1.hit_points<=0 or self.player2.hit_points<=0:
            if self.player1.hit_points<=0:
                self.player1hp["text"] = "0/" + str(self.player1_max_hp) + " HP"
                self.death_message["text"] = self.player1.die()
                self.victorious["text"] = str(self.player2.name) + " is victorious"
                self.player1_dead["text"] = "*DEAD*"

                self.attack_button.destroy()
                self.exit_button.grid(row=9, column=1, sticky=tkinter.E)

            if self.player2.hit_points<=0:
                self.player2hp["text"] = "0/" + str(self.player2_max_hp) + " HP"
                self.death_message["text"] = self.player2.die()
                self.victorious["text"] = str(self.player1.name) + " is victorious"
                self.player2_dead["text"] = "*DEAD*"

                self.attack_button.destroy()
                self.exit_button.grid(row=9, column=1, sticky=tkinter.E)

        if self.player1.hit_points<=0 and self.player2.hit_points<=0:
            self.player1hp["text"] = "0/" + str(self.player1_max_hp) + " HP"
            self.death_message["text"] = self.player1.die()
            self.death_message2["text"] = self.player2.die()
            self.victorious["text"] = "The battle ended in a tie!"
            self.player1_dead["text"] = "*DEAD*"
            self.player2_dead["text"] = "*DEAD*"

            self.death_message2.grid(row=4, column=1)
            self.victorious.grid(row=5, column=1)
            self.you.grid(row=6, column=0)
            self.computer.grid(row=6, column=1)
            self.w.grid(row=7, column=0)
            self.w2.grid(row=7, column=1)
            self.player1hp.grid(row=8, column=0)
            self.player2hp.grid(row=8, column=1)
            self.health_bar1.grid(row=9, column=0)
            self.health_bar2.grid(row=9, column=1)
            self.player1_dead.grid(row=10, column=0)
            self.player2_dead.grid(row=10, column=1)

            self.attack_button.destroy()

            self.exit_button.grid(row=10, column=1, sticky=tkinter.E)

    def exit_clicked(self):
        '''This method is called when the Exit button is clicked. 
            It passes control back to the callback method.'''        
        self.call_on_selected()