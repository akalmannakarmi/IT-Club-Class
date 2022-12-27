# ---------------------------------------------------------------
# How to declare varables ---------------------------------------
# ---------------------------------------------------------------
# We do not need to specify datatype in python
a = 2                   #Integer
b = 2.5                 #Float
c = True                #Bool
d = "My String"         #String
e = [2,5,4]             #List
f = {                   #Dictionary
    "name":"myName",
    "Age":1,
    "Course":"BCA"
}

# ---------------------------------------------------------------
# How to use string formating -----------------------------------
# ---------------------------------------------------------------
name = "Jack"
age = 15
course = "BCA"

# We can use + to add to strings together (concatenate)
# we use str(var) to convert the var to a string
introduction1 = "Hi I am "+name+",I am "+str(age)+" years old and I am studing "+course+"." 

# We can use f before the string to indicate it is a formated string
# which allows us to use {} to pass in variables inside
introduction2 = f"Hi I am {name},I am {age} years old and I am studing {course}." 

# We can use .format() to format the string 
# we use {key} to be a placeholder for varable and later assign value by
# assigning the key with a value in .format() 
introduction3 = "Hi I am {n},I am {a} years old and I am studing {c}.".format(n=name,a=age,c=course)


# ---------------------------------------------------------------
# How to use char in string -------------------------------------
# ---------------------------------------------------------------

singleQuotes = 'Sam said"We can Code!!".'
escapeCharacter = "Ram said\"We can Code!!\"."
Multiline = """
    I can write multi-line string here
    Truly its great
    to use this feature
    Ram said"We can Code!!".
"""
tabCharacter = "Name \tAge"  #\t creates a tab spaces 
nextLineCharacter = "Name \n myName" #\n creates a new line


# ---------------------------------------------------------------
# How to use if elseif else -------------------------------------
# ---------------------------------------------------------------
condition1 = True

if condition1:  #if condition1 is true
    pass
else:           #if condition1 is not true 
    pass 

if (1>2 or 2=="2"): # if 1>2 or 2=="2"
    pass
elif(34>=25 and 46 <= 106): #If previous conditions not satisfied and 34>=25 and 46<=106
    pass
else:   #If all of the conditions are not satisfied
    pass
