# 24.	Rotate a list:
'''
•	Left by one position 
•	Right by one position
'''

list=list(map(int,input("Enter a list :").split()))
left=list[1:]+list[:1]
right=list[-1:]+list[:-1]
print("original list :",list)
print("Left by one position :",left)
print("Right by one position :",right)