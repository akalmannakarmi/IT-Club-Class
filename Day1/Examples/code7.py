# Variable in different functions can have same names


def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    result = num1-num2
    return result

def multiply(num1,num2):
    result = num1 * num2
    return result


num1 = 10
num2 = 4

print(f"{num1} + {num2} = {add(num1,num2)}")

sub = substract(num1,num2)
print(f"{num1} + {num2} = {sub}")

mult = multiply(num1,num2)
print(f"{num1} + {num2} = {mult}")