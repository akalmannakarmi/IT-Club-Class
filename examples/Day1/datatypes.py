a= 1
print(f"a is {a}")
b = 1.2
print(f"b is {b}")
myBool = True
print(f"myBool is {myBool}")
myString = "this String"
print(f"myString is {myString}")

myList = [1,2,"apple","ball"]
print("items in myList:")
for item in myList:
    print(item)

myArray = [1,2,3,4]
print("items in myArray:")
for item in myArray:
    print(item)
    
myDictionary = {
    "Name":"MyName",
    "Address":"Earth",
    "Phone no":911,
    "Course":"BCA 2nd Sem"
}
print("items in myDictionary:")
for key,value in myDictionary.items():
    print(f"Key:{key}\tValue:{value}")