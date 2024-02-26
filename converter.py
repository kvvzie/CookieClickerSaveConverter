# made by kvvz

import base64

def decode_save_from_mobile(file_path):
    try:
        with open(file_path, 'r') as file:
            encoded_save = file.read().replace(" ", "")
            missing_padding = len(encoded_save) % 4
            if missing_padding != 0:
                encoded_save += '=' * (4 - missing_padding)
            decoded_save = base64.b64decode(encoded_save, altchars=b'+/')
            decoded_save = decoded_save.decode('ascii', errors='replace')
            return decoded_save
    except Exception as e:
        print("An error occurred while decoding the save from the mobile version:", e)
        return None

def encode_save_for_pc(decoded_save):
    if decoded_save is not None:
        encoded_save = base64.b64encode(decoded_save.encode('ascii')).decode('ascii')
        return encoded_save
    else:
        return None
# for normal values
def find_and_display_value(decoded_save, search_string):
    value_data_dict = {}
    if decoded_save is not None:
        if search_string in decoded_save:
            start_index = decoded_save.index(search_string) + len(search_string) + 2
            end_index = decoded_save.find(',', start_index)
            found_value = decoded_save[start_index:end_index].strip('"{}:')
            value_data_dict[search_string] = found_value

            print("Value found for string '{}': {}".format(search_string, found_value))
        else:
            print("The string '{}' was not found in the decoded text".format(search_string))
    else:
        print("An error occurred while decoding the save from the mobile version")
        
    return value_data_dict
# collecting values
def find_and_collect_values(decoded_save, value_name, value_data_dict):
    if decoded_save is not None:
        if value_name in decoded_save:
            start_index = decoded_save.index(value_name) + len(value_name) + 2
            end_index = decoded_save.find(',', start_index)
            found_value = decoded_save[start_index:end_index].strip('"{}:') 

            
            value_data_dict[value_name] = found_value
        else:
            print("The value '{}' was not found in the decoded text".format(value_name))
    else:
        print("An error occurred while decoding the save from the mobile version.")

# for buildings (idk how this works chat gtp gave me this) (i learned how it works)
def find_and_display_building(decoded_save, building_name):
    building_data_dict = {}
    if decoded_save is not None:
        start_index = decoded_save.find(building_name)
        if start_index != -1:
            opening_brace_index = decoded_save.find('{', start_index)
            closing_brace_index = decoded_save.find('}', opening_brace_index)
            if opening_brace_index != -1 and closing_brace_index != -1:
                building_data = decoded_save[opening_brace_index + 1:closing_brace_index]
                for param in ['"amount"', '"amountMax"', '"bought"', '"cookiesMade"']:
                    param_index = building_data.find(param)
                    if param_index != -1:
                        value_start_index = building_data.find(':', param_index) + 1
                        value_end_index = building_data.find(',', value_start_index) 
                        if value_end_index == -1:
                            value_end_index = closing_brace_index 
                        param_value = building_data[value_start_index:value_end_index]
                        building_data_dict[param] = param_value
                print("Building data found for '{}': {}".format(building_name, ", ".join(building_data_dict.values())))
            else:
                print("Error: No opening or closing brace found for '{}'".format(building_name))
        else:
            print("The building '{}' was not found in the decoded text".format(building_name))
    else:
        print("An error occurred while decoding the save from the mobile version.")
    
    return building_data_dict
# collecting data for encoding but for strings? (idk what im doin?) (update i did it)
def collect_data_for_strings(decoded_save, value_name):
    save_for_encoding = ""
    if decoded_save is not None:
        if value_name in decoded_save:
            start_index = decoded_save.index(value_name) + len(value_name) + 2
            end_index = decoded_save.find(',', start_index)
            found_value = decoded_save[start_index:end_index].strip('"{}:') 

            
            save_for_encoding += found_value + ", "
        else:
            print("The value '{}' was not found in the decoded text".format(value_name))
    else:
        print("An error occurred while decoding the save from the mobile version.")
    
    return save_for_encoding.rstrip(", ") 



