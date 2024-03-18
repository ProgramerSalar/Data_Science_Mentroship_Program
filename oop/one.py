
# Method Overriding


class A:
  
  def area(self, a, b=0):
    if b == 0:
      return 3.14*a*a 
    else:
      return a*b 
    
    
x = A()
print(x.area(10))
print(x.area(10,20))
    