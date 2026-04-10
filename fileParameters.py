
from fileNames import file_names
import random
import string

alphabet_list = list(string.ascii_lowercase)


class Parameter:
    def __init__(self, filename, filetype):
        self.name = filename
        self.type = filetype
        self.creationDay = random.randint(1, 30)
        self.creationMonth = random.randint(1, 12)
        self.creationYear = random.randint(2000, 2026)
        self.creation = str(self.creationDay) + "." + str(self.creationMonth) + "." + str(self.creationYear)
    
    def corruptedName(self):
        for letter in alphabet_list:
            if letter not in self.name: 
                corruptedLetter = letter
                break

        self.corruptname = list(self.name)
        self.corruptname[random.randint(0, len(self.name)-1)] = corruptedLetter
        
        return ("".join(self.corruptname))

    def corruptedType(self):
        types = []
        for type in file_names:
            typeExt = type[(type.find(".")):]
            types.append(typeExt)
        self.type = random.choice(types)
        return self.type

    def corruptedCreation(self):
        one = [self.creationDay, self.creationMonth, self.creationYear]
        two = random.choice(one)
        if two == self.creationDay:
            self.creationDay = random.randint(1, 30)
        if two == self.creationMonth:
            self.creationMonth = random.randint(1, 12)
        if two == self.creationYear:
            self.creationYear = random.randint(2000, 2026)
        self.creation = str(self.creationDay) + "." + str(self.creationMonth) + "." + str(self.creationYear)
        return self.creation

    def corruptedModification(self):
        pass

        

        

