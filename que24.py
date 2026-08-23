# 24.	Store visitor IDs from two different days in separate sets. Determine:
'''
•	Unique visitors across both days 
•	Returning visitors 
•	Visitors who came only on the first day 
•	Visitors who came only on the second day
•	Create sets representing products belonging to different categories. Find products that belong to both categories.
'''

day1={101,102,103,104,105}
day2={103,104,105,106,107}

unique=day1.union(day2)
returning=day1.intersection(day2)
first=day1.difference(day2)
second=day2.difference(day1)
