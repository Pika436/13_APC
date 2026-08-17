#8.	Store 15 integers in a list. Count how many numbers are:
'''•	Even 
•	Odd
'''

numbers=[]
for i in range(15):
    num=int(input("Enter a numers: "))
    numbers.append(num)

even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("EVEN : ",even," ODD : ",odd)                