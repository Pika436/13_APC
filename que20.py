#20.	Count Occurrences of a Word 
# a.	Count how many times a specific word appears in a sentence. 
s=input("enter a string : ")
search=input("enter element to search : ")
word=s.split()
count=0
for words in word:
    if words==search:
        count+=1
        
print("frequency : ",count)        
    