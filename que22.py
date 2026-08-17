# 22.	Find common elements between two lists.
l1=list(map(int,input("enetr first list :").split()))
l2=list(map(int,input("enter second list :").split()))
new=[]
for i in l1:
    if i in l2:
        new.append(i)  
print(new)          
        
    