class ATM:
    def __init__(self, pin , balance=0):
        self.__pin = pin    # private
        self.__balance = balance
    
    def check_pin(self,final_pin):
        return final_pin == self.__pin
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited")
        else:
            print("Negative aount can't be deposited")
    
    def withdraw(self , amount):
        if amount > 0 and amount <= self.balance:
            self.__balance -= amount
            print("Amount Withdrawn")
        else:
            print("Enter positive amount")
    
    def __check_balance(self):
        return self.__balance

# Self is a object
atm = ATM(1234, 1000)  
atm2 = ATM(3456,10000) 
# print(atm.check_balance())  
atm.__balance = 123445
# print(atm.__check_balance()) 
print(atm.__pin)
# print(atm.deposit(1200))
print(atm._ATM__check_balance())
print(atm._ATM__balance)



# Private - __member or __method  Or Access Modifier  - Private (Cars) , Public (Railways) , Protected (Family vehicle)
# _CLASSNAME__member
# _ATM__check_balance


# There is nothing private in Python.

