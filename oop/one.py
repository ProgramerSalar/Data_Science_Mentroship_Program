

class Fraction:
    
    def __init__(self, x, y):
        self.a = x 
        self.b = y 
        
        
    # str method is atomatically call 
    def __str__(self):
        return 'hello'
    
    
a = Fraction(2, 2)
print(a)