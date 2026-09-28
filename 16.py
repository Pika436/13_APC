# 16.	Store marks of 10 students in a NumPy array. Calculate:
'''
•	Highest marks 
•	Lowest marks 
•	Average marks 
•	Median 
•	Standard deviation
'''

import numpy as np
arr=np.array([20,30,40,50,60,70,80,90,35,67])

print("highest :",np.max(arr))
print("lowest marks :",np.min(arr))
print("average marks :",np.mean(arr))
print("madian :",np.median(arr))
print("std :",np.std(arr))
