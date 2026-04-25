from player import Player
import virusCreator
from stages import Stages
import usefulFeatures
from introduction import intro
from ui import UI, doing
from end import ending, bad_ending
import dataMan
import json
from assetControl import path_audio
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

introSong = path_audio("music", "introExpanded.mp3")
good_ending_bgm = path_audio("music", "end1Good.wav")
bad_ending_bgm = path_audio("music", "end2Bad.wav")

pygame.mixer.init()
pygame.mixer_music.set_volume(0.5)



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
        pygame.mixer_music.load(introSong)
        pygame.mixer_music.play(fade_ms=5000, loops=-1)
        intro(name)
        pygame.mixer_music.stop()
        pygame.mixer_music.unload()
    player = Player(dataMan.data["name"], dataMan.data["hp"], dataMan.data["scripts"], dataMan.data["budget"], dataMan.data["update"])
    
    while True:
        usefulFeatures.clear_screen()
        if player.update > 100:
            pygame.mixer_music.load(good_ending_bgm)
            pygame.mixer_music.play(fade_ms=5000, loops=-1)
            ending(player)
            break
        if player.hp <= 0:
            pygame.mixer_music.load(bad_ending_bgm)
            pygame.mixer_music.play(fade_ms=5000, loops=-1)
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

