# 19.	Store 15 integers in a tuple and count:
'''•	Even numbers 
•	Odd numbers
'''

mytuple=(2,4,5,6,7,8,9,11,33,43,45,66,21,54,55)
even=0
odd=0
for i in range(len(mytuple)):
    if i%2==0:
        even+=1
    else:
        odd+=1

print("even numbers :",even)
print("odd numbers :",odd)            