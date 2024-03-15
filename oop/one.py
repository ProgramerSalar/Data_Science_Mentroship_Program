# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line


class Point:
    
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y 
        
        
    def __str__(self):
        return "<{},{}>".format(self.x_cod, self.y_cod)
    
    
    def ecluen_distance(self, other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5 # 0.5 means root of two cordinate 
    
    
    def distance_from_origin(self):
        return self.ecluen_distance(Point(0, 0))
    
    
    
    
a = Point(0, 0)
a2 = Point(10,10)
print(a)
print(a2)
b = a.ecluen_distance(a2)
print(b)
c = a.distance_from_origin()
print(c)