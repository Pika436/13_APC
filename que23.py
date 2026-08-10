# 23.	String Compression 
# •	Compress repeated characters and return the original string if compression does not reduce the length. 

s=input("enetr a string : ")
result=""
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        result=result+s[i]+str(count)
        count=1
result=result+s[-1]+str(count)
if len(result)>len(s):
    print(s)
else:
    print(result)                