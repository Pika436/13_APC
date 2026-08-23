# 20.	Accept a number from the user and determine whether it exists in the tuple.
numbers=()
n=int(input("enter no. of elements :"))
for i in range(n):
    num=int(input("enter number :"))
    numbers=numbers+(num,)
search=int(input("enter element to search :"))
if search in numbers:
    print("exist")
else:
    print("not exist")        