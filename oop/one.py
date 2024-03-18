


class Product:
  def __init__(self, name, email):
    self.name = name 
    self.email = email
    
    
class Phone(Product):
  pass 


class smartPhone(Product):
  pass 


class keypadPhone(Product):
  pass 



a = Product('hello', 'ram@')
print(a.name)
print(a.email)