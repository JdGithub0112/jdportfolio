import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('mushrooms.csv')
#print(df.columns)
print(df.head)
print(df.columns)

nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')

print(df.isnull().sum())

def label_encoded(feat):
    le = LabelEncoder()
    le.fit(feat)
    print(feat.name,le.classes_)
#     print(le.classes_)
    return le.transform(feat)

for col in df.columns:
    df[str(col)] = label_encoded(df[str(col)])

df.head()


 
plt.figure(figsize=(12,10))
ax = sns.heatmap(df.corr())
