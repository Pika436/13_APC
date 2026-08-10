#17.	Anagram Check 
# a.	Check whether two strings are anagrams. 
s1=input("enetr a string 1 : ")
s2=input("enetr a string 2 : ")
if sorted(s1)==sorted(s2):
    print("anagrams")
else:
    print("not anagrams")    