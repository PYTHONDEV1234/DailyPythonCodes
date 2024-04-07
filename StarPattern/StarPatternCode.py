def starPattern(n):
    print("* "*n)
print("Using Function calls")
starPattern(1)
starPattern(2)
starPattern(3)
starPattern(4)
starPattern(5)

#Using the for loops inside the function

print("Using the for loops inside the function")
def starPattern(n):
    for i in range(1,n+1):
        print("* "*i)
starPattern(5)