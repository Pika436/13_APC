# 18.	Calculate the average of elements stored in a tuple.
mytup=(2,4,5,7,9,11,21,42)
sum=0
for i in mytup:
    sum=sum+i
print("sum :",sum)  
avg=sum/len(mytup)
print("average :",avg)  