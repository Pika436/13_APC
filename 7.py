# 7.	Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self,brand,model,storage,price):
        self.brand=brand
        self.model=model
        self.storage=storage
        self.price=price
        
    def display(self):
        print("brand :",self.brand)
        print("model :",self.model)
        print("storage :",self.storage)
        print("price :",self.price)
        
    def discount(self):
        discount=self.price*0.10
        final_price=self.price-discount
        return final_price
    
obj=MobilePhone("vivo","Y28s 5G",128,14000)
obj.display()
print("price after 10% discount :",obj.discount())            