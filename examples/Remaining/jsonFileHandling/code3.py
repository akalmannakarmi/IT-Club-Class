# Query from json file
import json

with open("Day2/Examples/data.json",'r') as file:
    data = json.load(file)
    

queryKey = input("Enter Key: ").strip()

found = False
for key in data:
    if queryKey == key:
        print(f"The value of the Key is {data[key]}")
        found = True
        
if not found:
    print("The key does not exist")
