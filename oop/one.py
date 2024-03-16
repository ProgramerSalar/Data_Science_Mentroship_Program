


class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.__balance = 0
    #self.menu()


 # geeter function 
  def get_balance(self):
    return self.__balance


# set function 
  def set_balance(self,new_value):
    if type(new_value) == int:
      self.__balance = new_value
    else:
      print('beta bahot maarenge')

  def __menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.__balance = user_balance

    print('pin created successfully')

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
    else:
      print('nai karne de sakta re baba')

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.__balance:
        self.__balance = self.__balance - amount
        print('withdrawl successful.balance is',self.__balance)
      else:
        print('abe garib')
    else:
      print('sale chor')
      
      
      
      
      
      
obj = Atm()
obj.set_balance("hehe")
obj.get_balance()

# give this error 
#TypeError: '<=' not supported between instances of 'int' and 'str'


### you make private variable no Any one not axis the variable because your function and variable private but
### IF YOU KNOW THE VARIABLE NAME, FUNCTION NAME THEN ACCESS THE YOUR VARIABLE AND FUNCTION OUT SIDE OF CLASS 
### HOW CAN ACCESS THE VARIABLE AND FUNCTION IF ARE PRIVATE ?
### EXAMPLE, YOU CLASS NAME IS ATM AND YOU PRIVATE FUNCTION IS VARIABLEIS BALANCE EX- _Atm_balance  



### IF YOU GET THE FUNCTION MEANS TUM PRIVATE METHOD KO NAHI PAR EK FUNCTION BANA KE USKO PUBLIC KAR DIYA 
### ISME TUM FUNCTION ME CONDITION BHI DAL SAKTE HAI,
### ISKO KARNE SE TUMHARA VARIABLE BHI PRIVATE RAHEGA OR EK FUNCTION ME DAL KE USKO ALLOW BHI KAR DIYA
### THIS IS CALLED GETTER AND SETTER METHOD 

#### GETER MEANS KON SA PARIVATE VARIABLE KO PUBLIC KARNA HAI
#### SETTER MEANS JO VARIABLE ALLOW KIYE HO PUBLIC KARNA USKO FUNCION ME DAL DO TAKI CONDITION USE KAR SAKO 