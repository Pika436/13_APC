# 19.	Create two sets:
'''
•	Students present in the morning session 
•	Students present in the afternoon session 
Find:
•	Students present in both sessions 
•	Students present only in the morning 
•	Students present only in the afternoon 
•	Students present in at least one session
'''
first={"ram","janaki","sweta","piyush","riya"}
second={"shyam","rohan","veda","ram","riya"}

print("Students present in both sessions :",first.intersection(second))
print("Students present only in the morning :",first.difference(second))
print("Students present only in the afternoon :",second.difference(first))
print("Students present in at least one session :",first.union(second))