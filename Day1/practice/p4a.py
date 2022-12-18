#simple
product1CP = 1000
product1SP = 1200
product2CP = 810
product2SP = 1000
product1ProfitPercentage = (product1SP-product1CP)/product1CP*100
product2ProfitPercentage = (product2SP-product2CP)/product2CP*100

if (product1ProfitPercentage>product2ProfitPercentage):
    print(f"Product 1 \nCost:{product1CP}\nSell:{product1SP}\nProfit:{product1ProfitPercentage}%")
else:
    print(f"Product 2 \nCost:{product2CP}\nSell:{product2SP}\nProfit:{product2ProfitPercentage}%")
    
#Medium
p1CP = float(input("Enter product 1 CostPrice"))
p1SP = float(input("Enter product 1 SellPrice"))
p2CP = float(input("Enter product 2 CostPrice"))
p2SP = float(input("Enter product 2 SellPrice"))
p1PP = (p1SP-p1CP)/p1CP*100
p2PP = (p2SP-p2CP)/p2CP*100

if (p1PP>p2PP):
    print(f"Product 1 \nCost:{p1CP}\nSell:{p1SP}\nProfit:{p1PP}%")
else:
    print(f"Product 2 \nCost:{p2CP}\nSell:{p2SP}\nProfit:{p2PP}%")