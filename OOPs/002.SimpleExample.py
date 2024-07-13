# Class has two things - 1. Data (Variables) - 2. Methods (Functions)
#ThisIsPascalCase
class Laptop:
    # Data - Variables
    def __init__(self, brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display_details(self):
        return f"Laptop : {self.brand} {self.model} {self.price}"

# Creating object
HPLaptop = Laptop("HP","Exteria","24000")
print(HPLaptop.display_details())

dellLaptop =Laptop("Dell","Plus","64000")
print(dellLaptop.display_details())

print(dellLaptop.brand)
print(HPLaptop.price)

# Anything under a class is not accessible without using objects 
#print(display_details())
#print(brand)