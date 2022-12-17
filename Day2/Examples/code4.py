# Add to json file
import json

with open("Day2/Examples/data.json",'r') as file:
    data = json.load(file)
    

key = input("Enter Key: ").strip()
value = input("Enter Value: ").strip()

data[key] = value

with open("Day2/Examples/data.json",'w') as file:
    jsonData = json.dumps(data)
    file.writelines(jsonData)

print(f"Key : {key} added with value: {value}")