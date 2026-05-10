from usefulFeatures import clear_screen, type_text

hinterPerkINFO = "You will be shown how many files are corrupted before you begin each stage."
currentfilePerkINFO = "With a small chance, you will be shown whether a file is corrupted or not."

perk_names = ["Hint", "CurrentFile"]
perk_prices = [20, 35]
perkinfolist = [hinterPerkINFO, currentfilePerkINFO]

unlocked_perks = []

def perksShop():
    perk_list = f"""
{"Perk name":^20}|{"Price":^8}|{"About this perk":^20}
{"="*60}"""
    for perk in unlocked_perks:
        index = perk_names.index(perk)
        type_text(f"{perk_names[index]:^20}|{perk_prices[index]:^8}| {perkinfolist[index]:^}")
        
    return perk_list




def hinter(player, current_stage):
    clear_screen()
    type_text(f"{f"{" "*8}{current_stage.numberofcorrupt} number of files are corrupt among the next {len(current_stage.stage)} files.":^120}", 0.01)
    input(f"{f"{" "*8}Press enter to continue, {player.name}.":^120}")

def currentfile_perk():
    type_text(f"{f"{" "*8} ATTENTION! THIS FILE IS CORRUPTED!":^120}", 0.01)
    input(f"{f"{" "*8}Press enter to continue.":^120}")
