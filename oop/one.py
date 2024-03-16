
class Point:
    
    def __init__(self, x, y):
        self.x_cod = x 
        self.y_cod = y 
        # print(self.x_cod, self.y_cod)
        
    def __str__(self):
        return "<{},{}>".format(self.x_cod, self.y_cod)
    
    
    def distance_between_two_point(self, other):
        return (self.x_cod - other.y_cod)
    
    
    
    
    
    
    
        
        
p = Point(2, 3)
p2 = Point(3, 2)
a = p.distance_between_two_point(p2)
print(a)