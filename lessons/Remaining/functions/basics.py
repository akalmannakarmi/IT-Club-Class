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