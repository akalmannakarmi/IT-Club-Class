# 6) Create a program to input any two number and an operator(+,-,*,/)
# and perfrom the specified operation and print the result. 

# Easy answer---------------------------------------------------------
firstNo = input("Enter First number: ")
secondNo = input("Enter Second number: ")
operator = input("Enter Operator: ")
firstNo = int(firstNo)
secondNo = int(secondNo)

if operator == "+":
    sum = firstNo + secondNo
    print(sum)
elif operator == "-":
    diff = firstNo - secondNo
    print(diff)
elif operator == "*":
    multi = firstNo * secondNo
    print(multi)
elif operator == "/":
    divi = firstNo / secondNo
    print(divi)
    
# Medium answer---------------------------------------------------------
def calculate():
    firstNo = input("Enter First number: ")
    secondNo = input("Enter Second number: ")
    operator = input("Enter Operator: ")
    firstNo = int(firstNo)
    secondNo = int(secondNo)

    if operator == "+":
        result = firstNo + secondNo
    elif operator == "-":
        result = firstNo - secondNo
    elif operator == "*":
        result = firstNo * secondNo
    elif operator == "/":
        result = firstNo / secondNo
    return result

print(calculate())

# Hard answer---------------------------------------------------------
def getInput():
    while True:
        try:
            firstNo = input("Enter First number: ")
            firstNo = int(firstNo)
            break
        except:
            print("Invalid input")
    while True:
        try:
            secondNo = input("Enter Second number: ")
            secondNo = int(secondNo)
            break
        except:
            print("Invalid input")
    while True:
        operator = input("Enter Operator: ")
        if operator == "+" or operator =="-" or operator == "*" or operator =="/":
            break
        print("Invalid Operator")
        
    return firstNo,secondNo,operator
    
def calc(firstNo,secondNo,operator):
    result = 0
    if operator == "+":
        result = firstNo + secondNo
    elif operator == "-":
        result = firstNo - secondNo
    elif operator == "*":
        result = firstNo * secondNo
    elif operator == "/":
        result = firstNo / secondNo
    return result

def run():
    (num1,num2,op)=getInput()
    result = calc(num1,num2,op)
    print(result)
    
run()