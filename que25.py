# 25.	Remove all duplicate elements while preserving the original order.
li=list(map(int,input("enter a list :").split()))
unique=[]
for i in set(li):
    unique.append(i)
print(unique)    