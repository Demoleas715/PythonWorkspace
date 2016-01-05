class Encryptor(object):
    def __init__(self, file_name):
        self.file_name=file_name
        self.e_dict={}
        self.d_dict={}
            
        text_file=open(file_name, "r")
    
        for line in text_file:
            line=line.strip().split("\t")
            self.e_dict[line[0]]=line[1]
            self.d_dict[line[1]]=line[0]
        '''
        Initializes a new encryption object, using the cipher
        from the specified file.

        This method sets the properties e_dict and d_dict.
        '''
    
    def encryptMessage (self, msg):
        self.msg=msg
        str=""
        for letter in msg:
            letter=self.e_dict.get(letter.upper(), letter)
            str+=letter
        return str
        '''
        Encrypts the string msg. Note this method DOES NOT print to
        The screen. Instead, it returns the encrypted message as a
        string.
        '''

    def decryptMessage (self, msg):
        self.msg=msg
        str=""
        for letter in msg:
            letter=self.d_dict.get(letter.upper(), letter)
            str+=letter
        return str
        ''' Performs the inverse action to encryptMessage. '''
        
        