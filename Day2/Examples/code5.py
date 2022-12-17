# Convert data of txt file to json file
import json

separator = ":"
# Read txt file
with open("Day2\Examples\code5.txt",'r') as file:
    txts = file.readlines()
    
# Split the data in a line
for i in range(0,len(txts)):
    txts[i] = txts[i].strip().split(separator)
    
# print(txts)
data={}
for line in txts:
    data[line[0]] = line[1]
        
# Write data to json file
with open("Day2\Examples\code5.json",'w') as file:
    jsonData = json.dumps(data)
    txts = file.writelines(jsonData)