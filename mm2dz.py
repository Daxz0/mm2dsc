#TODO: add more try/excepts

#Attempts to use the formatting from https://peps.python.org/pep-0008/


#Pathfinders
import os
from os import listdir
from os.path import isfile, join

#Very important packages for translation
import yaml
import re
import json

inputpath = f"{os.getcwd()}/input"
outputpath = f"{os.getcwd()}/output"
mobinputpath = f"{inputpath}/mobs"
moboutpath = f"{outputpath}/mobs"
iteminputpath = f"{inputpath}/items"
itemoutputpath = f"{outputpath}/items"
mobfiles = [f for f in listdir(mobinputpath) if isfile(join(mobinputpath, f))]
itemfiles = [f for f in listdir(iteminputpath) if isfile(join(iteminputpath, f))]

print("""
  __  __ __  __   _              _  _____           _       _   
 |  \/  |  \/  | | |            | |/ ____|         (_)     | |  
 | \  / | \  / | | |_ ___     __| | (___   ___ _ __ _ _ __ | |_ 
 | |\/| | |\/| | | __/ _ \   / _` |\___ \ / __| '__| | '_ \| __|
 | |  | | |  | | | || (_) | | (_| |____) | (__| |  | | |_) | |_ 
 |_|  |_|_|  |_|  \__\___/   \__,_|_____/ \___|_|  |_| .__/ \__|
                                                     | |        
                                                     |_|        

Created by: Daxz & funkychicken493

https://github.com/Daxz0/mm2dz
""")

#Translate a mm mob to dsc entity container
def translate_entity(script_name):
    
    #Spruce up the name for logging
    istr = "[" + script_name + "] "
    
    #Define the script type as entity
    l[script_name]["type"] = "entity"
    
    #Define the type of entity
    #Convert it to lowercase to help with mm's anger issues
    l[script_name]["entity_type"] = l[script_name]["Type"].lower()
    
    l[script_name]["mechanisms"] = {}
    
    #mm options -> dsc mechanisms
    #TODO: don't include a mechanism if it's not in the original mob
    
    #custom name
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "Display", "custom_name", parse_color(if_null_dict(l[script_name], "Display", "")))
    #max health
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "Health", "max_health", if_null_dict(l[script_name], "Health", "20"))
    #health
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "Health", "health", if_null_dict(l[script_name], "Health", "20"))
    #armor bonus
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "Armor", "armor_bonus", if_null_dict(l[script_name], "Armor", "0"))
    #custom name visible
    l[script_name]["mechanisms"]["custom_name_visible"] = True
    if l[script_name].get("Options") != None:
        #glowing
        l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name]["Options"], "Glowing", "glowing", bool_to_other(if_null_dict(l[script_name]["Options"], "Glowing", "false"), False))
        #speed
        l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name]["Options"], "MovementSpeed", "speed", float(if_null_dict(l[script_name]["Options"], "MovementSpeed", "0.23")))
        #has ai
        l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name]["Options"], "NoAi", "has_ai", str_not(if_null_dict(l[script_name]["Options"], "NoAi", "false")))
        #gravity
        l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name]["Options"], "NoGravity", "gravity", str_not(if_null_dict(l[script_name]["Options"], "NoGravity", "false")))
        #silent
        l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name]["Options"], "Silent", "silent", if_null_dict(l[script_name]["Options"], "Silent", "false"))
    
    #Flags for event based things
    #All flags should start with "mm2dz."
    l[script_name]["flags"] = {
        "mm2dz.script_name": script_name,
        "mm2dz.custom_damage": if_null_dict(l[script_name], "Damage", "5"), 
        "mm2dz.disguise": disguise_worker(script_name),
        "mm2dz.faction": if_null_dict(l[script_name], "Faction", "null"),
        "mm2dz.options.PreventItemPickup": if_null_dict(try_except_dict('l[script_name]["Options"]'), "PreventItemPickup", False),
        "mm2dz.options.PreventOtherDrops": if_null_dict(try_except_dict('l[script_name]["Options"]'), "PreventOtherDrops", False),
        #TODO: ai, immunity tables
    }
    
    #custom damage
    l[script_name]["flags"] = include_if_exists(l[script_name]["flags"], l[script_name], "Damage", "custom_damage", if_null_dict(l[script_name], "Damage", "5"))
    #disguise
    l[script_name]["flags"] = include_if_exists(l[script_name]["flags"], l[script_name], "Disguise", "disguise", disguise_worker(script_name))
    #faction
    l[script_name]["flags"] = include_if_exists(l[script_name]["flags"], l[script_name], "Faction", "faction", if_null_dict(l[script_name], "Faction", "null"))
    #prevent item pickup
    l[script_name]["flags"] = include_if_exists(l[script_name]["flags"], l[script_name], "Options", "PreventItemPickup", if_null_dict(try_except_dict('l[script_name]["Options"]'), "PreventItemPickup", False))
    #prevent other drops
    l[script_name]["flags"] = include_if_exists(l[script_name]["flags"], l[script_name], "Options", "PreventOtherDrops", if_null_dict(l[script_name]["Options"], "PreventOtherDrops", False))
    
    #Data for event based things
    l[script_name]["data"] = {
        "mm2dz": "true",
    }
    
    #drops
    l[script_name]["data"] = include_if_exists(l[script_name]["data"], l[script_name], "Drops", "drops", drop_worker(script_name))
    #drops chance
    l[script_name]["data"] = include_if_exists(l[script_name]["data"], l[script_name], "Drops", "drops_chance", drop_chance_worker(script_name))
    #damage modifiers
    l[script_name]["data"] = include_if_exists(l[script_name]["data"], l[script_name], "Damage", "damage_modifiers", damage_modifier_worker(script_name))
    #kill messages
    l[script_name]["data"] = include_if_exists(l[script_name]["data"], l[script_name], "KillMessages", "kill_messages", kill_message_worker(script_name))
    
    remove_old_keys(script_name)
    
    print(f">> Completed translation for entity file: {istr}\n")

