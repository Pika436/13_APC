# 18.	Create a shopping cart using a list.
'''Perform:
•	Add item 
•	Remove item 
•	Search item 
•	Display cart 
•	Count total items
'''

card=[]
while True:
    print("\n-----shopping cart-----")
    print("1.Add item")
    print("2.Remove item")
    print("3.Search item")
    print("4.Display cart")
    print("5.count total length")
    print("6.Exit")
    
    choice=int(input("enter your choice(1-6): "))
    
    if choice==1:
        item=input("enetr an item : ")
        card.append(item)
        print("item added successfully")
     
    elif choice==2:
        item=input("enter item to remove :")
        if item in card:
            card.remove(item)
            print("item deleted successfully")
        else:
            print("item not found")
    
    elif choice==3:
        item=input("enter item to search :")
        if item in card:
            print("item found")
        else:
            print("item not found")
    
    elif choice==4:
        print("shopping card :",card)
        
    elif choice==5:
        print("Total iems :",len(card))
    
    elif choice==6:
        print("Thank you")
        break
        
    else:
        print("invalid choice!")                                        