# 25.	Store runs scored in 10 matches and calculate:
'''
•	Total runs 
•	Highest score 
•	Lowest score 
•	Average score 
'''
score=(60,80,97,200,100,86,56,73,66,90)

total=sum(score)
high=max(score)
low=min(score)
avg=total/len(score)

print("Total runs :",total)
print("Highest score :",high)
print("Lowest score :",low)
print("Average score :",avg)