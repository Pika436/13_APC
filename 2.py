# 2. 2.	Create a dictionary containing:
''' 
Employee ID
Employee Name
Department
Salary
Experience
Convert it into a Pandas DataFrame and:
1.	Display employees with salary greater than ₹50,000. 
2.	Find the average salary. 
3.	Find the highest salary. 
4.	Find the employee with the highest experience.'''

import pandas as pd
emp={
    "id":[11,22,33,44,55],
    "name":["sanju","raju","neha","rupa","priya"],
    "dept":["it","entc","civil","aiml","cse"],
    "salary":[40000,50000,98500,87432,90000],
    "experience":[4,8,2,7,6]
}
print("employee data :")
df=pd.DataFrame(emp)

print("salary greater than 50000 :")
high=df[df["salary"]>50000]
print(high)

avg=df["salary"].mean()
print("\naverage salary is :",avg)

highest=df["salary"].max()
print("\nhighest salary :",highest)

experience=df[df["experience"]==df["experience"].max()]
print("\nhighest experience :")
print(experience)
