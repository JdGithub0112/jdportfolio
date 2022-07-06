# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:57:43 2022

@author: Matt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
df = pd.read_csv("StudentsPerformance.csv")


"""
-----------------------------------------------------------------------------------------------------------------
DATA EXPLORATION PROCESS
-----------------------------------------------------------------------------------------------------------------
"""

"""
Before doing any analysis work, I run two functions len and info to grab the
high-level information neeeded to get to know the structure and size of the dataset 
and field data types I'll be working with'
"""

print(len(df))
print(df.info())


"""
I wanted to know mor abaout the parental leveel of education field and did
some exploration here
"""
#print('parental level of education')
#print(df['parental level of education'].unique())

"""
Using 'for' we can iterate through every column and get their unique values
I've added the extra line and column name for better usability
"""
for col in df:
    print("")
    print([col])
    print(df[col].unique())
    
    
"""
 Calculating the mean scores across the data set
 
"""
#Using the .mean() to find the average score for each column in our data frame
mathScore = df['math score'].mean()
readingScore = df['reading score'].mean()
writingScore = df['writing score'].mean()

print("Average Math Score:" , round(mathScore, 2),"%")
print("Average Reading Score:" , round(readingScore, 2),"%")
print("Average Writing Score:" , round(writingScore, 2),"%")




"""
-----------------------------------------------------------------------------------------------------------------
LEVERAGING MATPLOTLIB FOR BASIC DATA ANALYSIS
-----------------------------------------------------------------------------------------------------------------
"""


x = df['parental level of education']
y = ['math score']

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y, color='green')
plt.xlabel("Parental Level of Education")
plt.ylabel("Math Score")
plt.title("Parentl Level of Education and its impact on child's math scoring")

plt.xticks(x_pos, x)
plt.show()
print("Hello Test")
