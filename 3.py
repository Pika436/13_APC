# 3.3.	Create a dictionary containing:
'''Product ID
Product Name
Category
Price
Quantity
Convert it into a DataFrame.
Calculate:
Total Amount = Price × Quantity
Then find the product having the highest total sales.'''
import pandas as pd
products={
    "id":[111,112,113,114,115],
    "name":["table","tv","chair","soap","pan"],
    "category":["furniture","electrical","furniture","grosary","kitchen"],
    "price":[4000,10000,2000,100,600],
    "quantity":[2,1,4,12,4]
}
df=pd.DataFrame(products)

df["total_amount"]=df["price"]*df["quantity"]
print("total amount :")
print(df[["id","name","total_amount"]])

highest_sale=df["total_amount"].max()
print("highest sale :")
print(df[df["total_amount"]==highest_sale])
