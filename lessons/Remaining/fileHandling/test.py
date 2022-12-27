# Read file
with open("Day2/Lessons/Requirements/data.txt","r") as test:
    rawData = test.read()
    
words = []
lineNo=0
# Spliting the data into lines then words
data = rawData.splitlines()
for line in data:
    lineNo+=1
    line = line.split(" ")
    print(f"Line {lineNo}----------")
    for word in line:
        print(word)
        words.append(word)