class Laptop:
    def __init__(self, brand,model, price):
        self._brand = brand
        self._model = model
        self._price = price
    
    @property       #getter function - read only code - means not changing the value - just trying to fetch details
    def brand(self):
        return self._brand
    
    @brand.setter 
    def brand(self,new_brand):
        self.brand = new_brand

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, new_model):
        self._model = new_model

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price

# Creating object
HPLaptop = Laptop("HP","Exteria","24000")
# getter function
# print(HPLaptop.price)

#setter 
HPLaptop._price = 234455667
print(HPLaptop.price)
dellLaptop =Laptop("Dell","Plus","64000")
