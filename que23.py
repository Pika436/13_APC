# 23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.
available={"math","english","python","java","c++"}
request={"science","marathi","hindi","python",""}

avail=available.intersection(request)
print(" requested books are available :",avail)