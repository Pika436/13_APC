# 13.Dataset: students.csv
'''Columns:
Student_ID,Name,Department,Python,DBMS,Maths
Problem Statement:
Read students.csv using Pandas and perform the following:
1.	Display the first 5 records. 
2.	Display the last 5 records. 
3.	Find the total and average marks of each student. 
4.	Display students whose average marks are greater than 75. 
5.	Find the student with the highest average. 
6.	Find the average marks for each subject. '''


import pandas as pd
df = pd.read_csv(
    r"C:\Users\Premkumar\OneDrive\Desktop\TY\Python\Pandas\students.csv"
)
print("First 5 Records:")
print(df.head(5))

print("\nLast 5 Records:")
print(df.tail(5))

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with Average Marks Above 75:")
print(df[df["Average"] > 75])

highest = df["Average"].max()

print("\nStudent with Highest Average:")
print(df[df["Average"] == highest])

print("\nAverage Marks of Each Subject:")
print(df[["Python", "DBMS", "Maths"]].mean())

