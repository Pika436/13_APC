# merge two lists and remove duplicate 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = list(set(list1 + list2))

print(merged)