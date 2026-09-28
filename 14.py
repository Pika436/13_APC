# 14.	Create an array containing duplicate values. Find and display only the unique elements.
import numpy as np
arr=np.array([10,20,30,40,50,60,40,30])
unique_arr=np.unique(arr)
print("original array :",arr)
print("unique element :",unique_arr)