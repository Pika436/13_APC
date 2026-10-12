# 9.8.	Create a Pandas Series using a dictionary containing employee names and their salaries.
'''Perform:
•	Display the Series. 
•	Find the highest salary. 
•	Find the lowest salary. 
•	Calculate average salary. 
•	Display employees earning more than ₹50,000.'''


import pandas as pd
employees = {
    "Prachi": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Amit": 35000,
    "Priya": 55000
}

s = pd.Series(employees)

print("Employee Salaries:")
print(s)

print("\nHighest Salary:", s.max())

print("Lowest Salary:", s.min())

print("Average Salary:", s.mean())

print("\nEmployees earning more than Rs. 50000:")
print(s[s > 50000])