#Translate a mm item to dsc item container
def translate_item(script_name):
    
    #If the container uses numerical IDs, warn the user if they aren't using override
    #Numerical IDs are not supported by dsc and were used in ancient versions of Minecraft to identitfy items
    #I honestly don't know why numerical IDs are supported by mm
    if type(l[script_name]["Id"]) != str and l[script_name].get("Override") == None:
        raise Exception("""
                        Item numerical id translation is not supported yet, but
                        if you don't care, please put "Override: true" underneath
                        the item id in the yaml file
                        """)
    
    l[script_name]["type"] = "item"
    
    #If the Id is a numerical ID, tell the user to fix it,
    #otherwise, just set it equal to the Id
    if type(l[script_name]["Id"]) == int:
        l[script_name]["material"] = str(l[script_name]["Id"]) + " CHANGE ME https://minecraftitemids.com/"
    else:
        l[script_name]["material"] = l[script_name]["Id"]
    
    l[script_name]["mechanisms"] = {}
    
    #unbreakable
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "Unbreakable", "unbreakable", if_null_dict(l[script_name], "Unbreakable", "false"))
    #custom model data
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "Data", "custom_model_data", if_null_dict(l[script_name], "Data", "0"))
    #hides flags
    l[script_name]["mechanisms"] = include_if_exists(l[script_name]["mechanisms"], l[script_name], "HideFlag", "hides", if_null_dict(l[script_name], "HideFlag", "false"))
    
    #Flag stuff for dsc tomfuckery
    l[script_name]["flags"] = {
        #This flag does nothing, but it stops empty field errors on dsc files
        "mm2dz.item": "true",
    }
    
    #prevent stack
    #just set the flag to a random ass uuid if it's true
    l[script_name]["flags"] = include_if_exists(l[script_name]["flags"], l[script_name], "PreventStacking", "mm2dz.prevent_stack", bool_to_other(if_null_dict(l[script_name], "PreventStacking", "false"), "true + <util.random_uuid>"))
    
    #A whole bunch of tomfuckery to get the item name
    l[script_name]["display name"] = parse_color(if_null_dict(l[script_name], "Display", ""))
    
    #Define the lore as empty before we modify it
    l[script_name]["lore"] = try_except_dict('l[script_name]["Lore"]').split()
    #Convert mm Lore to dsc lore
    for line in l[script_name]["lore"]:
        #Parse the color before replacing empty lines
        try_except_dict('l[script_name]["Lore"].append(replace_empty(parse_color(line)))')
    
    #Check if the enchantments exist in the first place
    if l[script_name].get("Enchantments") != None:
        
        #Define the enchantments as empty before we modify it
        l[script_name]["enchantments"] = []

        #mm enchantments are practically the same as dsc enchantments, so just lowercase them
        for enchantment in l[script_name]["Enchantments"]:
            l[script_name]["enchantments"].append(enchantment.lower())
    
    #Finish up
    remove_old_keys(script_name)
    
    print(f">> Completed translation for item file: {script_name}\n")

