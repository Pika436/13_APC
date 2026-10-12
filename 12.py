# 12.Create a Pandas Series using a dictionary containing student names and attendance percentages.
'''Perform:
•	Find the average attendance. 
•	Display students with attendance below 75%. 
•	Display students with attendance above 90%. 
•	Find the highest attendance'''


import pandas as pd
students = {
    "Prachi": 95,
    "Rahul": 68,
    "Sneha": 92,
    "Amit": 74,
    "Priya": 85
}

s = pd.Series(students)

print("Student Attendance:")
print(s)

print("\nAverage Attendance:", s.mean())

print("\nAttendance below 75%:")

print("\nAttendance above 90%:")
print(s[s > 90])

print("\nHighest Attendance:", s.max())
print("Student Name:", s.idxmax())

