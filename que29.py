# 29.	Sentence Reversal 
'''•	Reverse the order of words in a sentence without changing the words themselves. 
•	Example:
•	Input: Python is easy
Output: easy is Python
'''

s=input("entre a string : ")
word=s.split()
word.reverse()
print(" ".join(word))