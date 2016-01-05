import tkinter

class Screen_prepare_to_battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_prepare_to_battle, self).__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_next
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
         '''
        This method creates all of the widgets the prepare to battle page.
        '''
        #
        # TO DO
        #
 
    def continue_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.call_on_selected()
            
        