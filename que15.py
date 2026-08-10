#15.	Duplicate Characters 
# a.	Print all duplicate characters in a string. 
s=input("enter a string : ")
new=""
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j] and s[i] not in new:
            print(s[i])
            new+=s[i]