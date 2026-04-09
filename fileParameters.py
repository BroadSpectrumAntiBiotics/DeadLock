
from fileNames import file_names
import random
import string

alphabet_list = list(string.ascii_lowercase)


class Parameter:
    def __init__(self, filename, filetype, creationDate, modificationDate):
        self.name = filename
        self.type = filetype
        self.creation = creationDate
        self.modification = modificationDate
    
    def corruptedName(self):
        for letter in alphabet_list:
            if letter not in self.name: 
                corruptedLetter = letter
                break

        self.corruptname = list(self.name)
        self.corruptname[random.randint(0, len(self.name)-1)] = corruptedLetter
        
        return ("".join(self.corruptname))

    def corruptedType(self):
        pass

        

