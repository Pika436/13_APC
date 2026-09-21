# 6.	Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self,num,name,unit):
        self.num=num
        self.name=name
        self.unit=unit
        
    def calculate(self):
        if self.unit<=100:
            bill=self.unit*5
        elif self.unit<=200:
            bill=(100*5)+((self.unit-100)*7)
        else:
            bill=(100*5)+(100*7)+((self.unit-100)*10)
        return bill
    
    def display(self):
        print("consumer number :",self.num)
        print("consumer name :",self.name)
        print("units :",self.unit)
        print("electricity bill :",self.calculate())

obj=ElectricityBill(121,"prachi",340)
obj.display()        
                    
            