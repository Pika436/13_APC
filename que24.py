# 24.	Store temperatures of seven days in a tuple and determine:
'''
•	Maximum temperature 
•	Minimum temperature 
•	Average temperature 

'''
temp=(11,12,30,28,26,24,22)

max=max(temp)
mini=min(temp)
total=sum(temp)
avg=total/len(temp)

print("Maximum temperature :",max)
print("Minimum temperature :",mini)
print("Average temperature :",avg)