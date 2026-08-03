# 4. Palindrome Check 
# Check whether the entered string is a palindrome. 
str=input("enter a string : ")
rev=""

for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
if rev==str:
    print("pallindrome ")
else:
    print("not pallindrome")        