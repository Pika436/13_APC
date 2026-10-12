# 4.4.	Create a dictionary containing:
'''Patient ID
Patient Name
Age
Disease
Medical Charges
Convert the dictionary into a DataFrame and:
1.	Display patients above 60 years. 
2.	Find the average medical charge. 
3.	Find the maximum medical charge. 
4.	Display patients whose medical charges are greater than ₹50,000. '''

import pandas as pd
patients={
    "id":[2,3,4,5,6],
    "name":["ramu","sany","riya","ronny","rupa"],
    "age":[40,50,60,66,80],
    "disease":["fewer","cold","flue","corola","disentry"],
    "charges":[12000,10000,20000,40000,55000]
}
df=pd.DataFrame(patients)
print("patient data :")
print(df)

above=df[df["age"]>60]
print("\npatients above 60 years :")
print(above)

avg=df["charges"].mean()
print("\navreage charges :",avg)

maxi=df["charges"].max()
print("\nmaximum charges :",maxi)

greater=df["charges"].max()
print("highest charges :")
print(df[df["charges"]==greater])