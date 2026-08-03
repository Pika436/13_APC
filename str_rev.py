# 3.Reverse a String
# Reverse the given string without using built-in reverse functions. 
str=input("enter a string : ")
rev=" "
for ch in range(len(str)-1,-1,-1):
    rev=rev+str[ch]
    
print("reversed string : ",rev)        