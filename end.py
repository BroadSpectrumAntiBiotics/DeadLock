import time

from usefulFeatures import type_text

def ending(player):
    time.sleep(2)
    type_text("Update complete.", 0.1)
    type_text("I think you won.", 0.1)
    type_text(f"Congratulations... {player.name}.", 0.1)
    input()

def bad_ending():
    time.sleep(2)
    type_text("You couldn't keep the system safe.")
    type_text("You lost...", 0.1)
    input()
    
