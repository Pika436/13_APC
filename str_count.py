# 2.Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
str=input("Enter a string : ")
vo=0
con=0
dig=0
sp=0
for ch in str:
    if ch in "aeiouAEIOU":
        vo+=1
    elif ch.isalpha():
        con+=1
    elif ch.isdigit():
        dig+=1
    else:
        sp+=1
print("vowels: ",vo," consonent: ",con," digit: ",dig," special character : ",sp)                    