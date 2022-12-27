# 3) Create a program to print the sum,difference,multiplication,division of a = 10 , b = 2.

# Simple answer ---------------------------------------------------------
a = 10
b = 2
sum = a+b
diff = a-b
multi = a*b
divi = a/b

print(f"Sum = {sum}")
print(f"Difference = {diff}")
print(f"Multiplication = {multi}")
print(f"Division = {divi}")

# Medium answer ---------------------------------------------------------
a = 10
b = 2

def printOperations(a,b):
    print(f"Sum = {a+b}")
    print(f"Difference = {a-b}")
    print(f"Multiplication = {a*b}")
    print(f"Division = {a/b}")

printOperations(a,b)