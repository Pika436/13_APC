# 6.Write a program to find the largest and smallest number in a list without using max() or min().
li=[10,60,75,30,20]
small=li[0]
large=li[0]
for i in li:
    if(small > i):
        small=i
    elif (large<i):
        large=i   
print("small : ",small,"large : ",large)        