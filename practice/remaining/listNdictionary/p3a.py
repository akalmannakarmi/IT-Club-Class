# Medium
costs = []

for i in range(0,10):
    cost = int(input("Enter Product Cost: "))
    
    costs.append(cost)
    
cheepest = costs[0]
expensive = 0
for cost in costs:
    if cost < cheepest:
        cheepest = cost
    if cost > expensive:
        expensive = cost
        
print(cheepest)
print(expensive)

# Short
costs = []

for i in range(0,10):
    cost = int(input("Enter Product Cost: "))
    
    costs.append(cost)
    
costs.sort()

print(costs[0])
print(costs[-1])
print(costs)