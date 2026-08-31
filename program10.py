# 10. Read a text file and calculate the number of alphabets, digits, spaces, and special characters

with open("student.txt",'r') as f:
    content=f.read()
alpha=0
digit=0
space=0
special=0
for ch in content:
    if ch.isalpha():    
        alpha+=1
    elif ch.isdigit():
        digit+=1
    elif ch.isspace():
        space+=1
    else:
        special+=1

print("total alphabets :",alpha) 
print("total digits:",digit) 
print("total space :",space) 
print("total special character :",special) 
                   