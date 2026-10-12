# 7.7.	A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity.
'''Write a Python program to:
1.	Convert the dictionary into a Pandas DataFrame. 
2.	Add a new column Total_Sales. 
3.	Calculate the total sales using Price × Quantity. 
4.	Display products with sales greater than ₹10,000. 
5.	Find the product with maximum sales. 
6.	Calculate the average sales.'''


import pandas as pd

products = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Chair", "Table", "Headphones"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture", "Electronics"],
    "Price": [50000, 15000, 2000, 6000, 1000],
    "Quantity": [2, 3, 4, 2, 5]
}

df = pd.DataFrame(products)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Product Sales Data:")
print(df)

print("\nProducts with sales greater than Rs. 10000:")
high_sales = df[df["Total_Sales"] > 10000]
print(high_sales)

max_sales = df["Total_Sales"].max()

print("\nProduct with Maximum Sales:")
print(df[df["Total_Sales"] == max_sales])

avg_sales = df["Total_Sales"].mean()

print("\nAverage Sales:", avg_sales)
