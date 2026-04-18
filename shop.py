import time

from scripts import script_names, script_prices, script_list
from usefulFeatures import type_text, clear_screen


def shopping(budget, player):
    while True:
        try:
            clear_screen()
            type_text(script_list, 0.01)
            buy = input("Enter a script name to download it." \
            "\nEnter 'exit' to leave this menu.\n\n>>>")
            if buy == "exit":
                break
            if budget >= script_prices[script_names.index(buy)]:
                player.scripts.append(buy)
                player.budget_control(-int(script_prices[script_names.index(buy)]))
            if budget < script_prices[script_names.index(buy)]:
                type_text("\033[31mYou don't have enough money.\033[0m")
                time.sleep(2)
                continue

            break
        except:
            type_text("\033[31mInvalid script name. Please try again.\033[0m")
            clear_screen()
    

    