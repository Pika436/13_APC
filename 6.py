# 6.	Create two 3 × 3 NumPy matrices and perform matrix addition.
import numpy as np
A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
B=np.array([[9,8,7],
            [6,5,4],
            [3,2,1]])
C=A+B

print("matrix A :")
print(A)
print("matrix B :")
print(B)
print("addition :")
print(C)