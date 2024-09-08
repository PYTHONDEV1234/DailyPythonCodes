# getters and setters 

# get_name - This is used to fetch the name 
# set_name - to update the value 

class ATM:
    def __init__(self, pin , balance=0):
        self._pin = pin    
        self._balance = balance
    
    @property
    def pin(self):
        return self._pin
    
    @pin.setter
    def pin(self,new_pin):
        self._pin = new_pin
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,new_amount):
        if not isinstance(new_amount,int):
            raise ValueError("Amount should be an integer")
        self._balance = new_amount

atm1 = ATM(1234, 1000)  
atm2 = ATM(3456,10000) 
atm1.balance=1232435
print(atm1.balance)
print(atm2.balance)

