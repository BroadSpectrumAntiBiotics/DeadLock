from fileNames import file_names
import virusCreator
from usefulFeatures import type_text, clear_screen
from fileParameters import Parameter
import pyautogui, os, time, random

class Stages:
    def __init__(self):
        self.stage = []
        self.numberofcorrupt = random.randint(1, virusCreator.virus.difficulty)
        self.numberofvalid = random.randint(1, virusCreator.virus.difficulty)
        self.corruptFiles = []
        self.validFiles = []

    def corruptfilesStager(self):
        for corruptfile in range(self.numberofcorrupt):
            self.corruptFiles.append(random.choice(file_names))
        return self.corruptFiles
        
    def validfilesStager(self):
        for validfile in range(self.numberofvalid):
            self.validFiles.append(random.choice(file_names))
        return self.validFiles
    
    def stager(self, corrupt_files, valid_files):
        self.stage = corrupt_files + valid_files
        random.shuffle(self.stage)
        
        return self.stage

def stagedGame(player):
    current_stage = Stages()
    corrupt_files = current_stage.corruptfilesStager()
    valid_files = current_stage.validfilesStager()
    allFiles = current_stage.stager(corrupt_files, valid_files)
    files = allFiles.copy()
    counter = 0
    clear_screen()
    type_text(f"{f"{current_stage.numberofcorrupt} number of files are corrupt among the next {len(current_stage.stage)} files.":^120}", 0.01)
    input(f"{f"Press enter to continue, {os.getlogin()}.":^120}")
    
    for file in files:
        clear_screen()
        filePars = Parameter(file[:(file.find("."))], file[(file.find(".")):])
        filename = filePars.name
        filetype = filePars.type
        filecreation = filePars.creation
        filemodification = filePars.modification
        if file in corrupt_files:
            filePars.corruptChoice()

        detection = input(f"""
            {"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
            {f"{len(files)-counter} files left.":^100}

            EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:
            =================================                   |=================================
            File Name: {filename:<41}|File Name: {filePars.name:<30}
            File Type: {filetype:<41}|File Type: {filePars.type:<30}
            Creation Date: {filecreation:<37}|Creation Date: {filePars.creation:<20}
            Last Modified: {filemodification:<37}|Last Modified: {filePars.modification:<20}
>>>""")
        if ((detection == "valid") and (file in valid_files)) or ((detection == "corrupted") and (file in corrupt_files)):
            player.budget_control(int(virusCreator.virus.difficulty * 10))
        else:
            player.budget_control(-(int(virusCreator.virus.difficulty * 5)))
        type_text(f"\nFile marked as {detection}.")
        counter += 1
    if virusCreator.virus.difficulty < 5:
        virusCreator.virus.difficulty += 1

        



