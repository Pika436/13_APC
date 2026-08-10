#12.Longest Word 
# Find the longest word in a given sentence. 
s=input("enter a string : ")
word=s.split()
large=word[0]
for words in word:
    if len(large)<len(words):
        large=words
print("largest element : ",large)        