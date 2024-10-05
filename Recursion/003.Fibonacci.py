# 0 1 1 2 3 5 8 ......

def fibon(n):
    if n==0:
        return 0
    elif n==1:
        return 1 
    else:
        return fibon(n-1)+ fibon(n-2)

for i in range(6):
    print(fibon(i))

