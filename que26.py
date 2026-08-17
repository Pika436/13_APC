# 26.	Store marks of 20 students in a list and determine:
'''
•	Highest marks 
•	Lowest marks 
•	Average marks 
•	Number of students scoring above average 
•	Number of students scoring below average
'''

marks=[80,70,90,60,98,40,65,35,55,69,99,77,89,50,84,79,84,72,49,30]
print("highest marks :",max(marks))
print("lowest marks :",min(marks))

sum=0
above=[]
below=[]
for i in marks:
    sum=sum+i
avg=sum/20
print("average marks :",avg)
for i in marks:
    if i > avg:
        above.append(i)
    else:
        below.append(i)
print("Number of students scoring above average :",len(above))
print("Number of students scoring below average :",len(below))            
    