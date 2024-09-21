"""
1. What is the correct syntax for defining a constant in Python?
    A) const PI = 3.14

    B) PI = 3.14

    C) CONSTANT PI = 3.14

    D) PI: const = 3.14
------------------------------------------------------------------------------------------------
2. Which data type would be most appropriate for storing a collection of unique items?
    A) List

    B) Tuple

    C) Set

    D) Dictionary
------------------------------------------------------------------------------------------------
3. Which of the following is/are used to iterate over elements in a list? (Select all that apply)

    A) for loop

    B) while loop

    C) switch statement

    D) if statement
-----------------------------------------------------------------------------------------------
4. In Python, a variable name cannot start with a number. (True / False)

-----------------------------------------------------------------------------------------------
5. Which of the following variable names is valid in Python?**  
    a) `1variable`

    b) `variable_1`

    c) `variable-1`

    d) `variable 1`
----------------------------------------------------------------------------------------------
6. A dictionary in Python can have duplicate keys. (True or False)

-----------------------------------------------------------------------------------------------

7. The if-else statement can be replaced by a switch statement in Python for conditional checks.

-----------------------------------------------------------------------------------------------
8. Which of the following are mutable data types in Python? (Select all that apply)
    A) List
    B) Tuple
    C) Set
    D) Dictionary
-----------------------------------------------------------------------------------------------
10.What will be the output of the following code?
"""
names = ['Alice', 'Bob', 'Charlie', 'Dave']
short_names = [name for name in names if len(name) <= 4]
print(short_names)
"""
    a) ['Alice', 'Bob']

    b) ['Bob', 'Dave']

    c) ['Charlie', 'Dave']

    d) ['Bob', 'Charlie']
----------------------------------------------------------------------------------------------
11.What will be the output of this code?
"""
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(squares)
"""
    a) [1, 4, 9, 16, 25]

    b) [2, 3, 4, 5]

    c) [1, 8, 27, 64, 125]

    d) [1, 9, 25]
----------------------------------------------------------------------------------------------
12. What is the output of the following code?
"""
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)
"""
    A) [1, 2, 3, 4, 5]

    B) [1, 2, 3, 4]

    C) [5, 1, 2, 3, 4]

    D) [1, 2, 3, 4, [5]]
----------------------------------------------------------------------------------------------
13. What is the correct way to define a set in Python?
    A) my_set = {}
    B) my_set = []
    C) my_set = set()
    D) my_set = dict()
----------------------------------------------------------------------------------------------
14. A _______ is a collection of key-value pairs in Python.

----------------------------------------------------------------------------------------------
15.What will be the output of this code?
"""
nums = [3, 7, 12, 15, 19]
even_or_odd = ['Even' if num % 2 == 0 else 'Odd' for num in nums]
print(even_or_odd)
"""
    a) ['Odd', 'Odd', 'Odd', 'Odd', 'Odd']

    b) ['Odd', 'Odd', 'Even', 'Odd', 'Odd']

    c) ['Even', 'Odd', 'Even', 'Odd', 'Even']

    d) ['Even', 'Odd', 'Odd', 'Even', 'Even']
-----------------------------------------------------------------------------------------------
16. In Python, sets are ordered collections of unique items. (True/ False)

-----------------------------------------------------------------------------------------------
17. Given a dictionary student_scores with student names as keys and their scores as values, write a Python code snippet to print only the names of students who scored more than 75.
"""
student_scores = {
    'Alice': 85,
    'Bob': 70,
    'Charlie': 90,
    'David': 65,
}
for student, score in student_scores.items():
    if score > 75:
        print(student)
