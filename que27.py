# 27.	Store salaries of employees and determine:
'''
•	Highest salary 
•	Lowest salary 
•	Average salary 
•	Employees earning above ₹50,000 
•	Employees earning below ₹30,000 
'''

salary=[50000,60000,70000,80000,90000,55000,75000,2500,20000]
print("Highest salary :",max(salary))
print("lowest salary :",min(salary))
sum=0
for i in salary:
    sum=sum+i
avg=sum/len(salary)
print("Average salary :",avg)  

above=[]
below=[]
for i in salary:
    if i > 50000:
        above.append(i)
    elif i < 30000:
        below.append(i)
print("Employees earning above ₹50,000 :",above)
print("Employees earning below ₹30,000 :",below)        
              