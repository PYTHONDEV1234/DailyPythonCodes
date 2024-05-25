''' 
LAMDBA EXPRESSION PYTHON
'''

print("------------------- Normal Function call -------------------")
from functools import reduce
def Add(a,b):
    print(a+b)
Add(2,45)

print("------------------- Example 1 -------------------")
#example 1
add = lambda x,y : x+y
print(add(2,45))

print("------------------- Example 2 -------------------")
#Example 2
mul = lambda x : lambda y : x*y
prod = mul(2)
print(prod(3))

print("------------------- Example 3 -------------------")
#example 3
#from functools import reduce
numbers= [1,2,3,4,5,6]
product = reduce(lambda x, y: x*y,numbers)
print(product)

print("------------------- Example 4 -------------------")
#example 4
students =[
    {'name':'John','grade':'A','age':24},
    {'name':'Vicky','grade':'B','age':54},
    {'name':'Jonny','grade':'A','age':20},
    {'name':'Vineet','grade':'C','age':62},
    {'name':'Will','grade':'D','age':14}
]

# well_sorted = sorted(students , key =lambda x:(x['grade']))
# well_sorted = sorted(students , key =lambda x:(x['name']))
# well_sorted = sorted(students , key =lambda x:(x['age']))
well_sorted = sorted(students , key =lambda x:(x['age'],x['grade']))
print(well_sorted)

print("------------------- Example 5 -------------------")
data = [
    {'name':'John','scores':[50,45,78,99,70]},
    {'name':'Vicky','scores':[25,45,38,19,40]},
    {'name':'Jonny','scores':[40,85,78,62,77]},
    {'name':'Vineet','scores':[36,95,26,99,70]},
    {'name':'Will','scores':[51,35,80,49,30]}
]
transform = lambda d: {'name': d['name'].upper(), 'average_score': sum(d['scores']) // len(d['scores'])}
transformed_data = list(map(transform, data))
print(transformed_data)


print("------------------- Example 6 -------------------")
operations ={
    'add':lambda x, y : x+y,
    'sub':lambda x, y : x-y
}

print(operations['add'](12,15))
print(operations['sub'](19,15))

