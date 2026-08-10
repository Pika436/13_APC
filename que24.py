# 24.	Most Frequent Character 
# •	Find the character with the highest frequency. 

s=input("enetr a string : ")
max_char=""
max_freq=0
for ch in s:
    count=s.count(ch)
    if count>max_freq:
        max_freq=count
        max_char=ch
print("most frequent character : ",max_char)
print("frequency : ",max_freq)        