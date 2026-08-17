# 13.	Accept 10 numbers and sort them in:
'''•	Ascending order 
•	Descending order
'''

numbers=[]
for i in range(10):
    num=int(input("enter a number :"))
    numbers.append(num)

numbers.sort()
print("ascending order :",numbers)

numbers.reverse()
print("descending order :",numbers)    