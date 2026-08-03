#8.	Frequency of a Character 
# Find the number of times a specified character appears in a string. 
str=input("enetr a string : ")
ch=input("enter character to search : ")
count=0
for i in str:
    if i==ch:
        count+=1
print("frequency : ",count)            
