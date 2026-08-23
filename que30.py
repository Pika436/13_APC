# 30.	Create a tuple containing patient records:
'''
•	Patient ID 
•	Name 
•	Age 
•	Blood Group 
Perform the following operations:
•	Display all records 
•	Search for a patient by ID 
•	Count the total number of patients 
•	Display patients with a specific blood group 
'''

patient=(
    (11,"ram",20,"O+"),
    (12,"joya",21,"A+"),
    (22,"nayan",31,"AB+")
)
print("all record :")
for i in patient:
    print(i)
    
id=12
for i in patient:
    if i[0]==id:
        print("patient found :",i)
     
print("total patient :",len(patient))

print("A+ blood group patients:")
for i in patient:
    if i[3] == "A+":
        print(i)        