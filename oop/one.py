#

# class Atm():
#     # print('hello world')
    
#     def __init__(self):
#         # print("hello world")
#         self.pin = ''
#         # self.balance = 0
#         self.menu()
        
        
        
#         # method 
#     def menu(self):
#         # print("create pin")
#         user_pin = input("""
#                          1. create Pin
#                          2. chanage pin
#                          3. update pin 
#                          4. check balance
#                          """)
        
        
#         if user_pin == '1':
#             self.create_pin()
        
        
        
#         # method , if you function are inner side of class this is method 
#         # and outside of class that is function 
#     def create_pin(self):
        
#         user_pin = input("enter Pin")
#         self.pin = user_pin
#         print("create pin")
    
    
    
# Atm()



L = [1, 2, 3]
len(L)  # len is function 
L.append(2)  # append is method, b/c L is class and append is method 
print(L)