# 5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
names={"ram","shyam","sita","mira","radha"}
name=input("enetr name for search :")
if name in names:
    print(name,"exist")
else:
    print(name,"not exist")    