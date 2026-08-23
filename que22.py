# 22.	Create two sets representing technical skills of two employees. Find:
'''
•	Common skills 
•	Skills unique to Employee 1 
•	Skills unique to Employee 2 
•	All available skills
'''

emp1={"python","java","c","c++"}
emp2={"python","ml","ruby","sql"}

common=emp1.intersection(emp2)
uni1=emp1.difference(emp2)
uni2=emp2.difference(emp1)
all=emp1.union(emp2)

print("Common skills :",common)
print("Skills unique to Employee 1 :",uni1)
print("Skills unique to Employee 2 :",uni2)
print("All available skills :",all)