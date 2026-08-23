# 13.	Modify a tuple by converting it into a list and then back into a tuple
mytuple=(1,2,3,4,5,5)
print("original tuple :",mytuple)
mylist=list(mytuple)
mylist.append(80)
print("list :",mylist)

mytuple=tuple(mylist)
print("modified tuple :",mytuple)