# 1.Write a program to input a string and display its length without using the len() function. 
str=input("Enter a string : ")
count=0
for ch in str:
    if ch in str:
        count+=1
print("length of string : ",count)
        