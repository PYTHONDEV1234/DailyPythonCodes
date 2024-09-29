"""
Q1. What is a function in Python?

    a) A block of code that only runs when it is executed by an interpreter

    b) A block of code that runs automatically every time the program is run

    c) A reusable block of code that only runs when it is called

    d) A block of code that cannot accept inputs or return outputs

-------------------------------------------------------------------------------------
Q2. What is the purpose of the return statement in a Python function?

    a) It terminates the function and prints the result

    b) It terminates the function and returns a value to the caller

    c) It stops the execution of the entire program

    d) It returns the memory address of the function

-------------------------------------------------------------------------------------
Q3. What is the difference between a function argument and a function parameter?

    a) Arguments are the names defined in the function declaration; parameters are the values passed

    b) Parameters are the names defined in the function declaration; arguments are the actual values passed

    c) There is no difference between arguments and parameters

    d) Arguments are passed by reference, and parameters are passed by value

---------------------------------------------------------------------------------------
Q4. What happens if you try to return a value from a function without using the return statement?

    a) The function will return 0

    b) The function will return None

    c) The function will return an empty string ""

    d) The function will throw an error

-----------------------------------------------------------------------------------------------
Q5. In Python, what is the term used for a function defined inside another function?

    a) Nested function

    b) Inner function

    c) Sub-function

    d) Anonymous function

-------------------------------------------------------------------------------------------
Q6. Which of the following statements is true about function scope?
    a) Variables defined inside a function are accessible outside the function

    b) Variables defined inside a function are local to that function

    c) Variables defined inside a function are global variables

    d) Functions cannot access global variables

-------------------------------------------------------------------------------------------
Q7. What is a key feature of a recursive function?

    a) It calls itself until a base condition is met  

    b) It can only return integers  

    c) It cannot have more than one parameter  

    d) It never returns any value  

---------------------------------------------------------------------------------------------
Q8. What is the output of the following code?  
"""
def calculate(x, y=10):
    return x * y
print(calculate(5, 2))
""" 
    a) 50              b) 5             c) 20            d) 12 
---------------------------------------------------------------------------------------------
Q9. How can a function call itself in Python?  
    a) By using the `self` keyword

    b) By creating a copy of itself 

    c) By calling its name inside its own definition 

    d) By using recursion 
--------------------------------------------------------------------------------------------- 
Q10. What is the main difference between a `return` statement and a `print` statement in a function?**  
    a) `return` outputs a value, while `print` only prints a value to the console

    b) `print` can only be used in loops 

    c) `return` can print multiple values 

    d) `print` always returns a value  
----------------------------------------------------------------------------------------------
Q11. What does the following code return? 
""" 
def myFunc():
    pass
print(myFunc())
"""
    a) `None`             b) `pass`             c) `0`               d) Error 
-----------------------------------------------------------------------------------------------
Q12. What will be the output of the following code?
"""
def func1():
    return "Hello"

def func2():
    return func1() + " World" + 123
print(func2())
"""
    a) Hello            b) Hello World123      c) World Hello 123  d) Error   
---------------------------------------------------------------------------------------------
Q13. Which of the following is a built-in function in Python?

    a) `map()`          b) `myFunc()`          c) `calc()`        d) `run()` 

---------------------------------------------------------------------------------------------
Q14. What will the following code output?  
"""
def func(x):
    return x + 1
print(func(func(2)))
""" 
    a) 2              b) 3                    c) 4                d) 5
---------------------------------------------------------------------------------------------
Q15. Which of the following is NOT a valid Python function name? 

    a) `my_function()`   b) `_func123()`      c) `2coolFunc()`     d) `funcName()`  

----------------------------------------------------------------------------------------------
Q16. What happens if a function has no `return` statement? 
    a) It returns `0`

    b) It returns `None`

    c) It returns the last value calculated 

    d) It raises an error  
----------------------------------------------------------------------------------------------
Q17. What will be the output of the following code?
"""
def add(x, y):
    return x + y

def multiply(a, b):
    return add(a, b) * b

