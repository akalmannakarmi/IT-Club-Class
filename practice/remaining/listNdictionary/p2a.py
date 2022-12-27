# Medium
contacts = {}

while True:
    name = input("Enter Name :")
    phoneNo = input("Enter PhoneNo :")
    
    if name == "" or phoneNo == "":
        break
    
    contacts[name] = phoneNo
    
print(contacts)