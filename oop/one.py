


class Product:
  def __init__(self, name, email):
    self.name = name 
    self.email = email
    
    
class Phone:
  
  def hello(self):
    print("hello world")

class smartPhone(Product):
  pass 


class keypadPhone(Product, Phone):
  pass 



a = keypadPhone("hello", "@hello")
print(a.email, a.name)

