# 1.Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self,rn,name,marks):
        self.rn=rn
        self.name=name
        self.marks=marks
    
    def display(self):
        print("roll no: ",self.rn)
        print("name :",self.name)
        print("marks :",self.marks)
        print("percentage :",self.marks,"%")
     
obj1=Student(13,"prachi",80)
obj1.display()

obj2=Student(32,"aman",79)
obj2.display()
        
            