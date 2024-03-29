# My Mad Lib
# Create a story based on user input

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize the Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self, text="Enter information for a new story. Update story after each entry").grid(row=0, column=0, columnspan=2, sticky=W)
        
        # create a label and text entry for the name of a person
        Label(self, text="Name 1:").grid(row=1, column=0, sticky=W)
        self.name1_ent=Entry(self)
        self.name1_ent.grid(row=1, column=1, sticky=W)
        
        # create a label and text entry for a place
        Label(self, text= "Name 2:").grid(row=2, column=0, sticky=W)
        self.name2_ent=Entry(self)
        self.name2_ent.grid(row=2, column=1, sticky=W)
        
        # create the building variable
        self.building=StringVar()
        self.building.set(None)
        
        # create a building label
        Label(self, text="Name of building:").grid(row=3, column=0, sticky=W)
        
        # create a radiobutton option for the bank
        Radiobutton(self, text="Bank", variable=self.building, value="the bank").grid(row=3, column=1, sticky=W)
        
        # create a radiobutton option for City Hall
        Radiobutton(self, text="City Hall", variable=self.building, value="City Hall").grid(row=3, column=2, sticky=W)
        
        # create a radiobutton option for the police station
        Radiobutton(self, text="Police Station", variable=self.building, value="the police station").grid(row=3, column=3, sticky=W)
        
        # create a label and text entry for the first verb
        Label(self, text="Plural noun:").grid(row=4, column=0, sticky=W)
        self.plural_noun_ent=Entry(self)
        self.plural_noun_ent.grid(row=4, column=1, sticky=W)
        
        Label(self, text="Name:").grid(row=5, column=0, sticky=W)
        self.name3_ent=Entry(self)
        self.name3_ent.grid(row=5, column=1, sticky=W)
        
        Label(self, text="Noun:").grid(row=6, column=0, sticky=W)
        self.noun1_ent=Entry(self)
        self.noun1_ent.grid(row=6, column=1, sticky=W)
        
        Label(self, text="Adjective(s):").grid(row=7, column=0, sticky=W)
        
        self.is_dark=BooleanVar()
        Checkbutton(self, text="dark", variable=self.is_dark).grid(row=7, column=1, sticky=W)
        
        self.is_ominous=BooleanVar()
        Checkbutton(self, text="ominous", variable=self.is_ominous).grid(row=7, column=2, sticky=W)
        
        self.is_sinister=BooleanVar()
        Checkbutton(self, text="sinister", variable=self.is_sinister).grid(row=7, column=3, sticky=W)
        
        Label(self, text="Verb ending in -ing:").grid(row=8, column=0, sticky=W)
        self.verb_ing_ent=Entry(self)
        self.verb_ing_ent.grid(row=8, column=1, sticky=W)
        
        Label(self, text="Verb ending in -ed:").grid(row=9, column=0, sticky=W)
        self.verb_ed_ent1=Entry(self)
        self.verb_ed_ent1.grid(row=9, column=1, sticky=W)
        
        Label(self, text="Verb ending in -ed:").grid(row=10, column=0, sticky=W)
        self.verb_ed_ent2=Entry(self)
        self.verb_ed_ent2.grid(row=10, column=1, sticky=W)
        
        Label(self, text="Noun:").grid(row=11, column=0, sticky=W)
        self.noun2_ent=Entry(self)
        self.noun2_ent.grid(row=11, column=1, sticky=W)
        
        Label(self, text="Noun:").grid(row=12, column=0, sticky=W)
        self.noun3_ent=Entry(self)
        self.noun3_ent.grid(row=12, column=1, sticky=W)
        
        Label(self, text="Exclamation:").grid(row=13, column=0, sticky=W)
        self.exclamation_ent=Entry(self)
        self.exclamation_ent.grid(row=13, column=1, sticky=W)
        
        Label(self, text="Noun:").grid(row=14, column=0, sticky=W)
        self.noun4_ent=Entry(self)
        self.noun4_ent.grid(row=14, column=1, sticky=W)
        
        Label(self, text="Noun:").grid(row=15, column=0, sticky=W)
        self.noun5_ent=Entry(self)
        self.noun5_ent.grid(row=15, column=1, sticky=W)
        
        Label(self, text="Name of junior:").grid(row=16, column=0, sticky=W)
        self.name_of_junior_ent=Entry(self)
        self.name_of_junior_ent.grid(row=16, column=1, sticky=W)
        
        button=Button(self, text="Click to update story", command=self.tell_story).grid(row=17, column=0, sticky=W)
        
        self.story_txt=Text(self, width=100, height=15, wrap=WORD)
        self.story_txt.grid(row=18, column=0, columnspan=4)
        
        story="Two friends, [name] and [name] were wandering around the Mississippi University "
        story+="for Women on Halloween. As they were walking, they passed [name of building] where they "
        story+="heard weird [plural noun] from inside. [name] decided to go investigate. "
        story+="To get in the building, they climbed through an open [noun]. Inside, the hallway was [adjective(s)]"
        story+=" They heard [verb ending in -ing] coming from upstairs. [verb ending in -ed], they climbed the stairs. "
        story+="In the hallway there was a light that [verb ending in -ed] from the ceiling. Suddenly, a [noun] appeared "
        story+="in the [noun] coming from an open door. [exclamation]! [name of building] is haunted! "
        story+="Suddenly, a gust of [noun] knocked down the [noun] and revealed [name of junior] trying to scare them."
        
        self.story_txt.insert(0.0, story)
        
        
    def tell_story(self):
        name1=self.name1_ent.get()
        if name1=="":
            name1="[name]"
        else:
            name1=self.name1_ent.get().title()
            
        name2=self.name2_ent.get()
        if name2=="":
            name2="[name]"
        else:
            name2=self.name2_ent.get().title()
            
        building_name=self.building.get()
        if building_name=="":
            building_name="[name of building]"
        else:
            building_name=self.building.get()
            
        plural_noun=self.plural_noun_ent.get()
        if plural_noun=="":
            plural_noun="[plural noun]"
        else:
            plural_noun=self.plural_noun_ent.get()
        
        name3=self.name3_ent.get()
        if name3=="":
            name3="[name]"
        else:
            name3=self.name3_ent.get().title()
            
        noun1=self.noun1_ent.get()
        if noun1=="":
            noun1="[noun]"
        else:
            noun1=self.noun1_ent.get()
        
        adjective=""
        if self.is_dark.get():
            adjective+="dark"
            if self.is_ominous.get() and self.is_sinister.get():
                adjective+=", "
            elif self.is_ominous.get() or self.is_sinister.get():
                adjective+=" and "
        if self.is_ominous.get():
            adjective+="ominous"
            if self.is_dark.get() and self.is_sinister.get():
                adjective+=", and "
            elif self.is_sinister.get():
                adjective+=" and "
        if self.is_sinister.get():
            adjective+="sinister"
        
        if adjective=="":
            adjective="[adjective]"
            
        verb_ing=self.verb_ing_ent.get()
        if verb_ing=="":
            verb_ing="[verb ending in -ing]"
        else:
            verb_ing=self.verb_ing_ent.get()
        
        verb_ed1=self.verb_ed_ent1.get()
        if verb_ed1=="":
            verb_ed1="[verb ending in -ed]"
        else:
            verb_ed1=self.verb_ed_ent1.get()
        
        verb_ed2=self.verb_ed_ent2.get()
        if verb_ed2=="":
            verb_ed2="[verb ending in -ed]"
        else:
            verb_ed2=self.verb_ed_ent2.get()
        
        noun2=self.noun2_ent.get()
        if noun2=="":
            noun2="[noun]"
        else:
            noun2=self.noun2_ent.get()
        
        noun3=self.noun3_ent.get()
        if noun3=="":
            noun3="[noun]"
        else:
            noun3=self.noun3_ent.get()
            
        exclamation=self.exclamation_ent.get()
        if exclamation=="":
            exclamation="[exclamation]"
        else:
            exclamation=self.exclamation_ent.get()
        
        noun4=self.noun4_ent.get()
        if noun4=="":
            noun4="[noun]"
        else:
            noun4=self.noun4_ent.get()
            
        noun5=self.noun5_ent.get()
        if noun5=="":
            noun5="[noun]"
        else:
            noun5=self.noun5_ent.get()
        
        name_of_junior=self.name_of_junior_ent.get()
        if name_of_junior=="":
            name_of_junior="[name of junior]"
        else:
            name_of_junior=self.name_of_junior_ent.get().title() 
        
        story="Two friends, " + name1 + " and " + name2 + " were wandering around the Mississippi University "
        story+="for Women on Halloween. As they were walking, they passed " + building_name + " where they "
        story+="heard weird " + plural_noun + " from inside. " + name3 + " decided to go investigate. "
        story+="To get in the building, they climbed through an open " + noun1 + ". Inside, the hallway was "
        story+=adjective + ". They heard " + verb_ing + " coming from upstairs. " + verb_ed1 + ", they climbed the stairs. "
        story+="In the hallway there was a light that " + verb_ed2 + " from the ceiling. Suddenly, a " + noun2 + " appeared "
        story+="in the " + noun3 + " coming from an open door. " + exclamation + "! " + building_name + " is haunted! "
        story+="Suddenly, a gust of " + noun4 + " knocked down the " + noun5 + " and revealed " + name_of_junior + " trying to scare them."
        
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
        
root=Tk()
root.title("Mad Lib")
app=Application(root)
root.mainloop()