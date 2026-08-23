# 14.	Create a tuple and delete it completely.
mytuple=(1,2,34,54,92)
mylist=list(mytuple)
mylist.clear()
mytuple=tuple(mylist)
print(mytuple)