# 15.	Write a program to determine whether two sets have no elements in common.
s1={12,23,34,56}
s2={76,54,43,32}
if s1.isdisjoint(s2):
    print("sets have no element in comman")
else:
    print("sets have common elements")    