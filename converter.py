# made by kvvz

import base64

def decode_save_from_mobile(encoded_save):
    encoded_save = encoded_save.replace(" ", "")
    missing_padding = len(encoded_save) % 4
    if missing_padding != 0:
        encoded_save += '=' * (4 - missing_padding)
    try:
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
    if decoded_save is not None:
        if search_string in decoded_save:
            start_index = decoded_save.index(search_string) + len(search_string) + 2
            end_index = decoded_save.find(',', start_index)
            found_value = decoded_save[start_index:end_index].strip('"') 

            print("Value found for string '{}': {}".format(search_string, found_value))
        else:
            print("The string '{}' was not found in the decoded text".format(search_string))
    else:
        print("An error occurred while decoding the save from the mobile version")
# for buildings (idk how this works chat gtp gave me this)
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
                        param_name = '{}{}'.format(building_name, param.replace('"', ''))
                        building_data_dict[param_name] = param_value
                        print("Building data found for '{}': {}:{}".format(building_name, param_name, param_value))
            else:
                print("Error: No opening or closing brace found for '{}'".format(building_name))
        else:
            print("The building '{}' was not found in the decoded text".format(building_name))
    else:
        print("An error occurred while decoding the save from the mobile version.")
    
    return building_data_dict


# user input for encoded mobile save
encoded_save_from_mobile = input("Enter the encoded save from the mobile version: ")

# decoding user's mobile save 
decoded_save = decode_save_from_mobile(encoded_save_from_mobile)

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
    find_and_display_value(decoded_save, "")
    find_and_display_value(decoded_save, "")
    find_and_display_value(decoded_save, "")
    find_and_display_value(decoded_save, "")
    find_and_display_value(decoded_save, "")
    find_and_display_building(decoded_save, "Cursor")
    find_and_display_building(decoded_save, "Grandma")
    find_and_display_building(decoded_save, "Farm")
    find_and_display_building(decoded_save, "Mine")
    find_and_display_building(decoded_save, "Factory")
    find_and_display_building(decoded_save, "Bank")
    find_and_display_building(decoded_save, "Temple")
    find_and_display_building(decoded_save, "Wizard tower")
    find_and_display_building(decoded_save, "Portal")
    find_and_display_building(decoded_save, "Time machine")
    find_and_display_building(decoded_save, "Fractal engine")
    find_and_display_building(decoded_save, "Javascript console")
    find_and_display_building(decoded_save, "Idleverse")
    find_and_display_building(decoded_save, "Cortex baker")
    find_and_display_building(decoded_save, "You")





    print(" ")
    # encoding edited save for pc
    encoded_save_for_pc = encode_save_for_pc(decoded_save)
    if encoded_save_for_pc is not None:
        print("Encoded text for the PC version:", encoded_save_for_pc)
    else:
        print("An error occurred while encoding the save for the PC version")
else:
    print("An error occurred while decoding the save from the mobile version")

building_data_dict = find_and_display_building(decoded_save, "Cursor")

print(" ")
input("Press Enter to exit...")
