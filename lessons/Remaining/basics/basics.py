# ---------------------------------------------------------------
# How to use indexing -------------------------------------------
# ---------------------------------------------------------------

# Indexing starts from 0
# To get from the end us negative value
myString = "This string is fun"
myChar = myString[2]    #index of 2 will give us "i"
myNewString = myString[5:]      #it will create a string "string is fun"
myNewString2 = myString[5:11]   #it will create a string "string"


# ---------------------------------------------------------------
# How to use list and dictionary --------------------------------
# ---------------------------------------------------------------

mylist = [1,2,3,4,"he","she","they"]
mylist2 = [22.54,True,"long string",65]

#it creates a new list with all items of mylist and mylist2
longlist = mylist+mylist2 

# add item to list (it adds to the end)
mylist.append(142)

# remove items from list (removes from the end)
mylist.pop()

# Replace value my index
mylist[2] = "tall"


myDictionary = {
    "name":"myName",
    "Age":1,
    "Course":"BCA"
}

# Get value from key
name = myDictionary["name"]

# assign value to key
myDictionary["year"] = "2nd"


# ---------------------------------------------------------------
# How to loops --------------------------------------------------
# ---------------------------------------------------------------

# For loop
for i in range(0,10):   # i gets values 0 to 9 increasing by 1 every loop
    pass

# While loop
i=0
while i <10:    #loop through while the condition is true
    i+=1
    
# Loop through a list
mylist = [1,2,3,4,5]
for item in mylist:     #It assign item the value of each item in the list 
    pass

# Loop though a dictionary
myDictionary = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
}

for key,value in myDictionary.items():  
    # It assign key and value with the key and value of each item in dictionary
    pass



# ---------------------------------------------------------------
# How to use functions ------------------------------------------
# ---------------------------------------------------------------

# we use def to define a function
def myfunction1():
    print("this is inside a function")
    
# We call the function by its name
myfunction1()

# We can get values to a function my adding parameters inside () while defining
def myfunction2(a,b):
    print(f"a is {a}")
    print(f"b is {b}")
    
# We pass values to the function while calling the function
# by putting the values inside ()
myfunction2(2,19)


# We can get value from the function my using return 
def myfunction3(a,b):
    return a

# we need to assign a value to get the return value
result = myfunction3(56,23)