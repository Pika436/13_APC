# 5.	Create a list of student names. Remove:
'''
•	First student 
•	Last student 
•	A specific student by name 
Display the remaining list.
'''
stu=["ram","shyam","sita","gita","mayur","rani"]
stu.remove("sita") #specified
stu.pop() #last
stu.pop(0) #first
print(stu)