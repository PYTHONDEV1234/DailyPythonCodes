# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fwOy-bP8tAQl7l_ij-kzuRT1ovT07ICI
"""

import matplotlib as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,24])

plt.pyplot.plot(x,y)
plt.pyplot.show()

x = np.array([0,10])
y = np.array([0,24])

plt.pyplot.plot(x,y,'*')
plt.pyplot.show()

x = np.array([0,2,5,7,10])
y = np.array([0,6,11,19,24])

plt.pyplot.plot(x,y,'*')
plt.pyplot.show()

x = np.array([0,2,5,7,10])
y = np.array([0,6,11,19,24])

plt.pyplot.plot(x,y,'o')
plt.pyplot.show()

x = np.array([0,5,2,7,10])
y = np.array([0,6,10,9,24])

plt.pyplot.plot(x,y)
plt.pyplot.show()

z = np.array([3,1,6,8,10])
plt.pyplot.plot(z,marker='^')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
plt.pyplot.plot(z,'o-',ms=20)
plt.pyplot.show()

z = np.array([3,1,6,8,10])
plt.pyplot.plot(z,'o-',ms=20,mec='hotpink', mfc='hotpink')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.plot(z,linestyle='dotted')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.plot(z,color='r',linewidth='20')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.plot(z,color='r')
plt.pyplot.plot(x,color='hotpink')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.xlabel('Amount')
plt.pyplot.ylabel('Price (in Dollars) ')
plt.pyplot.plot(z,color='r')
plt.pyplot.plot(x,color='hotpink')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.title('Daily Expenditure')
plt.pyplot.xlabel('Amount')
plt.pyplot.ylabel('Price (in Dollars) ')
plt.pyplot.plot(z,color='r')
plt.pyplot.plot(x,color='hotpink')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.title('Daily Expenditure',loc='left')
plt.pyplot.xlabel('Amount')
plt.pyplot.ylabel('Price (in Dollars) ')
plt.pyplot.plot(z,color='r')
plt.pyplot.plot(x,color='hotpink')
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.title('Daily Expenditure',loc='left')
plt.pyplot.xlabel('Amount')
plt.pyplot.ylabel('Price (in Dollars) ')
plt.pyplot.plot(z,color='r')
plt.pyplot.plot(x,color='hotpink')
plt.pyplot.grid()
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.title('Daily Expenditure',loc='left')
plt.pyplot.xlabel('Amount')
plt.pyplot.ylabel('Price (in Dollars) ')
plt.pyplot.plot(z,color='r')
plt.pyplot.plot(x,color='hotpink')
plt.pyplot.grid(color='hotpink',linestyle='--',linewidth=0.5)
plt.pyplot.show()

z = np.array([3,1,6,8,10])
x = np.array([0,4,9,14,8])

# plt.pyplot.plot(z,linestyle='dashed')
plt.pyplot.title('Daily Expenditure',loc='left')
plt.pyplot.xlabel('Amount')
plt.pyplot.ylabel('Price (in Dollars) ')
plt.pyplot.scatter(z,x)
# plt.pyplot.plot(x,color='hotpink')

x = np.array([10,20,13,8,40])
y = np.array([12,45,6,23,17])

plt.pyplot.bar(x,y)
plt.pyplot.show()

x = np.array([10,20,13,8,40])
y = np.array([12,45,6,23,17])

plt.pyplot.barh(x,y)
plt.pyplot.show()

x = np.array([10,20,13,8,40])
y = np.array([12,45,6,23,17])

plt.pyplot.hist(x)
plt.pyplot.show()

x = np.array([10,20,13,8,40])
y = np.array([12,45,6,23,17])
myExplode=np.array([0,0,0,0,0.4])
plt.pyplot.pie(x)
myLabels = ['A','B','C','D','E']
plt.pyplot.pie(y, labels=myLabels)
plt.pyplot.legend(title="Categories:")

plt.pyplot.show()