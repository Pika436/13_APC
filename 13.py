# 13.	Create an unsorted NumPy array and display it in:
'''
•	Ascending order 
•	Descending order
'''

import numpy as np
arr=np.array([89,65,23,11,45,27])

asc=np.sort(arr)
desc=np.sort(arr)[::-1]

print("original array :",arr)
print("ascending order :",asc)
print("descending order :",desc)