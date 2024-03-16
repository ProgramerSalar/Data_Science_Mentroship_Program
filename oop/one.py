
# class Point:
    
#     def __init__(self, x, y):
#         self.x_cod = x 
#         self.y_cod = y 
#         # print(self.x_cod, self.y_cod)
        
#     def __str__(self):
#         return "<{},{}>".format(self.x_cod, self.y_cod)
    
    
#     def distance_between_two_point(self, other):
#         return ((self.x_cod - other.y_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    
#     def distance_between_point_and_origin(self):
#         # return self.distance_between_two_point(Point(0,0))
#         return ((self.x_cod**2 + self.y_cod**2))**0.5
        
    
    
    
# class Line:
    
#     def __init__(self, x, y, z):
#         self.a = x 
#         self.b = y 
#         self.c = z 
        
#     def __str__(self):
#         return "{}x + {}y + {}".format(self.a, self.b, self.c)
    
    
#     def Point_on_lines(self, point):
#         if self.a*point.x_cod + self.b*point.y_cod + self.c == 0:
#             return "Lies on the lines"
#         else:
#             return "not Lies on the lines"
    
    
    
#     def shortest_distance(line, point):
#         nominator = abs(line.a*point.x_cod + line.b*point.y_cod + line.c)
#         dominator = (line.a**2 + line.b**2)**0.5
#         return nominator/dominator
    
    
   
        
# l1 = Line(1,1,-2)
# p1 = Point(1,10)
# print(l1.shortest_distance(p1))


class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)
      
      
      
# Attribute creation from outside of the class      
c = Person.gender = "male"
print(c)