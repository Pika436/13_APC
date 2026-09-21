# 3.Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*self.length + 2*self.breadth
    
    def display(self):
        print("Area= ",self.area())
        print("Perimeter= ",self.perimeter())
        
obj=Rectangle(30,10)
obj.display()        