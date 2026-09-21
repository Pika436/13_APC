# 4.	Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14* self.radius * self.radius  
    
    def circumferance(self):
        return 2 * 3.14 * self.radius
    
    def display(self):
        print("area of circle : ",self.area())  
        print("circumference of circle :",self.circumferance())
        
obj=Circle(4)
obj.display()        