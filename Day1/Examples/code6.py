# When passing a variable to a function the function creates a copy of the variable


def run(a,b):
    a = b+10
    print(f"a is {a}")

num1 = 2
num2 = 3
run(num1,num2)
print(f"num1 is {num1}")

# def run2(a,b):
#     a = b+10
#     print(f"a is {a}")
#     return a

# number1 = 2
# number2 = 3
# number1 = run2(number1,number2)
# print(f"number1 is {number1}")