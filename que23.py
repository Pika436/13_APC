# 23.	Store item prices in a tuple and calculate:
'''
•	Total bill 
•	Average price 
•	Highest-priced item 
•	Lowest-priced item
'''
prices=(500,6000,5400,800,960,1000)

total=sum(prices)
avg=total/len(prices)
high=max(prices)
low=min(prices)

print("total bill :",total)
print("Average price :",avg)
print("Highest-priced item :",high)
print("Lowest-priced item :",low)