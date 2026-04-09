from usefulFeatures import type_text, clear_screen
import time

def intro(player):
    time.sleep(0.6)
    type_text(f"Welcome, {player}.")
    time.sleep(0.6)
    type_text("In Deadlock, you'll face various situations where you'll need to think.")
    time.sleep(0.6)
    type_text("You are trying to update files on a system you own.")
    time.sleep(0.6)
    type_text("But some of these files are infected.")
    time.sleep(0.6)
    type_text("Downloading infected files harms the system in their own ways.")
    time.sleep(0.6)
    type_text("Your mission is to finish the update while keeping the system safe.")
    time.sleep(0.6)
    type_text("Good luck.", 0.1)
    time.sleep(1.5)
    clear_screen()
    