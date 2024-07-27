# class Square:
#     def __init__(self,side):
#         print("Init is called")
#         self.side = side

#     def calculateArea(self):
#         return f"Area of the square is : {self.side * self.side} unit square."   

# # ObjectName = ClassName()
# square1 = Square(5)
# print(square1.calculateArea())

# square2 = Square(10)
# print(square2.calculateArea())

class ATM:
    def __init__(self):
        print("""
            Choose from the menu given below:
              1. Check the balance
              2. Deposit amount
              3. Withdraw amount
              4. Change your pin
              5. Exit """)
        
    def checkBalance(self):
        print("Your balance is 10000$.")
    def withdraw(self):
        print("Your've withdrawn 100$.")

bank1 = ATM()
choice = int(input())

if choice == 1:
    bank1.checkBalance()
elif choice ==2:
    bank1.withdraw()

    






















# def myFunc():
#     print("Hello")

# myFunc()


