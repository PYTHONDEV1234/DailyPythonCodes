# -*- coding: utf-8 -*-
"""Numpy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l0--aDjtXyhkWDWPBK3RqTKyshndC2xC
"""

#NUMPY Library
import numpy as np
arr = np.array([1,2,3,4,5])
print(f'Array : {arr}')
print(f'Type : {type(arr)}')

#Accessing 1-D array
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[2])

#2-D array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(type(arr))

#Accessing the 2D array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1][3])
print(type(arr))

#Shape of an array
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

#Slicing the array
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[2:5])

#Slicing with Step
import numpy as np
arr = np.array([12, 23,56, 78, 89, 30, 20, 34, 47])
#               0   1   2   3   4   5  6   7   8
print(f'Length of the array : {len(arr)}')
print(arr[2:7])
print(arr[2:7:1])
print(arr[2:7:2])

#Reshape array
import numpy as np
arr = np.array([[1,2,3,4,5,11],[6,7,8,9,10,34]])
print(arr.shape)
#( Rows, Columns)
# 1 2 3 4 5
# 6 7 8 9 10  --> Current

#   1  2
#   3  4
#   5  6
#   7  8
#   9 10    ---> Output

# print(arr.reshape(5,2))
print(arr.reshape(3,4))

import numpy as np
arr = np.array([[1,2,3,4,5,11],[6,7,8,9,10,34]])
arr2  = np.array([1,2,3,4,5,11])

# printing elememts of 2-D array
for i in arr:
    print(i)

# printing elememts of 1-D array
for x in arr2:
    print(x)

#Joining two arrays
import numpy as np
arr1 = np.array([11,26,30,74,85,11])
arr2  = np.array([1,2,3,4,5,19])
print(np.concatenate((arr1,arr2)))
print(np.concatenate((arr2,arr1)))
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
print(np.vstack((arr2,arr1)))

#Splitting array
import numpy as np
arr1 = np.array([11,26,30,74,85,11])
arr2  = np.array([1,2,3,4,5,19])
print(np.split(arr1,6))

#Ascending Order
import numpy as np
arr = np.array([18,26,30,74,85,11])
print(np.sort(arr))

#Searching the elements
import numpy as np
arr = np.array([18,26,30,74,85,11])
print(np.where(arr==4))
print(np.where(arr==85))

#Even Odd
import numpy as np
arr = np.array([18,17, 26,30,74,85,11])

print(np.where(arr%2==0))  #Even
print(np.where(arr%2==1))  #Odd

#Descending Order
import numpy as np
arr = np.array([18,26,30,74,85,11])
print(np.sort(arr)[::-1])
