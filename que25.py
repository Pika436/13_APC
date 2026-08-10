#25.	Second Most Frequent Character 
# •	Find the second most frequently occurring character. 

s=input("enetr a string : ")
first=0
second=0
first_ch=""
second_ch=""
for ch in s:
    count=s.count(ch)
    if count>first:
        second=first
        second_ch=first_ch
        
        first=count
        first_ch=ch
    elif (count>second and count!=first) :
        second=count
        second_ch=ch
print("second most frequent character : ",second_ch)
print("frequency : ",second)        