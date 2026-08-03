# 5.Uppercase and Lowercase Count 
# Count the number of uppercase and lowercase letters in a string. 
str=input("enetr a string : ")
up=0
low=0
for ch in str:
    if ch.isupper():
        up+=1
    elif ch.islower():
        low+=1
print("lowercase :  ",low," uppercase : ",up)        
            