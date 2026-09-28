# 8.	Create a 3 × 4 matrix and display its transpose.
import numpy as np
A=np.array([[1,2,3],
          [4,5,6],
          [7,8,9]])
T=A.T 

print("original matrix :")
print(A)
print("transpose of matrix :")
print(T)