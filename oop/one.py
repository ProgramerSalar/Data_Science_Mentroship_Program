
class Point:
    
    def __init__(self, x, y):
        self.x_cod = x 
        self.y_cod = y 
        # print(self.x_cod, self.y_cod)
        
    def __str__(self):
        return "<{},{}>".format(self.x_cod, self.y_cod)
    
    
    def distance_between_two_point(self, other):
        return ((self.x_cod - other.y_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    
    def distance_between_point_and_origin(self):
        # return self.distance_between_two_point(Point(0,0))
        return ((self.x_cod**2 + self.y_cod**2))**0.5
        
    
    
    
class Line:
    
    def __init__(self, x, y, z):
        self.a = x 
        self.b = y 
        self.c = z 
        
    def __str__(self):
        return "{}x + {}y + {}".format(self.a, self.b, self.c)
    
    
    def Point_on_lines(self, point):
        if (self.a*point.x_cod + self.b*point.y_cod + self.c) == 0:
            return "Lies on the lines"
        else:
            return "not Lies on the lines"
    
    
        
    
    
    
    
    
        
p = Point(2, 3)
p2 = Point(3, 2)
a = p.distance_between_two_point(p2)
b = p.distance_between_point_and_origin()
# print(b)
# print(a)


l = Line(0, 0, 0)
# print(l)

l1 = l.Point_on_lines(Point(3,4))
print(l1)



