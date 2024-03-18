
class Product:
  
  def review(self):
    print("Product customer review")
    
    
class Phone(Product):
  
  def __init__(self, name):
    self.name = name 
    
    
  def buy(self):
    print("buy a product")
    
    
class SmartPhone(Phone):
  pass 




a = SmartPhone('manish')
print(a.name)