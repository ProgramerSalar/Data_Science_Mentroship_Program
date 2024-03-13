


class Atm:

    # constructor 
    # custructor are atomatically call when excute the class 
    def __init__(self):
        # print("hello world")
        self.pin = ''
        self.balance = 0
        self.func()


    # function 
    def func(self):
        user_input = input("""
            Hi how can help you
            1. Press 1 To create Pin
            2. Press 2 TO change Pin
            3. Press 3 To check Balance
            4. Press 4 To withdraw
            5. Anything To Exit.
        """)
        
        if user_input == '1':
            self.create_pin()
            
        
            
            
        
    def create_pin(self):
        user_pin = input("ENter Pin")
        self.pin = user_pin
        
        


Atm()