# 20.	Create a (2, 3, 4) array and calculate:
'''•	Sum of all elements 
•	Sum of each layer 
•	Sum along rows 
•	Sum along columns
'''

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

total = np.sum(arr)

layer_sum = np.sum(arr, axis=(1, 2))

row_sum = np.sum(arr, axis=1)

col_sum = np.sum(arr, axis=2)

print("3D Array:")
print(arr)

print("Sum of all elements:", total)
print("Sum of each layer:", layer_sum)
print("Sum along rows:")
print(row_sum)
print("Sum along columns:")
print(col_sum)