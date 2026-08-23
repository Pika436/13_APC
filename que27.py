# 27.	Merge two tuples and remove duplicate elements.
tup1=(34,78,6,12,34)
tup2=(42,45,12,34,7,9,78)

merged=()
for item in tup1+tup2:
    if item not in merged:
        merged += (item,)
        
print("merged tuple :",merged)        