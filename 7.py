# 7.Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.

import numpy as np
A=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
B=np.array([[10,11],
           [12,13],
           [14,15]])

C=np.matmul(A,B)

print("matrix A :")
print(A)
print("matrix B :")
print(B)
print("multiplication :")
print(C) 