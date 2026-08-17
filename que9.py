# 9.Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
cities=["pune","mumbai","satara","kolhapur","nashik"]
city=input("Enter a city : ")
if city in cities:
    print("exist")
else:
    print("not exist")    
