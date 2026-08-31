# 3. Write a program to append additional student information to an existing file without deleting its previous contents. 

with open("student.txt",'a') as f:
    f.write("\nstudent name :ram\n")
    f.write("Roll Number :23\n")
    f.write("Branch :cse\n")
    f.write("semester :6\n")
print("additional student information added")    
    