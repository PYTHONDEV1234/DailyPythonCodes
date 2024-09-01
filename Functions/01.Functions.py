# function definition // Declaration
# Function Calling 

# greet(1,20)

# Passing - are we passing the arguments to the function or not

# return - is my function returning something or not - does my function code has return keyword or not

# no passing no return 
def Add():
    a =20 
    b = 30
    print(a+b)

# Not passing arguments 
# function calling 
# Add()

# passing no return 
def Add2(a,b):
    print(a+b)

# Add2(10,20)
# Add2(100,20)
# no passing but return 
def Greet():
    return "Hello Good Morning !!!"

print(Greet())
x = Greet()
print(x)

# passing and return 
def TotalScore(S1,S2,S3,S4,S5):
    total = S1+S2+S3+S4+S5
    return total

x = TotalScore(67,37,58,49,35)
print(x/5)