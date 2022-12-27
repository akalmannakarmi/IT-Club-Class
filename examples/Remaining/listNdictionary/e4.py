# Program to add new contact in your contacts

myContacts = {
    "Jack":"9800000000",
    "Harry":"9800000001",
    "Karl":"9800000002"
}

print("Enter New Contact info")
name = input("Enter Name :")
number = input("Enter PhoneNo :")

myContacts[name] = number

print(myContacts)