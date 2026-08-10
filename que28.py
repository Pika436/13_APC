# 28.	Word Frequency Dictionary 
# •	Count the frequency of every word in a paragraph. 

s=input("enter a string : ")
words=s.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)            