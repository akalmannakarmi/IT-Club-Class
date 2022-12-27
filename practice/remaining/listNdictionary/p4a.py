# Medium
products = {}

for i in range(0,5):
    name = input("Enter Product Name: ")
    cost = int(input("Enter Product Cost: "))
    
    products[name]=cost
    
expensive = 0
expensiveName = ''
for name,cost in products.items():
    if cost > expensive:
        expensive = cost
        expensiveName = name
        
print(expensiveName)
