# getters and setters 

# get_name - This is used to fetch the name 
# set_name - to update the value 

class ATM:
    def __init__(self, pin , balance=0):
        self.pin = pin    
        self.balance = balance
    
    def get_pin(self):
        return self.pin
    
    def set_pin(self,new_pin):
        self.pin = new_pin
    
    def get_balance(self):
        return self.balance
    
    def set_balance(self,new_amount):
        self.balance = new_amount

# Self is a object
atm1 = ATM(1234, 1000)  
atm2 = ATM(3456,10000) 
atm1.set_balance(300)
atm2.set_balance("Hello")
print(atm1.get_balance())
print(atm2.get_balance())

