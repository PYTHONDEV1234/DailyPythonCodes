# class Animal:
#     def __init__(self, species,sound):
#         self.species = species
#         self.sound = sound
#     def makes_sound(self):
#         return f"The {self.species} makes {self.sound} sound."

# dog = Animal("Dog","Bark")
# print(dog.makes_sound())

# cat = Animal("Cat","Meow")
# print(dog.sound)
# print(cat.makes_sound())


# class Student:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def greet(self):
#         return f"Hello {self.name} , Good Morning."
#     def display_info(self):
#         return f"Your name is: {self.name} and you are {self.age} years old."

# arvin = Student("Arvin", 30)
# print(arvin.greet())
# print(arvin.display_info())

# ansel = Student("Ansel",20)
# print(ansel.age)
# print(ansel.display_info())



class Rectangle:
    def __init__(self , length, bredth):
        self.length= length
        self.bredth= bredth
    
    def area(self):
        return self.length * self.bredth
    
    def perimter(self):
        return 2*self.length + 2*self.bredth

rect1 = Rectangle(20,10)
print(rect1.area())
print(rect1.perimter())


# Task 
# Create a student class 
# with variables like student name , Total marks and Total subjects 
# It has one method to print the average marks obtained bhy a student. 
# With Student 

# Create a Circle Class 
# It will accept Radius as variable
# It should have functions to print the circumference and area of a circle 