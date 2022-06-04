#TODO: Mythicmob item conversion and add more try/excepts

import os
from os import listdir
from os.path import isfile, join
import yaml

path = f"{os.getcwd()}/input"
pathout = f"{os.getcwd()}/output"
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
    
    istr = "[" + script_name + "] "
    
    l[script_name]["type"] = "entity"
    l[script_name]["entity_type"] = l[script_name]["Type"].lower()
    
    #Mechanisms
    l[script_name]["mechanisms"] = {
        "custom_name": ifnulldict(l[script_name], "Display", ""),
        "max_health": ifnulldict(l[script_name], "Health", "20"), 
        "health": ifnulldict(l[script_name], "Health", "20"),
        "armor_bonus": ifnulldict(l[script_name], "Armor", "0"),
        "custom_name_visible": True,
        "glowing": s2bool(ifnulldict(l[script_name]["Options"], "Glowing", False)),
        "speed": float(ifnulldict(l[script_name]["Options"], "Speed", "0.3")),
        "has_ai": s2bool(strnot(ifnulldict(l[script_name]["Options"], "NoAi", False))),
        "gravity": s2bool(strnot(ifnulldict(l[script_name]["Options"], "NoGravity", False)))
        #TODO: equipment
        #TODO: more mechanisms from mm
    }
    
    #Flags for event based things
    l[script_name]["flags"] = {
        "mm2dz.custom_damage": ifnulldict(l[script_name], "Damage", "5"), 
        "mm2dz.disguise": diguiseWorker(script_name),
        #TODO: drops, damage modifiers, kill message, trades, ai, factions, etc
    }
    
    #Data for event based things
    l[script_name]["data"] = {
        "drops": dropsWorker(script_name),
        "damagemodifiers": damageModifierWorker(script_name)
        #TODO: kill message, trades, ai, factions, etc
    }
    
    #A list of things to delete
    old_keys = ["Type", "Display", "Health", "Damage", "Options", "Skills", "Armor", "Disguise", "LevelModifiers", "Faction", "Mount", "KillMessages", "Equipment", "Drops", "DamageModifiers", "Trades", "AIGoalSelectors", "AITargetSelectors", "Modules", "BossBar"]
    for i in old_keys:
        trydel(l[script_name], i)
    print(f">> Completed translation for file: {istr}")


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
        
        #TODO: further diguise logic
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

for s in files:
    #If the file is a .dsc file, skip it
    if(s.endswith(".dsc")):
        continue
    
    #Open the epic yaml file and put it into l as a dict
    with open(f"{path}/{s}") as file:
        l = yaml.load(file, Loader=yaml.FullLoader)
    
    count = 0
    
    for label in l:
        translate(label)
        count += 1
        
    print("\n<< All translations complete >>")
    print(">> Translated " + str(count) + " containers")
    
    #Makes a new .dsc file and dumps all new data in
    #Existing data is overwritten
    with open(f"{pathout}/{s}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=False, indent=4, line_break = "\n", Dumper=yaml.Dumper).replace("'", "")
        yaml_file.write(dump)