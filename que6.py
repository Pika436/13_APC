# 6.	Create a tuple with repeated numbers and count how many times a particular number appears.
num=(1,2,3,4,5,6,1,6,4,8,3,2,9,4,6,4,2)
for n in set(num):
    print(n,":",num.count(n))
    
