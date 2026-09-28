# 10.	Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
import numpy as np
arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [8,9,10,11],
              [12,13,14,15]])

row_sum=np.sum(arr,axis=1)
col_sum=np.sum(arr,axis=0)

print("matrix")
print(arr)
print("sum of each row :")
print(row_sum)
print("sum of each column :")
print(col_sum)