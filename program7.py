# 7. Write a program to count the total number of characters in a text file, including spaces. 

with open("student.txt", "r") as file:
    content = file.read()

characters = len(content)

print("Total number of characters:", characters)