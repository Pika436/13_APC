# 5.	Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.

class Book:
    def __init__(self,id,title,author,price):
        self.id=id
        self.title=title
        self.author=author
        self.price=price
        
    def display(self):
        print("book id :",self.id)
        print("book title :",self.title)
        print("author :",self.author)
        print("book price :",self.price)
        
b1=Book(111,"wings of fire","APJ abdul kalam",1000)
b1.display()

b2=Book(112,"Gitanjali","Rabindranath Tagore",1200)
b2.display()

b3=Book(113,"Atomic Habit","James clear",800)
b3.display()            