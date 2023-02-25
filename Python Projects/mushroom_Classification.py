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


#Another way of writing this is df.shape() to obtain rows and columns respectively
nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')

print(df.isnull().sum())

df = df.drop('veil-type', axis=1)

def label_encoded(feat):
    le = LabelEncoder()
    le.fit(feat)
    print(feat.name,le.classes_)
#     print(le.classes_)
    return le.transform(feat)

for col in df.columns:
    df[str(col)] = label_encoded(df[str(col)])

df.head()

 #use matplotlib library to call function figure to size
 #length and width of output.
plt.figure(figsize=(12,10))
#plt.style.use("dark_background")
#Seaborn to plot a correalation heatmap
ax = sns.heatmap(df.corr())

fig = plt.figure(figsize = (20,15))
ax = fig.gca()
df.hist(ax=ax)
plt.show()

corr = df.corr()
rela = corr['class'].sort_values(ascending = False)
rela

plt.subplots(figsize=(12, 12))
sns.heatmap(corr, annot = True) 
