# Read file
with open("Day2/Lessons/Requirements/data.txt","r") as test:
    rawData = test.read()
    
data = rawData.splitlines()
words = []
lineNo=0
for line in data:
    lineNo+=1
    line = line.split(" ")
    print(f"Line {lineNo}----------")
    for word in line:
        print(word)
        words.append(word)