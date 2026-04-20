from player import Player
import virusCreator
from stages import Stages
import usefulFeatures
from introduction import intro
from ui import UI, doing
from end import ending, bad_ending
import dataMan
import json




def gameF():
    try:
        with open("data.json", "r") as file:
            dataMan.data = json.load(file)
    except:
        with open("data.json", "w") as file:
            json.dump(dataMan.data, file)
    usefulFeatures.clear_screen()
    if dataMan.data["name"] == "":
        name = input("Enter your name: ")
        dataMan.data["name"] = name
        usefulFeatures.clear_screen()
        intro(name)
    player = Player(dataMan.data["name"], dataMan.data["hp"], dataMan.data["scripts"], dataMan.data["budget"], dataMan.data["update"])
    
    while True:
        usefulFeatures.clear_screen()
        if player.update > 100:
            ending(player)
            break
        if player.hp <= 0:
            bad_ending()
            break
        UI(player.name, player.hp, player.scripts, player.budget, player.update)
        dataMan.data["budget"] = player.budget
        dataMan.data["scripts"] = player.scripts
        dataMan.data["hp"] = player.hp
        dataMan.data["update"] = player.update
        do = input("""
Type:
                   
"continue" for resuming update,
"shop" for viewing shop,
"info" for general info,
"exit" for... obviously.
                   
>>>""")
        if do == "exit":
            with open("data.json", "w") as file:
                json.dump(dataMan.data, file)
            break
        doing(do, player, player.budget)
        



if __name__ == "__main__":
    gameF()

