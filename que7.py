# 7.	Create a tuple of employee IDs and find the index of a given ID.
ids=[101,102,200,300,303,104,400]
id=int(input("enter id to find index :"))
if id in ids:
    print("index :",ids.index(id))