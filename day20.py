# 20.	Create a list of books.
'''Implement:
•	Add a new book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books
'''

books=['math','english','science','hindi','marathi']
while True:
    print("\n-----list of books-----")
    print("1.Add a new book ")
    print("2.Search a book")
    print("3.Remove a book ")
    print("4.Display all books ")
    print("5.Count total books")
    print("6.exit")
    
    choice=int(input("Enter choice (1-6): "))
    
    if choice==1:
        name=input("enetr a book name: ")
        books.append(name)
        print(books,"added successfully")
    elif choice==2:
        name=input("Enter book for search :")
        if name in books:
            print(name," found")
        else:
            print(name,"not found")
    elif choice==3:
        name=input("enter book to remove:")
        if name in books:
            books.remove(name)
            print(name,"removed successfully")
        else:
            print(name,"not found")
    elif choice==4:
        print("list of books :",books)
    elif choice==5:
        print("Total books :",len(books))
    elif choice==6:
        print("program ended")
        break
    else:
        print("invalid input")                            