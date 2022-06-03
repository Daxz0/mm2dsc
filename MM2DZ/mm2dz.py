import os
from os import listdir
from os.path import isfile, join
import yaml

path = f"{os.getcwd()}/mythicmobs"
files = [f for f in listdir(path) if isfile(join(path, f))]

#Keys to be deleted from the mob script
oldkeys = ["Type", "Display", "Health", "Damage", "Options", "Skills"]

def translate():
    
    #Make the script name prettier for the user
    istr = "[" + script_name + "] "
    
    #Print mob information
    print(istr.capitalize())
    for key in oldkeys:
        print(istr + key + ": " + str(ifnulldict(l[script_name], key, "N/A")))
    
    #Add in the denizen keys
    l[script_name]["type"] = "entity"
    l[script_name]["entity_type"] = l[script_name]["Type"]
    l[script_name]["mechanisms"] = {
        "custom_name": ifnulldict(l[script_name], "Display", ""), 
        "max_health": ifnulldict(l[script_name], "Health", "20"), 
        "health": ifnulldict(l[script_name], "Health", "20"),
        "glowing": ifnulldict(l[script_name]["Options"], "Glowing", "false"),
        "speed": ifnulldict(l[script_name]["Options"], "Speed", "0.3"),
        "has_ai": ifnulldict(l[script_name]["Options"], "NoAi", "false"),
        "gravity": strnot(ifnulldict(l[script_name]["Options"], "NoGravity", "false"))
    }
    
    #Get rid of the old keys
    for key in oldkeys:
        trydel(l[script_name], key)
    
def ifnulldict(dict, key, default):
    #Check if the key exists in the dict, if not, return the default
    if key in dict:
        return dict[key]
    else:
        return default
    
def trydel(dict, key):
    #Try to delete the key from the dict, if it doesn't exist, do nothing
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
    
    #Check if the file already is a dsc file, if so, skip it
    if(s.endswith(".dsc")):
        continue
    
    with open(f"{path}/{s}") as file:
        l = yaml.load(file, Loader=yaml.FullLoader)
    
    #For each script, translate it
    for script_name in l:
        translate()
    
    
    with open(f"{path}/{s}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=True, indent=4, Dumper=yaml.Dumper)
        yaml_file.write( dump )