# 23.	Count the frequency of each element in a list.
list=list(map(int,input("enetr a list :").split()))
for i in set(list):
    print(i,":",list.count(i))
