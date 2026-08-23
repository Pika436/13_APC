# 29.	Convert a tuple into a sorted tuple in ascending and descending order.
tup=(56,86,23,90,12,75)

ascending=tuple(sorted(tup))
descending=tuple(sorted(tup,reverse=True))

print("ascending order :",ascending)
print("descending order :",descending)