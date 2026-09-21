# 8.	Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self,id,name,age,disease,fee):
        self.id=id
        self.name=name
        self.age=age
        self.disease=disease
        self.fee=fee
        
    def display(self):
        print("patient id :",self.id)
        print("patient name :",self.name)
        print("patient age :",self.age)
        print("fees :",self.fee)
        
    def total_fee(self):
        return self.fee
    
p1=Patient(111,"priya",21,"fever",700)
p1.display()
print("Total Bill :",p1.total_fee())    
            