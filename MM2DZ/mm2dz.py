import os
from os import listdir
from os.path import isfile, join
from tkinter.ttk import Separator
import yaml

path = f"{os.getcwd()}/mythicmobs"
files = [f for f in listdir(path) if isfile(join(path, f))]

def translate():
    istr = "[" + script_name + "] "
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
        "health": ifnulldict(l[script_name], "Health", "20")
    }
    trydel(l[script_name], "Type")
    trydel(l[script_name], "Display")
    trydel(l[script_name], "Health")
    trydel(l[script_name], "Damage")
    trydel(l[script_name], "Options")
    trydel(l[script_name], "Skills")
    
def ifnulldict(dict, key, default):
    if key in dict:
        return dict[key]
    else:
        return default
    
def trydel(dict, key):
    if key in dict:
        del dict[key]

for s in files:
    if(s.endswith(".dsc")):
        continue
    with open(f"{path}/{s}") as file:
        l = yaml.load(file, Loader=yaml.FullLoader)
    for script_name in l:
        translate()
    #script_name = list(l.keys())[0]
    #translate()
    with open(f"{path}/{s}.dsc".replace(".yml", ""), 'w') as yaml_file:
        dump = yaml.dump(l, default_flow_style = False, allow_unicode = True, sort_keys=True, indent=4, Dumper=yaml.Dumper)
        yaml_file.write( dump )