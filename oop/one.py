

class Fraction:
    
    
    # paramatrize constructor - that constructor when you give the input in this constructor give two parameter x and y  
    def __init__(self, x, y):
        self.num = x     # num means nemonetor 
        self.den = y     # den means demonetor
        # print(x, y)
        
        
    # magic method     
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    
    def __add__(self, other):   # we have two fraction , add method take two parameter first is self, and second is other || then we are added the faction object  
        # return "hello world"
        # print("hello world")
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)   # here we are not use self how because we are not create object in class, we created the object in method so not need to self 
    
        
    def __sub__(self, other):   # we have two fraction , add method take two parameter first is self, and second is other || then we are added the faction object  
        # return "hello world"
        # print("hello world")
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)   # here we are not use self how because we are not create object in class, we created the object in method so not need to self 
    
        
    # multiply magic mathod 
    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)   # here we are not use self how because we are not create object in class, we created the object in method so not need to self 
    
        
    # devide magic mathod 
    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den * other.num
        return "{}/{}".format(new_num, new_den)   # here we are not use self how because we are not create object in class, we created the object in method so not need to self 
    
        
        
    
    
        
    

a = Fraction(2, 2)
b = Fraction(1, 2)
# print(a)    
# print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)