# collecting data for encoding
def collect_data_for_encoding(decoded_save, building_name):
    save_for_encoding = ""
    if decoded_save is not None:
        start_index = decoded_save.find(building_name)
        if start_index != -1:
            opening_brace_index = decoded_save.find('{', start_index)
            closing_brace_index = decoded_save.find('}', opening_brace_index)
            if opening_brace_index != -1 and closing_brace_index != -1:
                building_data = decoded_save[opening_brace_index + 1:closing_brace_index]
                for param in ['"amount"', '"amountMax"', '"bought"', '"cookiesMade"']:
                    param_index = building_data.find(param)
                    if param_index != -1:
                        value_start_index = building_data.find(':', param_index) + 1
                        value_end_index = building_data.find(',', value_start_index) 
                        if value_end_index == -1:
                            value_end_index = closing_brace_index 
                        param_value = building_data[value_start_index:value_end_index].strip('"')
                        save_for_encoding += param_value + ", "
                save_for_encoding = save_for_encoding.rstrip(", ")  
            else:
                print("Error: No opening or closing brace found for '{}'".format(building_name))
        else:
            print("The building '{}' was not found in the decoded text".format(building_name))
    else:
        print("An error occurred while decoding the save from the mobile version.")
    
    return save_for_encoding

    

# user input for encoded mobile save
file_path = input("Enter the file path containing the encoded save from the mobile version: ")


# decoding user's mobile save 
decoded_save = decode_save_from_mobile(file_path)

