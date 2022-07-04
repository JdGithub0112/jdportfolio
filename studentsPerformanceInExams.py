# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:57:43 2022

@author: Matt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("StudentsPerformance.csv")

print(len(df))
print(df.info())
"""
I wanted to know mor abaout the parental leveel of education field and did
some exploration here

"""
#print('parental level of education')
#print(df['parental level of education'].unique())


#Using 'for' we can iterate through every column and get their unique values
#I've added the extra line and column name for better usability
for col in df:
    print("")
    print([col])
    print(df[col].unique())