# 11.	Create two sets and find:
'''
•	Elements present in the first set but not the second 
•	Elements present in the second set but not the first
'''

set1={23,34,12,43,12}
set2={12,23,34,45}
first=set1.difference(set2)
second=set2.difference(set1)
print("Elements present in the first set but not the second :",first)
print("Elements present in the second set but not the first :",second)