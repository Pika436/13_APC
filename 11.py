#11.10.	Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values.
'''Perform:
•	Find the average age. 
•	Find the oldest patient. 
•	Find the youngest patient. 
•	Display patients above 60 years.'''

import pandas as pd
patients = {
    101: 45,
    102: 67,
    103: 32,
    104: 78,
    105: 61
}
s = pd.Series(patients)

print("Patient Ages:")
print(s)

print("\nAverage Age:", s.mean())

print("\nOldest Patient:")
print("Patient ID:", s.idxmax())
print("Age:", s.max())

print("\nYoungest Patient:")
print("Patient ID:", s.idxmin())
print("Age:", s.min())

print("\nPatients above 60 years:")
print(s[s > 60])

