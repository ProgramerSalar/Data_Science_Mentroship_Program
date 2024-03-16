

# Encapsulation = this means different different variable have different different data 

# instance var -> python tutor
class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

p1 = Person('nitish','india')
p2 = Person('steve','australia')
print(p1.name)
print(p2.name)