# Simple
myList =["Apple","Ball","Cat","Zebra"]

choice = input("""
Print list       : p or 1
Add to list      : a or 2
Remove from list : r or 3
Replace from list: rp or 4
Enter your choice: """)

if choice == 'p' or choice == '1':
    print(myList)
elif choice == 'a' or choice == '2':
    addValue = input("Enter val to Add: ")
    myList.append(addValue)
elif choice == 'r' or choice == '3':
    removeValue = input("Enter val to Remove: ")
    myList.remove(removeValue)
elif choice == 'rp' or choice == '4':
    replaceValue = input("Enter val to Replace: ")
    replaceWithValue = input("Enter val to Replace with: ")
    index = myList.index(replaceValue)
    myList[index] = replaceWithValue
else:
    print("Invalid")


print(myList)