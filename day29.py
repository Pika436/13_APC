# 29.	Store the temperature of 30 days and determine:
'''
•	Hottest day 
•	Coldest day 
•	Average temperature 
•	Days above average temperature 
•	Days below average temperature
'''

temp=[30,20,10,22,29,33,10,23,23.39,
      11,12,13,14,20,20,34,11.22,21,
      34,9,18,19,10.27,20,34,20,18.3,33]
total=0
above=[]
below=[]
for i in temp:
    total=total+i
avg=total/len(temp)
for i in temp :
    if i > avg:
        above.append(i)
    else:
        below.append(i)
print("Hottest day :",max(temp))
print("coldest day :",min(temp))
print("average temperature :",avg)
print("Days above average temperature :",above)
print("Days below average temperature :",below)               