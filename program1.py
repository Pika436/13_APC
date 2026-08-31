#  Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file. 


name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write("Student Name: " + name + "\n")
    file.write("Roll Number: " + roll_no + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")

print("Student details written successfully.")