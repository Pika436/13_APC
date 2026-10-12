#10.9.	Create a Pandas Series using a dictionary containing product names and prices.
'''Perform:
•	Display all products and prices. 
•	Increase every price by 10%. 
•	Find the most expensive product. 
•	Find products costing more than ₹1,000. '''


import pandas as pd
products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Headphones": 2000,
    "Pendrive": 800
}

s = pd.Series(products)

print("Products and Prices:")
print(s)

s = s * 1.10
print("\nPrices after 10% Increase:")
print(s)

print("\nMost Expensive Product:")
print(s.idxmax(), ":", s.max())

print("\nProducts costing more than Rs. 1000:")
print(s[s > 1000])

