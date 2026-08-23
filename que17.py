# 17.	Find the largest and smallest number in a tuple without using max() and min().
mytuple=(12,34,78,54,19,86)
max=mytuple[0]
min=mytuple[0]
for i in mytuple:
    if max < i:
        max=i
    elif min > i:
        min=i
        
print("max :",max)
print("min :",min)            