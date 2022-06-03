import os
from os import listdir
from os.path import isfile, join
from tkinter.ttk import Separator
import yaml

path = f"{os.getcwd()}/mythicmobs"
files = [f for f in listdir(path) if isfile(join(path, f))]


def translate():
    
    #Make the script name look cooler
    istr = "[" + script_name + "] "
    
    #Print basic info of the script
    print("Translating " + istr + "...")
    print(istr + "Type: " + str(l[script_name]["Type"]).lower())
    print(istr + "Display: " + str(l[script_name]["Display"]))
    print(istr + "Health: " + str(l[script_name]["Health"]))
    print(istr + "Damage: " + str(l[script_name]["Damage"]))
    
    l[script_name]["type"] = "entity"
    l[script_name]["entity_type"] = l[script_name]["Type"]
    l[script_name]["mechanisms"] = {
        "custom_name": ifnulldict(l[script_name], "Display", ""), 
        "max_health": ifnulldict(l[script_name], "Health", "20"), 
        "health": ifnulldict(l[script_name], "Health", "20"),
        "armor_bonus": ifnulldict(l[script_name], "Armor", "0"),
        "glowing": ifnulldict(l[script_name]["Options"], "Glowing", "false"),
        "speed": ifnulldict(l[script_name]["Options"], "Speed", "0.3"),
        "has_ai": ifnulldict(l[script_name]["Options"], "NoAi", "false"),
        "gravity": strnot(ifnulldict(l[script_name]["Options"], "NoGravity", "false"))
        #TODO: equipment
    }
    #flags for event based things
    l[script_name]["flags"] = {
        "custom_damage": ifnulldict(l[script_name], "Damage", "5"), 
        "disguise": ifnulldict(l[script_name], "Disguise", ""),
        #TODO: drops, damage modifiers, kill message, trades, ai, factions, etc
    }
    deleteThis = ["Type", "Display", "Health", "Damage", "Options", "Skills", "Armor", "Disguise", "LevelModifiers", "Faction", "Mount", "KillMessages", "Equipment", "Drops", "DamageModifiers", "Trades", "AIGoalSelectors", "AITargetSelectors"]
    for i in deleteThis:
        trydel(l[script_name], i)
    
def ifnulldict(dict, key, default):
    #Return a value from a dictionary if it exists, otherwise return a default value
    if key in dict:
        return dict[key]
    else:
        return default
    
def trydel(dict, key):
    #Try to delete a key from a dictionary, if it doesn't exist, do nothing
    if key in dict:
        del dict[key]

def strnot(string):
    #Return the opposite of a string
    if string == "true":
        return "false"
    elif string == "false":
        return "true"
    else:
        return string

for s in files:
    
    #If the file is a .dsc file, skip it
    if(s.endswith(".dsc")):
        continue
    
    with open(f"{path}/{s}") as file:
        l = yaml.load(file, Loader=yaml.FullLoader)
        
    for script_name in l:
        translate()
        
    with open(f"{path}/{s}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=True, indent=4, line_break = "\n",Dumper=yaml.Dumper)
        yaml_file.write( dump )