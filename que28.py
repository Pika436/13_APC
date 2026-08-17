# 28.	Store scores of a batsman in 10 matches and calculate:
'''
•	Highest score 
•	Lowest score 
•	Total runs 
•	Average runs 
•	Number of centuries (≥100) 
•	Number of half-centuries (50–99)
'''

scores=[57,50,80,102,30,59,105,88,99,40]
total=0
century=0
half_cen=0
for score in scores:
    total=total+score
    if score >= 100:
        century+=1
        
    elif score >= 50:
       half_cen+=1
avg=total/len(scores)
print("highest score :",max(scores))
print("lowest score :",min(scores))
print("total runs :",total)
print("average runs :",avg)
print("number of century :",century)  
print("number of half century :",half_cen)
          