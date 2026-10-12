# 14. Dataset: employees.csv
'''Columns:
Employee_ID,Name,Department,Experience,Salary
Problem Statement:
Read the CSV file and:
1.	Display employees from the CSE department. 
2.	Find the average salary. 
3.	Find the highest and lowest salary. 
4.	Display employees having salary greater than ₹50,000. 
5.	Calculate department-wise average salary. '''


import pandas as pd
df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

print("\nEmployees from CSE Department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

print("\nEmployees with Salary Greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())