#I've noticed that the mm yaml keys always start with a capital letter
#so I've created this function to remove any keys that start with a capital letter
def remove_old_keys(script_name):
    
    for key in l[script_name].copy():
        
        if key[0].isupper():
            try_del(l[script_name], key)
    
    return l[script_name]

#Turn the mm supported color codes into dsc color codes
#Example: &e -> <&e>
#Example: <&sq> -/> <<&s>q>
def parse_color(string):
    regex = r"&[a-z1-9]"
    matches = re.finditer(regex, string, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        match = match.group()
        #FIXME: this will check for <> tags in mm files, but will break if any user has ">" in the string
        try:
            if string[string.find(match) + 3] == '>':
                continue
        except:
            pass
        #end hack
        
        #Replace the color code with the dsc equivalent
        string = string.replace(match, "<" + match + ">")
    #Send the string back to the oven
    return string

#Takes a completely empty string (usually lore) and 
#replaces it with dsc's empty string
def replace_empty(string):
    if string == "":
        #The <empty> tag is usually redundant, but it becomes extremely important here
        return "<empty>"
    else:
        return string

#Show lower usage of needed etcWorkers()
def bool_to_other(val, default):
    if val == "true" or val == True:
        return default
    else:
        return val

#Function to include a key in a dictionary if another key already exists within that dictionaryz
def include_if_exists(dictionary, old_dictionary, checking_key, key_to_set, value_to_set):
    if old_dictionary.get(checking_key) != None:
        dictionary[key_to_set] = value_to_set
    return dictionary

#Processes the mob's custom kill messages
def kill_message_worker(script_name):
    try:
        returnList = {}
        num_messages = 0
        for message in l[script_name]["KillMessages"]:
            num_messages += 1
            returnList[num_messages] = f"{message}"
        return returnList
    except:
        return "null"

#Processes mob damage modifiers
def damage_modifier_worker(script_name):
    try:
        returnList = {}
        
        for damage_modifier in l[script_name]["DamageModifiers"]:
            damage_modifier = damage_modifier.split()
            modifier = damage_modifier[0]
            value = damage_modifier[1]
            returnList[f"{modifier}"] = value
            
        return returnList
    except:
        return "null"

#Processes the chances for drops
def drop_chance_worker(script_name):
    try:
        returnList = {}
        
        #<item/exp/droptable> <amount> <chance>
        for drop in l[script_name]["Drops"]:
            drop = drop.split()
            item = drop[0]
            try:
                chance = str(drop[2])
            except:
                chance = "100"
            returnList[f"{item}"] = chance
            
        return returnList
    except:
        return "null"

#Processes the mm drops
def drop_worker(script_name):
    try:
        returnList = {}
        
        #<item/exp/droptable> <amount> <chance>
        for drop in l[script_name]["Drops"]:
            drop = drop.split()
            item = drop[0]
            amount = drop[1]
            returnList[f"{item}"] = amount
            
        return returnList
    except:
        return "null"

#Deals with the mm disguise mechanics
def disguise_worker(script_name):
    try:
        #SKELETON setGlowing setSpinning setBurning
        d = if_null_dict(l[script_name], "Disguise", None)
        
        if d != None:
            return d.split()[0]
        else:
            return "null"
    except:
        return "null"

#Converts a string to a boolean
def str_to_bool(str):
    #If v is a boolean, return it
    if type(str) == bool:
        return str
    #Otherwise, convert it to a boolean
    else:
        #1. Lowercase the string
        #2. If it's "true", return true
        #3. If it isn't, return false
        return str.lower() == "true"


#Return a value from a dictionary if it exists, otherwise return a default value
def if_null_dict(dict, key, default):
    try:
        if key in dict:
            return dict[key]
        else:
            return default
    except:
        return "null"

#Python freaks out so this checks if it exists in the first place without calling the actual thing
def try_except_dict(dict):
    try:
        if json.load(dict) != None:
            return json.load(dict)
    except:
        return "null"

#Try to delete a key from a dictionary, if the key is missing, do nothing
def try_del(dict, key):
    if key in dict:
        del dict[key]

#Return the opposite of a string
def str_not(string):
    if string == "true":
        return "false"
    elif string == "false":
        return "true"
    else:
        return "string not true or false"

#Return snake_case from camelCase
#(will be used later for container name formatting)
#Example: camelCase -> camel_case
#Code generated by Github Copilot ###Lets all say thanks to Copilot before it proceeds to charge us 70$ a month!!!###
def camel_case_to_snake_case(string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

#Counter for the amount of containers processed
count = 0

#Foreach mob file, process it
for fil in mobfiles:
    
    #If the file is not a .yml file, skip it
    if not fil.endswith(".yml"):
        if fil.endswith(".gitkeep"):
            continue
        else:
            print(">> Skipping file: " + fil)
            continue
    
    #Open the yaml and load it into a dictionary
    with open(f"{mobinputpath}/{fil}") as f:
        l = yaml.load(f, Loader=yaml.FullLoader)
    
    for container_name in l:
        count += 1
        print(f">> Processing mob container {container_name}...")
        if l[container_name]["Type"] != None:
            translate_entity(container_name)

    #Writes the new container to a file with the same name
    with open(f"{moboutpath}/{fil}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=False, indent=4, line_break = "\n", Dumper=yaml.Dumper).replace("'", "")
        yaml_file.write(dump)
        
#Foreach item file, process it
for fil in itemfiles:
    
    #If the file is not a .yml file, skip it
    if not fil.endswith(".yml"):
        if fil.endswith(".gitkeep"):
            continue
        else:
            print(">> Skipping file: " + fil)
            continue
    
    #Open the yaml and load it into a dictionary
    with open(f"{iteminputpath}/{fil}") as f:
        l = yaml.load(f, Loader=yaml.FullLoader)
    
    for container_name in l:
        count += 1
        print(f">> Processing item container {container_name}...")
        if l[container_name]["Id"] != None:
            translate_item(container_name)

    #Writes the new container to a file with the same name
    with open(f"{itemoutputpath}/{fil}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=False, indent=4, line_break = "\n", Dumper=yaml.Dumper).replace("'", "")
        yaml_file.write(dump)

if count > 1:
    print(">> Translated " + str(count) + " containers.")
elif count == 1:
    print(">> Translated " + str(count) + " container.")
else:
    print(">> No containers were translated.")

print(">> All translations complete <<\n")
