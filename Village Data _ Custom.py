# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nGYv07dhdGZKITOTO1ZfBzfDhKjySXcD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

num_citizens = 350

ages = np.random.randint(0, 110, size=num_citizens)
genders = np.random.choice(['Male', 'Female'], size=num_citizens)
marital_status = np.random.choice(['Married','Single','Divorced','Widowed'],size=num_citizens)
educational_status = np.random.choice(['High School','Bachelor','Master','PhD','Other'],size=num_citizens)
religion = np.random.choice(['Islam','Christianity','Hinduism','Buddhism','Judaism','Other'],size=num_citizens)
eligible_to_vote = np.random.choice([True, False], size=num_citizens)

village_data = pd.DataFrame({
    'Age':ages,
    'Gender':genders,
    'Marital Status':marital_status,
    'Educational Status':educational_status,
    'Religion':religion,
    'Eligible to Vote':eligible_to_vote
})

age_stats = village_data['Age'].describe()
# print(age_stats)
gender_stats = village_data['Gender'].value_counts(normalize=True)
#print(gender_stats)
marital_status_stats = village_data['Marital Status'].value_counts(normalize=True)
# print(marital_status_stats)
educational_status_stats = village_data['Educational Status'].value_counts(normalize=True)
# print(educational_status_stats)
religion_stats = village_data['Religion'].value_counts(normalize=True)
# print(religion_stats)
vote_stats = village_data['Eligible to Vote'].value_counts(normalize=True)
# print(vote_stats)

# https://coolors.co/palettes/trending -- Colors

#Visulisation of Data
plt.figure(figsize=(10, 6))
plt.pie(gender_stats, labels=gender_stats.index, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.show()

plt.figure(figsize=(10, 6))
plt.pie(marital_status_stats, labels=marital_status_stats.index, autopct='%1.1f%%' ,colors=['#ffb703','#e63946'])
plt.title('Marital Status Distribution')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(village_data['Age'], bins=20, edgecolor='black',color='#bc6c25')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(educational_status_stats.index, educational_status_stats)
plt.title('Educational Status Distribution')
plt.xlabel('Educational Status')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(religion_stats.index, religion_stats,color=['#e63946','#fca311','#283618','#e63946','#03045e'])
plt.title('Religion Distribution')
plt.xlabel('Religion')
plt.ylabel('Frequency')
plt.show()
myExplode=[0.1,0]
plt.figure(figsize=(10, 6))
plt.pie(vote_stats, labels=vote_stats.index, autopct='%1.1f%%',colors=['#283618','#e63946'],explode=myExplode)
plt.title('Eligible to Vote Distribution')
plt.show()