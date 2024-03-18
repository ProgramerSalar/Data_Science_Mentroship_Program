

class A:
  def m1(self):
    return 20 
  
  
class B(A):
  def m1(self):
    val = super().m1() + 20   # upper class A m1 constructor call
    return val 
  
  
class C(B):
  def m1(self):
    val = super().m1()   # this code are work
    val = self.m1()      # this code are not work
    return val 
  
# a = B()
# print(a.m1())
b = C()
print(b.m1())