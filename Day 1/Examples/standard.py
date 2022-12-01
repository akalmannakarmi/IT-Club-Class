# Import requred here
import time

# Declare global variables
PI = 3.14
g = 10
name = "Your Name"

# Declare functions
def add(a,b):
    return a+b

def run():
    num1 = input("Enter First number:")
    num2 = input("Enter Second number:")
    
    sum = add(num1,num2)
    
    print(f"Sum of {num1} and {num2} is {sum}")
    
    
# Execute if this is the main process or sth like that
if __name__ == "__main__":
    run()