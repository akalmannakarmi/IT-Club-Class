# Program to remove a contact from your contacts

myContacts = {
    "Jack":"9800000000",
    "Harry":"9800000001",
    "Karl":"9800000002"
}

print(myContacts)

print("Enter Contact to remove")
name = input("Enter Name :")

myContacts.pop(name)

print(myContacts)