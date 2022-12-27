# Simple
a = 2
b = 3
c = 5
d = 7
e = 4
average = (a+b+c+d+e)/5
print(f"Average :{average}")

# medium
a = input("Enter a num")
b = input("Enter a num")
c = input("Enter a num")
d = input("Enter a num")
e = input("Enter a num")
average = (a+b+c+d+e)/5
print(f"Average :{average}")

# Good
average = 0
for i in range(0,5):
    average += input("Enter a num")
average = average/5
print(f"Average :{average}")
