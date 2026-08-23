# 12.	Accept five numbers from the user, store them in a list, and convert the list into a tuple.
mylist=[]
for i in range(5):
    num=int(input("enter a number :"))
    mylist.append(num)
print("list :",mylist)
mytuple=tuple(mylist)
print("tuple :",mytuple)    