# printing decoded text (will update in future) todo
if decoded_save is not None:
    print(" ")
    print("Decoded save from the mobile version:", decoded_save)
    print(" ")

    # search and display values ​​for strings
    find_and_display_value(decoded_save, "runStart")
    find_and_display_value(decoded_save, "time")
    find_and_display_value(decoded_save, "gameStart")
    # find_and_display_value(decoded_save, "bakeryName")
    find_and_display_value(decoded_save, "seed")
    # find_and_display_value(decoded_save, "youApperance1-7")

    find_and_display_value(decoded_save, "particles")
    # find_and_display_value(decoded_save, "numbers")
    # find_and_display_value(decoded_save, "autoSave")
    # find_and_display_value(decoded_save, "autoUpdate")
    find_and_display_value(decoded_save, "milk")
    find_and_display_value(decoded_save, "fancy")
    # find_and_display_value(decoded_save, "closingWarning")
    find_and_display_value(decoded_save, "cursors")
    # find_and_display_value(decoded_save, "defocus")
    # find_and_display_value(decoded_save, "shortNumbers")
    # find_and_display_value(decoded_save, "fastNotes")
    find_and_display_value(decoded_save, "cookiewobble")
    # find_and_display_value(decoded_save, "altFont")
    # find_and_display_value(decoded_save, "cssFilters")
    # find_and_display_value(decoded_save, "altCookieSound")
    # find_and_display_value(decoded_save, "iconCrates")
    # find_and_display_value(decoded_save, "backupWarning")
    # find_and_display_value(decoded_save, "extraButtons")
    # find_and_display_value(decoded_save, "lumpConfirmation")
    # find_and_display_value(decoded_save, "customGrandmas")
    # find_and_display_value(decoded_save, "sleepMode")
    # find_and_display_value(decoded_save, "enableColudSaving")
    find_and_display_value(decoded_save, "sound")
    # find_and_display_value(decoded_save, "scaryStaffOn")
    # find_and_display_value(decoded_save, "fullscreen")
    # find_and_display_value(decoded_save, "screenReader")
    # find_and_display_value(decoded_save, "todo")

    find_and_display_value(decoded_save, "cookies")
    find_and_display_value(decoded_save, "cookiesEarned")
    find_and_display_value(decoded_save, "cookieClicks")
    find_and_display_value(decoded_save, "gcClicksTotal")
    find_and_display_value(decoded_save, "cookiesHandmade")
    find_and_display_value(decoded_save, "gcMissed")
    # find_and_display_value(decoded_save, "bgType")
    # find_and_display_value(decoded_save, "milkType")
    # find_and_display_value(decoded_save, "cookiesForfeitedByAscending")
    find_and_display_value(decoded_save, "elderWrath")
    find_and_display_value(decoded_save, "pledges")
    find_and_display_value(decoded_save, "pledgeT")
    # find_and_display_value(decoded_save, "currentlyResearching")
    find_and_display_value(decoded_save, "researchTM")
    find_and_display_value(decoded_save, "resets")
    find_and_display_value(decoded_save, "gcClicks")
    find_and_display_value(decoded_save, "cookiesSucked")
    find_and_display_value(decoded_save, "wrinklersPopped")
    find_and_display_value(decoded_save, "santaLevel")
    find_and_display_value(decoded_save, "reindeerClicks")
    find_and_display_value(decoded_save, "seasonT")
    find_and_display_value(decoded_save, "seasonUses")
    find_and_display_value(decoded_save, "season")
    # find_and_display_value(decoded_save, "cookiesContainedInWrinklers")
    # find_and_display_value(decoded_save, "numberOfWrinklers")
    # find_and_display_value(decoded_save, "prestigeLevel")
    find_and_display_value(decoded_save, "heavenlyChips")
    find_and_display_value(decoded_save, "heavenlyChipsSpent")
    find_and_display_value(decoded_save, "cookiesReset")
    # find_and_display_value(decoded_save, "ascensionMode")
    # find_and_display_value(decoded_save, "pernamentUpgrades") will need a new function
    # find_and_display_value(decoded_save, "pernamentUpgrades") will need a new function
    # find_and_display_value(decoded_save, "pernamentUpgrades") will need a new function
    # find_and_display_value(decoded_save, "pernamentUpgrades") will need a new function
    # find_and_display_value(decoded_save, "pernamentUpgrades") will need a new function
    find_and_display_value(decoded_save, "dragonLevel")
    find_and_display_value(decoded_save, "dragonAura")
    find_and_display_value(decoded_save, "dragonAura2")
    # find_and_display_value(decoded_save, "goldenCookieChimeType")
    # find_and_display_value(decoded_save, "volume")
    # find_and_display_value(decoded_save, "numberOfShinyWrinklers")
    # find_and_display_value(decoded_save, "sugarLumps")
    # find_and_display_value(decoded_save, "totalSugarLumpsMade")
    # find_and_display_value(decoded_save, "timeOfStartOfSugarLump")
    # find_and_display_value(decoded_save, "timeOfLastSugarLump")
    # find_and_display_value(decoded_save, "sugarLumpType")
    # find_and_display_value(decoded_save, "upgradesInVault")
    # ind_and_display_value(decoded_save, "heralds")
    # find_and_display_value(decoded_save, "todo")
    # find_and_display_value(decoded_save, "todo")
    # find_and_display_value(decoded_save, "todo")
    # find_and_display_value(decoded_save, "musicVolume")
    # find_and_display_value(decoded_save, "cookiesSent")
    # find_and_display_value(decoded_save, "cookiesRecived")
    
    find_and_display_building(decoded_save, "Cursor")
    find_and_display_building(decoded_save, "Grandma")
    find_and_display_building(decoded_save, "Farm")
    find_and_display_building(decoded_save, "Mine")
    find_and_display_building(decoded_save, "Factory")
    find_and_display_building(decoded_save, "Bank")
    find_and_display_building(decoded_save, "Temple")
    find_and_display_building(decoded_save, "Wizard tower")
    find_and_display_building(decoded_save, "Shipment")
    find_and_display_building(decoded_save, "Alchemy lab")
    find_and_display_building(decoded_save, "Portal")
    find_and_display_building(decoded_save, "Time machine")
    find_and_display_building(decoded_save, "Antimatter condenser")
    find_and_display_building(decoded_save, "Prism")
    find_and_display_building(decoded_save, "Chancemaker")
    find_and_display_building(decoded_save, "Fractal engine")
    find_and_display_building(decoded_save, "Javascript console")
    find_and_display_building(decoded_save, "Idleverse")
    find_and_display_building(decoded_save, "Cortex baker")
    find_and_display_building(decoded_save, "You")

    value_data_dict = {}
    find_and_collect_values(decoded_save, "runStart", value_data_dict)
    find_and_collect_values(decoded_save, "time", value_data_dict)
    find_and_collect_values(decoded_save, "gameStart", value_data_dict)
    # find_and_collect_values(decoded_save, "bakeryName", value_data_dict)
    find_and_collect_values(decoded_save, "seed", value_data_dict)
    # find_and_collect_values(decoded_save, "youApperance1-7", value_data_dict)
    
    find_and_collect_values(decoded_save, "particles", value_data_dict)
    # find_and_collect_values(decoded_save, "numbers", value_data_dict)
    # find_and_collect_values(decoded_save, "autoSave", value_data_dict)
    # find_and_collect_values(decoded_save, "autoUpdate", value_data_dict)
    find_and_collect_values(decoded_save, "milk", value_data_dict)
    find_and_collect_values(decoded_save, "fancy", value_data_dict)
    # find_and_collect_values(decoded_save, "closingWarning", value_data_dict)
    find_and_collect_values(decoded_save, "cursors", value_data_dict)
    # find_and_collect_values(decoded_save, "defocus", value_data_dict)
    # find_and_collect_values(decoded_save, "shrotNumbers", value_data_dict)
    # find_and_collect_values(decoded_save, "fastNotes", value_data_dict)
    find_and_collect_values(decoded_save, "cookiewobble", value_data_dict)
    # find_and_collect_values(decoded_save, "altFont", value_data_dict)
    # find_and_collect_values(decoded_save, "cssFilters", value_data_dict)
    # find_and_collect_values(decoded_save, "altCookieSound", value_data_dict)
    # find_and_collect_values(decoded_save, "iconCrates", value_data_dict)
    # find_and_collect_values(decoded_save, "backupWarning", value_data_dict)
    # find_and_collect_values(decoded_save, "extraButtons", value_data_dict)
    # find_and_collect_values(decoded_save, "lumpConfirmation", value_data_dict)
    # find_and_collect_values(decoded_save, "customGrandmas", value_data_dict)
    # find_and_collect_values(decoded_save, "sleepMode", value_data_dict)
    # find_and_collect_values(decoded_save, "enableColudSaving", value_data_dict)
    find_and_collect_values(decoded_save, "sound", value_data_dict)
    # find_and_collect_values(decoded_save, "scaryStaffOn", value_data_dict)
    # find_and_collect_values(decoded_save, "fullscreen", value_data_dict)
    # find_and_collect_values(decoded_save, "screenReader", value_data_dict)
    # find_and_collect_values(decoded_save, "todo", value_data_dict)
    
    find_and_collect_values(decoded_save, "cookies", value_data_dict)
    find_and_collect_values(decoded_save, "cookiesEarned", value_data_dict)
    find_and_collect_values(decoded_save, "cookieClicks", value_data_dict)
    find_and_collect_values(decoded_save, "gcClicksTotal", value_data_dict)
    find_and_collect_values(decoded_save, "cookiesHandmade", value_data_dict)
    find_and_collect_values(decoded_save, "gcMissed", value_data_dict)
    # find_and_collect_values(decoded_save, "bgType", value_data_dict)
    # find_and_collect_values(decoded_save, "milkType", value_data_dict)
    # find_and_collect_values(decoded_save, "cookiesForfeitedByAscending", value_data_dict)
    find_and_collect_values(decoded_save, "elderWrath", value_data_dict)
    find_and_collect_values(decoded_save, "pledges", value_data_dict)
    find_and_collect_values(decoded_save, "pledgeT", value_data_dict)
    # find_and_collect_values(decoded_save, "currentlyResearching", value_data_dict)
    find_and_collect_values(decoded_save, "researchTM", value_data_dict)
    find_and_collect_values(decoded_save, "resets", value_data_dict)
    find_and_collect_values(decoded_save, "gcClicks", value_data_dict)
    find_and_collect_values(decoded_save, "cookiesSucked", value_data_dict)
    find_and_collect_values(decoded_save, "wrinklersPopped", value_data_dict)
    find_and_collect_values(decoded_save, "santaLevel", value_data_dict)
    find_and_collect_values(decoded_save, "reindeerClicks", value_data_dict)
    find_and_collect_values(decoded_save, "seasonT", value_data_dict)
    find_and_collect_values(decoded_save, "seasonUses", value_data_dict)
    find_and_collect_values(decoded_save, "season", value_data_dict)
    # find_and_collect_values(decoded_save, "cookiesContainedInWrinklers", value_data_dict)
    # find_and_collect_values(decoded_save, "numberOfWrinklers", value_data_dict)
    # find_and_collect_values(decoded_save, "prestigeLevel", value_data_dict)
    find_and_collect_values(decoded_save, "heavenlyChips", value_data_dict)
    find_and_collect_values(decoded_save, "heavenlyChipsSpent", value_data_dict)
    find_and_collect_values(decoded_save, "cookiesReset", value_data_dict)
    # find_and_collect_values(decoded_save, "ascensionMode", value_data_dict)
    # find_and_collect_values(decoded_save, "pernamentUpgrades", value_data_dict) will need a new function
    # find_and_collect_values(decoded_save, "pernamentUpgrades", value_data_dict) will need a new function
    # find_and_collect_values(decoded_save, "pernamentUpgrades", value_data_dict) will need a new function
    # find_and_collect_values(decoded_save, "pernamentUpgrades", value_data_dict) will need a new function
    # find_and_collect_values(decoded_save, "pernamentUpgrades", value_data_dict) will need a new function
    find_and_collect_values(decoded_save, "dragonLevel", value_data_dict)
    find_and_collect_values(decoded_save, "dragonAura", value_data_dict)
    find_and_collect_values(decoded_save, "dragonAura2", value_data_dict)
    # find_and_collect_values(decoded_save, "goldenCookieChimeType", value_data_dict)
    # find_and_collect_values(decoded_save, "volume", value_data_dict)
    # find_and_collect_values(decoded_save, "numberOfShinyWrinklers", value_data_dict)
    # find_and_collect_values(decoded_save, "sugarLumps", value_data_dict)
    # find_and_collect_values(decoded_save, "totalSugarLumpsMade", value_data_dict)
    # find_and_collect_values(decoded_save, "timeOfStartOfSugarLump", value_data_dict)
    # find_and_collect_values(decoded_save, "timeOfLastSugarLump", value_data_dict)
    # find_and_collect_values(decoded_save, "sugarLumpType", value_data_dict)
    # find_and_collect_values(decoded_save, "upgradesInVault", value_data_dict)
    # find_and_collect_values(decoded_save, "heralds", value_data_dict)
    # find_and_collect_values(decoded_save, "todo", value_data_dict)
    # find_and_collect_values(decoded_save, "todo", value_data_dict)
    # find_and_collect_values(decoded_save, "todo", value_data_dict)
    # find_and_collect_values(decoded_save, "musicVolume", value_data_dict)
    # find_and_collect_values(decoded_save, "cookiesSent", value_data_dict)
    # find_and_collect_values(decoded_save, "cookiesRecived", value_data_dict)

    
    
    
    


    print(" ")
    # encoding edited save for pc
    encoded_save_for_pc = encode_save_for_pc(decoded_save)
    if encoded_save_for_pc is not None:
        print("Encoded text for the PC version:", encoded_save_for_pc)
    else:
        print("An error occurred while encoding the save for the PC version")
else:
    print("An error occurred while decoding the save from the mobile version")
    
    
    print("Collected values:")
for key, value in value_data_dict.items():
    print("{} {}".format(key, value))
    
# testing probably gonna use if for encoding later on
building_data_dict = find_and_display_building(decoded_save, "Cursor")
building_data_dict = find_and_display_value(decoded_save, "seed")


save_for_encoding_grandma = collect_data_for_encoding(decoded_save, "Grandma")
save_for_encoding_cursor = collect_data_for_encoding(decoded_save, "Cursor")
print(save_for_encoding_cursor, save_for_encoding_grandma)

save_for_encoding_seed = collect_data_for_strings(decoded_save, "seed")
print(save_for_encoding_seed)




print(" ")
input("Press Enter to exit...")
