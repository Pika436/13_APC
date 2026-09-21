# 2.	Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id=emp_id
        self.name=name
        self.basic_salary=basic_salary
     
    def calculate_hra(self):
        return self.basic_salary*0.20
    
    def calculate_da(self):
        return self.basic_salary*0.10
    
    def calculate_gross(self):
        hra=self.calculate_hra()
        da=self.calculate_da()
        return self.basic_salary + hra + da 
    
    def display(self):
        print("employee id :",self.emp_id)
        print("name :",self.name)
        print("basic salary :",self.basic_salary)
        print("HRA :",self.calculate_hra())
        print("DA :",self.calculate_da())
        print("Gross salary :",self.calculate_gross())
        
b=Employee(23,"ram",50000)
b.display()        