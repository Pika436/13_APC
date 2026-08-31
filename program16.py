# 16. Read a text file and create another file containing the same text in uppercase. 
with open("student.txt", "r") as file:
    content = file.read()

with open("uppercase.txt", "w") as file:
    file.write(content.upper())

print("File created successfully.")