print(multiply(2, 3))
"""
    a) 5        b) 6        c) 15       d) 12
----------------------------------------------------------------------------------------------
Q18. What will be the code output?
"""
def outer():
    return inner()

def inner():
    return "Inside inner"

print(outer())
"""
    a) Inside inner     b) outer inner      c) Error        d) None
----------------------------------------------------------------------------------------------
Q19.Output of the code would be ?
"""
def square(x):
    return x * x

def cube(y):
    return square(y) * y

print(cube(3))
"""
    a) 9        b) 27       c) 81       d) Error
-----------------------------------------------------------------------------------------------
Q20. What will the following code output?
"""
def first():
    return "First"

def second():
    return first() + " Second"

def third():
    return second() + " Third"

print(third())
"""
    a) First Second         b) First Second Third           c) Second Third         d) Error
-----------------------------------------------------------------------------------------------
Q21. What will the output of this code be?
"""
def funcA():
    return 5

def funcB():
    return funcA() * 2

def funcC():
    return funcB() + 3

print(funcC())
"""
    a) 5        b) 10       c) 13       d) 16
---------------------------------------------------------------------------------------------
Q22. What will the output be?
"""
def greeting():
    return "Hi"

def farewell():
    return greeting() + " Bye"

print(farewell())
"""
    a) Hi           b) Bye          c) Hi Bye           d) Error
----------------------------------------------------------------------------------------------
Q23. What will the following code output?
"""
def calculate(a):
    return a * 2

def total(b):
    return calculate(b) + 5

print(total(6))
"""
    a) 12           b) 17           c) 11           d) 8
----------------------------------------------------------------------------------------------
Q24. What will the output be?
"""
def myFunc(a, b=2, c=3):
    return a + b + c
print(myFunc(1, 5))
"""
    a) 6           b) 9            c) 11            d) Error 

---------------------------------------------------------------------------------------------
Q25. What is the purpose of the `global` keyword in a function? 
    a) It declares that a variable is global only within the function

    b) It allows a function to return global variables 

    c) It defines a global variable inside a function 

    d) It allows modification of global variables within a function  
---------------------------------------------------------------------------------------------
Q26. What will be the result of the following code?  
"""
def add(a, b):
    return a + b
result = add(b=3, a=2)
print(result)
""" 
    a) Error        b) 5        c) 6        d) 2 

---------------------------------------------------------------------------------------------
Q27. What will the following code output? 
""" 
def myFunc(a, b):
    return b, a
print(myFunc(1, 2))
"""
    a) 1 2          b) 2 1      c) (2, 1)   d) Error

----------------------------------------------------------------------------------------------
Q28. Which of the following allows a function to remember the value of a variable between calls?
 
    a) `global`    b) `nonlocal`  c) `lambda`  d) `static` 

-----------------------------------------------------------------------------------------------
Q29. What is a function that calls itself repeatedly known as?**  
    a) In-place function 

    b) Lambda function

    c) Recursive function 

    d) Anonymous function  
----------------------------------------------------------------------------------------------
Q30. How can you make a function return multiple values? 
    a) By using multiple `return` statements 

    b) By returning a tuple  

    c) By using a global variable  

    d) By passing the values as arguments  
-----------------------------------------------------------------------------------------------
Q31. What happens if you do not specify a return value in a Python function?**  
    a) The function will return 0 

    b) The function will return `None`

    c) The function will raise an error 

    d) The function will return `False`  
-----------------------------------------------------------------------------------------------
Q32. How can a function be assigned to a variable in Python?**  
    a) `var = myFunc()`

    b) `var = myFunc` 

    c) `var(myFunc)`

    d) `myFunc = var()`  
----------------------------------------------------------------------------------------------
Q33. Which of the following is a valid way to return nothing from a function in Python?**  
    a) `return None`

    b) `return 0` 

    c) `pass`

    d) `return ""`  
----------------------------------------------------------------------------------------------
Q34. What will the following code output?
"""
def increment(x):
    return x + 1

def double(x):
    return increment(x) * 2

print(double(4))
"""
    a) 8            b) 10           c) 12           d) 14
"""







