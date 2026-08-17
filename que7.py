# 7.	Accept 10 numbers from the user and store them in a list. Calculate:
'''•	Sum 
   •	Average 
'''
list=[]
for i in range(10):
    num=int(input("enter an number : "))
    list.append(num)

sum=0
for num in list:
    sum=sum+num
    
avg=sum/10
print("sum :",sum," avg :",avg)        