
# 1. 1.	Create a dictionary containing the following information for 5 students:
'''•	Student ID 
•	Student Name 
•	Python Marks 
•	DBMS Marks 
•	Mathematics Marks 
Convert the dictionary into a Pandas DataFrame and:
1.	Display the DataFrame. 
2.	Calculate total marks for each student. 
3.	Calculate average marks. 
4.	Display students who scored more than 75% average.
'''
import pandas as pd
students={
    "ID":[22,23,24,25,26],
    "p_marks":[90,98,68,88,81],
    "d_marks":[78,54,77,28,90],
    "m_marks":[90,99,89,70,89]
}
df=pd.DataFrame(students)
print("student data :")
print(df)

df["total"]=df["p_marks"]+df["d_marks"]+df["m_marks"]
print("\ntotal marks :")
print(df[["ID","total"]])

df["avg"]=df["total"]/3
print("\naverage marks :")
print(df[["ID","avg"]])

print("\nscoring above 75% :")
result=df[df["avg"]>75]
print(result)
