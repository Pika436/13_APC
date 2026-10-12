# 5.5.	Create a dictionary containing:
'''Order_ID
Customer
Product
Quantity
Price
Discount
Create a DataFrame and calculate:
Final Amount = Quantity × Price − Discount
Then display:
•	All orders 
•	Orders above ₹5,000 
•	Highest-value order 
•	Average order value '''


import pandas as pd

orders = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Prachi", "Rahul", "Sneha", "Amit", "Priya"],
    "Product": ["Laptop", "Mobile", "Headphones", "Tablet", "Monitor"],
    "Quantity": [1, 2, 3, 1, 2],
    "Price": [60000, 20000, 2000, 15000, 12000],
    "Discount": [5000, 2000, 500, 1000, 1500]
}

df = pd.DataFrame(orders)

df["Final Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above Rs. 5000:")
print(df[df["Final Amount"] > 5000])

highest = df["Final Amount"].max()
print("\nHighest-value Order:")
print(df[df["Final Amount"] == highest])

average = df["Final Amount"].mean()
print("\nAverage Order Value:", average)
