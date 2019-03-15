import os
import importlib

cog_list = []

cogpath = os.path.join(os.path.dirname(__file__),'cog')
for file in os.listdir(cogpath):
    if file.endswith('.py'):
        cog_list.append(os.path.splitext(file)[0])

cogs = {} #final dict of cogs. Usage: cogs[<name>].<call>

for cog_name in cog_list:
    t = importlib.import_module('cog.'+cog_name)
    if not hasattr(t, "attributes"):
        print("Can't get attributes for module '"+cog_name+"'")
        continue
    if not t.attributes.get("Name"):
        print("Can't get 'Name' attribute for module '"+cog_name+"'")
        continue
    cogs[t.attributes.get("Name")] = t
    print("Imported module '"+cog_name+"'")
