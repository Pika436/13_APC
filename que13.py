#13.	Shortest Word 
# a.	Find the shortest word in a sentence. 
s=input("enter a string : ")
word=s.split()
small=word[0]
for words in word:
    if len(small)>len(words):
        small=words
        
print("smallest word : ",small)        