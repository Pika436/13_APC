# 28.	Count the frequency of each element in a tuple.
tup=(45,2,98,9,8,55,2,9,34,2,1)

frequency={}
for item in tup:
    if item not in frequency:
        frequency[item] = 1
    else:
        frequency[item]+=1
print("frequency of each element :",frequency)            