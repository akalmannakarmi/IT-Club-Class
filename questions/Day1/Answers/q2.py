# 2) Create a program to print the values of a = 10,b=25.42,c="cat",d=TRUE.

# simple answer---------------------------------------------------------
a = 10
b = 25.42
c = "cat"
d = True

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")


# Medium answer---------------------------------------------------------
a = 10
b = 25.42
c = "cat"
d = True

def printVals():
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")

printVals()


# Hard answer---------------------------------------------------------
a = 10
b = 25.42
c = "cat"
d = True

def printVals(a,b,c,d):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")

printVals(a,b,c,d)
