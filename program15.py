# 15. Read a Python source file and create another file after removing single-line comments. 
with open("program.py", "r") as file:
    lines = file.readlines()

with open("new_program.py", "w") as file:
    for line in lines:
        if "#" in line:
            line = line.split("#")[0]
        file.write(line)

print("Comments removed successfully.")