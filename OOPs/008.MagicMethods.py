#__init__
#__eq__
#
# Magic Methods - Dunder Methods - 
# self  Other
# 3/5 + 6/7  = 21+30 /35 = 51/45
# Numerator , Denominator
class Fraction:
    def __init__(self,numerator, denominator):
        self.numerator= numerator
        self.denominator= denominator
    
    def __add__(self,other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)
    def __sub__(self,other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    # __mul__
    #div - find the method
def main():
    print("\nWelcome to Fraction Calculator\n")
    num1 = int(input("Numerator1: "))
    denom1 = int(input("Denominator1: "))

    print(f"First Fraction : {num1} / {denom1}")
    fraction1= Fraction(num1,denom1)
    num2 = int(input("Numerator2: "))
    denom2 = int(input("Denominator2: "))

    print(f"First Fraction : {num2} / {denom2}")

    fraction2= Fraction(num2,denom2)

    while True:
        print("\nSelect one option:\n")
        print("1. TO add Fractions")
        print("2. TO sub Fractions")
        print("3. TO mul Fractions")
        print("4. TO div Fractions")
        print("5.Exit")

        choice = int(input("Enter your choice (1-5):"))

        if choice ==1:
            print(f"\n {fraction1} + {fraction2}={fraction1 + fraction2}")
        elif choice ==2:
            print(f"\n {fraction1} + {fraction2}={fraction1 - fraction2}")
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()

