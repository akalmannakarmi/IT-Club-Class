# Write to json files
import json

data = {
    "key1":1,
    "key2":2,
    "key3":3,
    "key4":4,
    "key5":5,
    "key6":6,
    "key7":7
}

with open("Day2/Examples/data.json",'w') as file:
    jsonData = json.dumps(data)
    file.writelines(jsonData)