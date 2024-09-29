# Recursice function -- Means a function calling itself 


# def Hello():
#     print("Hello")
#     Hello()

# Hello()


# Recursvie Function ---  1) Calling itself  2) Base Condition

def Decreement(x):
    if x<0:
        return 0
    else:
        
        Decreement(x-1)
        print(x)

Decreement(10)


