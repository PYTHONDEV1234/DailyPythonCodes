class ATM:
    def __init__(self, pin , balance=0):
        self.pin = pin       #public
        self.balance = balance
    
    def check_pin(self,final_pin):
        return final_pin == self.pin
    
    def deposit(self , amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited")
        else:
            print("Negative aount can't be deposited")
    
    def withdraw(self , amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn")
        else:
            print("Enter positive amount")
    
    def check_balance(self):
        return self.balance
    
atm = ATM(1234, 1000)   
print(atm.check_balance())   
atm.pin = 1456
print(atm.pin)
atm.balance = "1234"
# print(atm.deposit(1200))

