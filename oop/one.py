


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
            
        if user_input == '2':
            self.change_pin()
            
            
        if user_input == '3':
            self.check_balance()
            
        if user_input == '4':
            self.withdrawl()
            
        
            
            
        
    def create_pin(self):
        user_pin = input("ENter Pin")
        balance = int(input("Enter Balance"))
        self.pin = user_pin
        self.balance = balance
        print("Pin created Successfully")
        self.func()
        
        
    def change_pin(self):
        old_pin = input("Enter Old Pin")
        if old_pin == self.pin:
            new_pin = input("Enter New Pin")
            self.pin = new_pin
            print("pin Updated Successfully")
            self.func()
        else:
            print("invalid pin")
            self.func()
            
            
    def check_balance(self):
        user_pin = input("Enter Pin")
        # if user_pin == self.pin:
        print(self.balance)
        self.func()
        
        
    def withdrawl(self):
        user_pin = input("Enter Pin")
        if user_pin == self.pin:
            amount = int(input("how many Amount withdrawl"))
            
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('withdrowl secessfully', self.balance)
                self.func()
                
                
                
    
                    
            
                
            
        
        
        


Atm()