#2. Write a program to open a text file and display its complete contents. 
with open("student.txt",'r') as f:
    content=f.read()
    print(content)