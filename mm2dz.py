#TODO: Mythicmob item conversion and add more try/excepts

import os
from os import listdir
from os.path import isfile, join
import yaml
import re

path = f"{os.getcwd()}/mobs/input"
pathout = f"{os.getcwd()}/mobs/output"
iteminpath = f"{os.getcwd()}/items/input"
itemoutpath = f"{os.getcwd()}/items/output"
files = [f for f in listdir(path) if isfile(join(path, f))]

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


def translate(script_name):
    
    #Currently this variable is unused, but it may be used in the future for
    #logging purposes
    istr = "[" + script_name + "] "
    
    #Define the script type as entity
    l[script_name]["type"] = "entity"
    
    #Define the type of entity
    #Convert it to lowercase to help with mm's anger issues
    l[script_name]["entity_type"] = l[script_name]["Type"].lower()
    
    #Mechanisms
    #TODO: don't include a mechanism if it's not in the original mob
    l[script_name]["mechanisms"] = {
        #"custom_name": "<element[" + ifnulldict(l[script_name], "Display", " ") + "].parse_color>",
        #"custom_name": ifnulldict(l[script_name], "Display", " "),
        "custom_name": parse_color(ifnulldict(l[script_name], "Display", "")),
        "max_health": ifnulldict(l[script_name], "Health", "20"), 
        "health": ifnulldict(l[script_name], "Health", "20"),
        "armor_bonus": ifnulldict(l[script_name], "Armor", "0"),
        "custom_name_visible": True,
        "glowing": ifnulldict(l[script_name]["Options"], "Glowing", False),
        "speed": float(ifnulldict(l[script_name]["Options"], "MovementSpeed", "0.23")),
        "has_ai": strnot(ifnulldict(l[script_name]["Options"], "NoAi", "false")),
        "gravity": strnot(ifnulldict(l[script_name]["Options"], "NoGravity", "false")),
        "silent": ifnulldict(l[script_name]["Options"], "Silent", "false"),
        #TODO: more mechanisms from mm
    }
    
    #Flags for event based things
    #All flags should start with "mm2dz."
    l[script_name]["flags"] = {
        "mm2dz.script_name": script_name,
        "mm2dz.custom_damage": ifnulldict(l[script_name], "Damage", "5"), 
        "mm2dz.disguise": diguiseWorker(script_name),
        "mm2dz.faction": ifnulldict(l[script_name], "Faction", "null"),
        "mm2dz.options.PreventItemPickup": ifnulldict(l[script_name]["Options"], "PreventItemPickup", False),
        "mm2dz.options.PreventOtherDrops": ifnulldict(l[script_name]["Options"], "PreventOtherDrops", False),
        #TODO: ai, immunity tables
    }
    
    #Data for event based things
    l[script_name]["data"] = {
        "drops": dropsWorker(script_name),
        "drops_chance": dropsWorkerChance(script_name),
        "damagemodifiers": damageModifierWorker(script_name),
        "kill_messages": kill_messageWorker(script_name),
    }
    
    #A list of things to delete
    old_keys = ["Type", "Display", "Health", "Damage", "Options", "Skills", "Armor", "Disguise", "LevelModifiers", "Faction", "Mount", "KillMessages", "Equipment", "Drops", "DamageModifiers", "Trades", "AIGoalSelectors", "AITargetSelectors", "Modules", "BossBar"]
    for i in old_keys:
        trydel(l[script_name], i)
    print(f">> Completed translation for file: {istr}")


def parse_color(string):
    #Match &+letter/number and replace with the match+<>
    regex = r"[&][a-z1-9]"
    matches = re.finditer(regex, string, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        match = match.group()
        final = "<"+match+">"
        string = string.replace(match, final)
    return string

def kill_messageWorker(script_name):
    try:
        returnList = {}
        id = 0
        for i in l[script_name]["KillMessages"]:
            id += 1
            returnList[id] = f"{i}"
        return returnList
    except:
        return "null"

def damageModifierWorker(script_name):
    try:
        returnList = {}
        
        for i in l[script_name]["DamageModifiers"]:
            i = i.split()
            modifier = i[0]
            value = i[1]
            returnList[f"{modifier}"] = value
            
        return returnList
    except:
        return "null"

def dropsWorkerChance(script_name):
    try:
        returnList = {}
        
        for i in l[script_name]["Drops"]:
            i = i.split()
            item = i[0]
            try:
                chance = i[2]
            except:
                chance = "100"
            returnList[f"{item}"] = chance
            
        return returnList
    except:
        return "null"

def dropsWorker(script_name):
    try:
        returnList = {}
        
        for i in l[script_name]["Drops"]:
            i = i.split()
            item = i[0]
            amount = i[1]
            returnList[f"{item}"] = amount
            
        return returnList
    except:
        return "null"

def diguiseWorker(script_name):
    #Deals with the disguise logic
    try:
        d = ifnulldict(l[script_name], "Disguise", None)
        
        if d != None:
            return d.split()[0]
            
        else:
            return "null"

    except:
        return "null"

def s2bool(v):
    if v == True or v == False:
        return v
    else:
        return v.lower() in ("true")

def ifnulldict(dict, key, default):
    #Return a value from a dictionary if it exists, otherwise return a default value
    try:
        if key in dict:
            return dict[key]
        else:
            return default
    except:
        return "null"

def trydel(dict, key):
    #Try to delete a key from a dictionary, if it doesn't exist, do nothing
    if key in dict:
        del dict[key]
    else:
        return

def strnot(string):
    #Return the opposite of a string
    if string == "true":
        return "false"
    elif string == "false":
        return "true"
    else:
        return "string not true or false"
    
def nacheck(string):
    if string == None:
        return "N/A"
    else:
        return string

count = 0
for s in files:
    #If the file is a .dsc file, skip it
    if(s.endswith(".dsc")):
        continue
    
    #Open the epic yaml file and put it into l as a dict
    with open(f"{path}/{s}") as file:
        l = yaml.load(file, Loader=yaml.FullLoader)
    
    for label in l:
        count += 1
        translate(label)
        
    #Makes a new .dsc file and dumps all new data in
    #Existing data is overwritten
    with open(f"{pathout}/{s}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=False, indent=4, line_break = "\n", Dumper=yaml.Dumper).replace("'", "")
        yaml_file.write( dump )
print("\n>> Translated " + str(count) + " container(s)")
print("\n<< All translations complete >>")
