# Program to list all your contacts

myContacts = {
    "Jack":"9800000000",
    "Harry":"9800000001",
    "Karl":"9800000002"
}

for name,phoneNo in myContacts.items():
    print(f"{name} : {phoneNo}")