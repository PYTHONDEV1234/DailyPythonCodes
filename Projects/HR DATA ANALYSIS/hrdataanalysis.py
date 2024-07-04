# -*- coding: utf-8 -*-
"""HRDataAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PVewqORkByL0snGqmA9-gk95L65kgEcv
"""

import numpy as np
import pandas as pd

np.random.seed(42)

data = {
    'employee_id':np.arange(1,101),
    'name':np.random.choice(['Ansel','Bob','Caron','Dolly','Evan','Fredy','George','Hills','Irik'],100),
    'salary':np.random.choice([10000,100000],100),
    'genders':np.random.choice(['Male','Female'],100),
    'department':np.random.choice(['HR','Finance','Marketing'],100),
    'releigion':np.random.choice(['Islam','Hindu','Buddist','Christian'],100),
    'age':np.random.choice([20,25,30,20,np.nan, 19,np.nan,45,np.nan],100),
}
df = pd.DataFrame(data)
rename={
    'employee_id':'ID',
    'salary':'Monthly_salary',
    'genders':'Gender',
    'department':'Department',
    'releigion':'Religion'
}
df['name']=df['name'].str.upper()
df.drop_duplicates(inplace=True)
df.rename(columns=rename,inplace=True)

# df.dropna(inplace=True)
# df.addNaN(10,inplace=True)
# df.NaN.replace(np.nan,0,inplace=True)

print(df.head(20))


#Count the number of employees with names as GEORGE  or NUber of employees with Salaarues equal to 10000
# how many employees are older than 56 years
# Visualizations

