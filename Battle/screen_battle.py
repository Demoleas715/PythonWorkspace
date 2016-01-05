import tkinter

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
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()
  
            
            
            
            