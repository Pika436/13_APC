# 25.	Represent the friends of two users using sets. Find:
'''
•	Mutual friends 
•	Friends unique to User 1 
•	Friends unique to User 2 
•	Total unique friends
'''

user1={"prachi","shravani","aditi","sanchita"}
user2={"prachi","siddhi","kalyani","sneha"}

mut=user1.intersection(user2)
u1=user1.difference(user2)
u2=user2.difference(user1)
total=user1.union(user2)

print("Mutual friends :",mut)
print("Friends unique to User 1 :",u1)
print("Friends unique to User 1 :",u2)
print("Total unique friends :",total)