# Anything written after return  keyword will not be executed
def Greet():
    print("Hello")
    return "Hello Good Morning"
    # print("This is New message")

print(Greet())

# Can we have multiple keywords in our code?
# Answer - Yes 

def MaxOfTwo(a,b):
    if a>b:
        return a 
    else:
        return b
    
x = MaxOfTwo(100,200)
print("Larger value is :",x)



# ATM pin 


# Break keyword in loops 
# Return is used to exit a function


for i in range(20):
    if i==5:
        continue         # Skipping the current itereation
    elif i==10:
        break              #to exit the loop
    else:
        print(i) 
    
 #recursion - A function calling itself  
 
 