"""
What will be the output of the above code?
-------------------------------------------------------------------------------------------------
18. How can you access the third element of a list named fruits?
    A) fruits.get(3)

    B) fruits[3]

    C) fruits[2]

    D) fruits.get(2)
------------------------------------------------------------------------------------------------
19. What will be the output of the following code?
"""
my_set = {1, 2, 3}
my_set.add(2)
print(my_set)
"""
    A) {1, 2, 3}
    B) {1, 2, 3, 2}
    C) {1, 2}
    D) {2, 3}
-------------------------------------------------------------------------------------------------
20. In Python, the else block is executed when the if condition is _______.

-------------------------------------------------------------------------------------------------
21. In Python, a set cannot contain _______ elements.

-------------------------------------------------------------------------------------------------
22. The switch statement is natively supported in Python. (True or False)

-------------------------------------------------------------------------------------------------
23. A list in Python can contain elements of different data types. (True or False)

-------------------------------------------------------------------------------------------------
24. What will be the output of the following code?
"""
my_tuple = (1, 2, 3)
my_tuple[1] = 4
print(my_tuple)
"""
    A) (1, 4, 3)

    B) (1, 2, 3, 4)

    C) (1, 2, 3)

    D) TypeError
-------------------------------------------------------------------------------------------------
25. What is the main difference between a list and a set in Python?
    A) A list is unordered, and a set is ordered.

    B) A list allows duplicate elements, and a set does not.

    C) A list is mutable, and a set is immutable.

    D) A list supports indexing, and a set does not.

-------------------------------------------------------------------------------------------------
26. In Python, a variable name can contain letters, numbers, and _______ characters, but cannot start with a number.
 
-------------------------------------------------------------------------------------------------
27. In Python, the len() function can be used to determine the number of elements in a tuple. (True or False)

-------------------------------------------------------------------------------------------------
28. Which of the following methods can be used to add elements to a list? (Select all that apply)
    A) append()

    B) insert()

    C) extend()

    D) add()

-------------------------------------------------------------------------------------------------
29. Which of the following statements about Python dictionaries are true? (Select all that apply)
    A) Dictionary keys must be unique.

    B) Dictionary values must be immutable.

    C) Dictionary keys can be of any data type.

    D) Dictionary values can be of any data type.
-------------------------------------------------------------------------------------------------
30. Write a Python code snippet to create a set from a list of numbers and then print the length of the set.
"""
numbers = [1, 2, 2, 3, 4, 4, 5]
queue = set(numbers)
print(len(queue))
"""
What will be the output of the above code?

-------------------------------------------------------------------------------------------------
31. Which of the following statements is true about lists and tuples in Python?
    A) Lists are immutable, and tuples are mutable.

    B) Lists are ordered collections, and tuples are unordered collections.

    C) Lists are mutable, and tuples are immutable.

    D) Lists and tuples are both immutable.
-------------------------------------------------------------------------------------------------
Q32. What is the output of this code?  
"""
x = 5
print(type(x))
"""
a) `int`  
b) `<class 'int'>`  
c) `5`  
d) `None` 
----------------------------------------------------------------------------------------------
33. What will be the output of this code?
"""
words = ['apple', 'banana', 'pear','orange']
capital_words = [word.upper() for word in words if len(word) > 4]
print(capital_words)
"""
a) ['APPLE', 'BANANA']
b) ['apple', 'banana', 'pear','ORANGE']
c) ['APPLE', 'BANANA', 'PEAR']
d) ['apple', 'banana', 'pear','orange']

----------------------------------------------------------------------------------------------
34.What does the following code do?
"""
for i in range(3):
    print(i)
"""
    a) Prints 0, 1, 2

    b) Prints 1, 2, 3

    c) Prints 3 times but with no values

    d) Error due to missing arguments
----------------------------------------------------------------------------------------------
35. What does the continue statement do in a loop? 
    a) Exits the loop

    b) Skips the remaining code inside the loop for the current iteration

    c) Restarts the loop from the beginning

    d) Terminates the program
----------------------------------------------------------------------------------------------
36.What will the following code print?
"""
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
"""
    a) 1 2 3 4 5

    b) 1 2 4 5

    c) 1 2 3 5

    d) Infinite loop
----------------------------------------------------------------------------------------------
37.What is the purpose of the break statement in Python? 
    a) To exit from the innermost loop only

    b) To exit the loop and continue the next iteration

    c) To terminate the entire program

    d) To skip the current iteration of the loop
----------------------------------------------------------------------------------------------
38.What will be the output of this code?
"""
for i in range(1, 10):
    if i % 3 == 0:
        break
    print(i)
"""
    a) 1 2

    b) 1 2 3

    c) 1 2 3 4 5

    d) No output
-----------------------------------------------------------------------------------------------
39.What will the following code print?
"""
for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print()
"""
a)  
    * * * * *
b)
    *  
    *   
    *  
    * * * *
c)
    * * * * * 
    * * *  
    * * * *  
    * * * * *
d)
    *  
    * *  
    * * *  
    * * * *  
-----------------------------------------------------------------------------------------
40. What does this code output?
"""
for i in range(4, 0, -1):
    for j in range(4 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
"""
a)
    * * * * * * *  
      * * * * *  
        * * *  
          *  
b)
    *  
    * *  
    * * *  
    * * * *  
c)
    *  
     * *  
      * * *  
       * * * *  
d)

       *  
      * *  
     * * *  
    * * * *  
"""