# 11.	Convert a tuple into a list and add a new element.
mytuple=(3,5,7,8,9)
print("original :",mytuple)
mylist=list(mytuple)
mylist.append(100)
mytuple=tuple(mylist)
print("new :",mytuple)