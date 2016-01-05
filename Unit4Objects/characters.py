import random

class Character (object):
    ''' 
    The maximum dexterity of any character is 100.  This value is used in attack()
    to determine the likelihood of the Character hitting the enemy. 
    '''    
    MAX_DEXTERITY = 100
    
    def __init__ (self, name, hit_points, strength, dexterity, block):
        self.name=name
        self.hit_points=int(hit_points)
        self.strength=int(strength)
        self.dexterity=int(dexterity)
        self.block=int(block)
        ''' 
        Set the instance variables of name, hit_points, strength, and dexterity
        based upon the passed parameters. 
        '''
        
    def attack (self, enemy):
        hitChance=100+self.dexterity-enemy.dexterity
        if hitChance>random.randint(1, 200):
            attackPower=random.randint(0, self.strength)
            enemy.hit_points-=attackPower
            print(self.name + " attacks " + enemy.name + " for " + str(attackPower) + " damage" )
        else:
            print(self.name + " misses " + enemy.name)
        
        ''' 
        In this method, self attempts to attack the enemy.  First, the method determines if 
        a hit occurs using randomness.  If the opponents had the same dexterity, the probability 
        of a hit would be 50%.  If the dexterity of self is higher than that of enemy, the probabil+ty
        of a hit increases.  If the dexterity of self is lower than that of enemy, the probability
        of a hit decreases.  The exact implementation of this probability is up to you, but 
        make it as fair as possible.
        
        If a hit occurs, hit_points damage should be a random number between 0 and the self.strength.
        
        The method should then print the result of the attack to the user.
        '''
        
    def die (self):
        print(self.name + " has fainted!")
        ''' Prints a death message. '''
        
    def __str__ (self):
        print(self.name, self.hit_points, self.strength, self.dexterity, self.block)
        ''' Prints the name, hit points, strength, and dexterity of the object. '''
class CharacterList (object): 
    def __init__ (self, file_name):
        self.file_name=file_name
        text_file=open(file_name, "r")
        
        self.characters=[]
        
        for line in text_file:
            line=line.strip()
            row=line.split(',')
            self.characters.append(Character(row[0], row[1], row[2], row[3], row[4]))
        
        
        ''' 
        This method initializes a new CharacterList object by loading
        a list of Characters from file_name.  The list is stored as an
        instance variable of this CharacterList object.
        
        The file is in comma, separated format.  The fields of the file include:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
    
    def print_list (self):
        index=0
        for c in self.characters:
            print(str(index) + ": ", end=" ")
            c.__str__()
            index+=1
            
    def get_and_remove_character (self, i):
        #print(self.characters[i])
        return self.characters.pop(i)
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Doing so prevents the user and computer from 
        using the same character.
        '''
    
    def get_random_character (self):
        for character in self.characters:
            character=random.choice(self.characters)
        return character
        ''' Gets and returns a random character from the list (for the computer). '''
    
    def get_number_of_characters (self):
        count=0
        for characters in self.characters:
            count+=1
        return count
            
        ''' Returns the number of characters in the list. '''
            
