# 30.	String Rotation 
'''•	Check whether one string is a rotation of another. 
•	Example:
•	ABCD
•	CDAB
Output: Yes
'''

s1=input("enter first string : ")
s2=input("enetr second string : ")
if len(s1)==len(s2) and s2 in s1 +s1:
    print("yes")
else:
    print("no")    