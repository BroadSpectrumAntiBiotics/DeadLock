import time

from scripts import script_names, script_prices, script_list
from usefulFeatures import type_text, clear_screen
from perks import perksShop, perk_prices, perk_names, unlocked_perks


def shopping(budget, player):
    while True:
        try:
            clear_screen()
            category = input("""
What do you want to buy:
                             "scripts" for scripts
                             "perks" for perks
                             
                             'exit' to leave this menu.

>>>""")
            clear_screen()
            if category == "exit":
                break
            if category == "scripts":
                type_text(script_list, 0.01)
                buy = input("Enter a script name to download it." \
                "\nEnter 'exit' to leave this menu.\n\n>>>")
                
                if buy == "exit":
                    break
                scriptname = script_names[script_names.index(buy)] #This is to ensure that buy equals any script name.
                times = int(input(f"How many {scriptname} do you want to purchase?: \n\n>>>"))
                if budget >= (script_prices[script_names.index(buy)]*times):
                    for once in range(times):    
                        player.scripts.append(buy)
                    player.budget_control(-(int(script_prices[script_names.index(buy)]))*times)
                if budget < (script_prices[script_names.index(buy)]*times):
                    type_text("\033[31mYou don't have enough money.\033[0m")
                    time.sleep(2)
                    continue

                break
            if category == "perks":
                type_text(perksShop(), 0.01)
                buy = input("\n\nEnter a perk name to configure it to your system." \
                "\nEnter 'exit' to leave this menu.\n\n>>>")
                
                if buy == "exit":
                    break
                perkname = unlocked_perks[unlocked_perks.index(buy)]
                if buy in unlocked_perks:
                    if budget >= (perk_prices[perk_names.index(buy)]):
                        player.budget_control(-(int(perk_prices[perk_names.index(buy)])))
                    if budget < (perk_prices[perk_names.index(buy)]):
                        type_text("\033[31mYou don't have enough money.\033[0m")
                        time.sleep(2)
                        continue
                

                break
        except:
            type_text("\033[31mInvalid type of input. Please try again.\033[0m")
            clear_screen()
    

    