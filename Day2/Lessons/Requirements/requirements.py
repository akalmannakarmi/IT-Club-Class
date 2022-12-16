# ---------------------------------------------------------------
# How to use files ----------------------------------------------
# ---------------------------------------------------------------

# Create file and write to it
with open("Day2/Lessons/Requirements/create.txt","w") as test:
    test.writelines("Hellow")

# Append to file
with open("Day2/Lessons/Requirements/append.txt","a") as test:
    test.writelines("Hellow\n")

# Read file
with open("Day2/Lessons/Requirements/read.txt","r") as test:
    print(test.read())


# ---------------------------------------------------------------
# How to filter string ------------------------------------------
# ---------------------------------------------------------------

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