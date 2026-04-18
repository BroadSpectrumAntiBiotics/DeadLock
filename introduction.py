from usefulFeatures import type_text, clear_screen
import time

def intro(player):
    time.sleep(0.6)
    type_text(f"Welcome, {player}.")
    time.sleep(0.6)
    type_text("In Root Sentry, you'll face various situations where you'll need to think.")
    time.sleep(0.6)
    type_text("You are trying to update files on a system you own. By comparing file properties to see if they match.")
    time.sleep(0.6)
    type_text("But some of these files are infected. Mark them as 'corrupted'.")
    time.sleep(0.6)
    type_text("Downloading infected files harms the system in their own ways.")
    time.sleep(0.6)
    type_text("Your mission is to finish the update while keeping the system safe.")
    time.sleep(0.6)
    type_text("Good luck.", 0.1)
    input("Press enter to continue.")
    clear_screen()
    