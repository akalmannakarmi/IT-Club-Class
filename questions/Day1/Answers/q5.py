# 5) Create a program to print the smallest and the largest number in the array/list [2,7,8,23,75,23,64].

# Easy answer---------------------------------------------------------
myList = [2,7,8,23,75,23,64]
myList.sort()
print(f"Largest = {myList[-1]}")
print(f"Smallest = {myList[0]}")


# Medium answer---------------------------------------------------------
myList = [2,7,8,23,75,23,64]

largest = myList[0]
smallest = myList[0]
for item in myList:
    if item > largest:
        largest = item
    if item < smallest:
        smallest = item
print(f"Largest = {largest}")
print(f"Smallest = {smallest}")