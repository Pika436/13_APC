# 11.Word Count 
# 	Count the total number of words in a sentence. 
str=input("Enter a string : ")
count=1
for ch in str:
    if ch==" ":
        count+=1
print("total word = ",count)        