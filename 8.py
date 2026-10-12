# 8. .	Create a Pandas Series using a dictionary where the student names are keys and their marks are values.
'''Perform:
•	Display the Series. 
•	Display marks of a particular student. 
•	Find maximum and minimum marks. 
•	Calculate the average marks. 
•	Display students who scored more than 75'''


import pandas as pd

# Create a dictionary
students = {
    "Prachi": 85,
    "Rahul": 68,
    "Sneha": 92,
    "Amit": 74,
    "Priya": 80
}

s = pd.Series(students)

print("Student Marks:")
print(s)

print("\nMarks of Sneha:", s["Sneha"])

print("\nMaximum Marks:", s.max())
print("Minimum Marks:", s.min())

print("\nAverage Marks:", s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])
