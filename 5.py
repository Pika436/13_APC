# 5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
'''•	2 × 6 matrix 
•	3 × 4 matrix 
•	4 × 3 matrix
'''

import numpy as np
arr=np.arange(1,13)

print("original array :",arr)
print("\n2*6 matrix :")
print(arr.reshape(2,6))

print("\n3*4 matrix :")
print(arr.reshape(3,4))

print("\n4*3 matrix :")
print(arr.reshape(4,3))