# 6.6.	Create a dictionary containing:
'''Student_ID
Name
Department
Total_Classes
Classes_Attended
Create a DataFrame and calculate:
Attendance Percentage = (Classes_Attended / Total_Classes) × 100
Display students whose attendance is below 75%.'''


import pandas as pd
students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Prachi", "Rahul", "Sneha", "Amit", "Priya"],
    "Department": ["CSE", "IT", "AIML", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 120, 80, 100],
    "Classes_Attended": [90, 65, 80, 50, 75]
}

df = pd.DataFrame(students)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("All Student Data:")
print(df)

print("\nStudents with attendance below 75%:")
low_attendance = df[df["Attendance_Percentage"] < 75]
print(low_attendance)
