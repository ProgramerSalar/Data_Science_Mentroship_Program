


class Parent:
  
  def __init__(self):
    self.num = 100
    
    
class Child(Parent):
  
  def __init__(self):
    super().__init__()
    self.val = 200
    
    
  def show(self):
    # return self.num, self.val
    print(self.num)
    print(self.val)
    
    
    
    
    
a = Parent()
print(a.num)
b = Child()
print(b.val)
print(b.show())