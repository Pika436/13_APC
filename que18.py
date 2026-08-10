#18.	Remove Duplicate Characters 
# a.	Remove duplicate characters while maintaining the original order. 
s=input("enetr a string : ")
result=""
for ch in s:
    if ch not in result:
        result+=ch
print("new string : ",result)        