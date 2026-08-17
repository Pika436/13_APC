# 14.	Create a list containing duplicate values and display only unique elements.
list=[10,20,30,49,10,60,70,40,30,20]
uni=[]
for num in list:
    if num not in uni:
        uni.append(num)
        
print("unique elements :",uni)        