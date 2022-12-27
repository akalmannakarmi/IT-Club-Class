# Read json data form json file
import json

with open("Day2/Examples/data.json",'r') as file:
    data = json.load(file)
    
for key,value in data.items():
    print(key,value)
    
