# 2456 --> 2+4+5+6 = 17

def sumOfDigits(n):
    if n==0:
        return 0
    else:
        return n%10 + sumOfDigits(n//10)

print(sumOfDigits(42456))


# Find the Product of all the digits 
# Find the average of all the digits 
# Reversing a number
