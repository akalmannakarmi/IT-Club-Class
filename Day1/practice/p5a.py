# Simple ------------------------------------
myList=["Apple","Ball","Cat","Zebra"]

#Adding
myList.append("Elephant")
print(myList)
#Removing
myList.remove("Zebra")
print(myList)

#Replacing
index =myList.index("Ball")
myList[index] = "Bat"
print(myList)

# Medium -------------------------------------
myList=["Apple","Ball","Cat","Zebra"]

#Adding
addValue = input("Enter value to add: ")
myList.append(addValue)
print(myList)

#Removing
removeValue = input("Enter value to remove: ")
myList.remove(removeValue)
print(myList)

#Replacing
replaceValue = input("Enter value to replace: ")
replaceWithValue = input("Enter value to replace with: ")
index =myList.index(replaceValue)
myList[index] = replaceWithValue
print(myList)