class Car:
    def __init__(self,brand,model,year):
        self._brand = brand 
        self._model = model 
        self._year = year
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand_name):
        self._brand = brand_name

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model_name):
        self._model = model_name

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,new_year):
        self._year = new_year

car1 = Car("BWM","XYZ",2020)
car2 = Car("BALENO","ABC",2016)
print(car1.brand)
print(car1.year)

car2._brand = "Python"
print(car2.brand)
print(car2.year)
