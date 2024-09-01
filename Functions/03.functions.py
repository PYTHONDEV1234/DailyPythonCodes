#Stack - Function calling


def First():
    print("Hello in am in First")
    Third()
    print("Exiting the First Code")

def Second():
    print("Hello in am in Second")

def Third():
    Second()
    print("Hello in am in Third")
    Fourth()

def Fourth():
    print("Hello in am in Fourth")

print("Program Started")
First()
print("Program ended")