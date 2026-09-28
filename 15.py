# 15.	Create two NumPy arrays and concatenate them horizontally and vertically. 
import numpy as np
A=np.array([[1,2,3],
            [4,5,6]])
B=np.array([[7,8,9],
           [3,2,1]])

horizontal=np.hstack((A,B))
vertical=np.vstack((A,B))

print("array A :")
print(A)
print("array B :")
print(B)
print(" horizontal concatination :")
print(horizontal)
print("verticle concatination :")
print(vertical)