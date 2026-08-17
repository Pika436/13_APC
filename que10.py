# 10.	Write a program to reverse a list without using the reverse() method.
list=[1,2,3,4,5,6,7]
rev=[]
for i in range(len(list)-1,-1,-1):
    rev.append(list[i])
print("original list :",list )
print("reverced list :",rev)    
    