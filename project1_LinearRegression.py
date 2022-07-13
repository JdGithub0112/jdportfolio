# -*- coding: utf-8 -*-
"""
PROJECT 1: Craigslist Cars - a linear regression approach
"""
#Import libraries needed for this script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in the csv file and obtain general information on the data
df = pd.read_csv('vehicles.csv')
df.columns
df.head(3)

#Nulls/Data Quality Check
df.isnull().any()
print((df.isnull().sum() / df.shape[0]).round(2) * 100)

print(df.description.sample(3))

df['text_len'] = df.description.apply(lambda x: len(str(x)))
(df['text_len'].value_counts() > 1).sum()


df.cylinders.dtype
df.cylinders.value_counts()
df.cylinders = df.cylinders.apply(lambda x: str(x).replace('cylinders','').strip())
df.cylinders.value_counts()


df.cylinders = pd.to_numeric(df.cylinders, errors = 'coerce')
df.cylinders.value_counts()

df.boxplot('price')
print("$", "{:,}".format(df.price.max()))

data_outliers = df[(df.price < df.price.quantile(.995)) & (df.price > df.price.quantile(.005)) & (df.price != 0) & (df.odometer != 0)]
data_outliers = data_outliers[(data_outliers.odometer < data_outliers.odometer.quantile(.995)) & (data_outliers.odometer > data_outliers.odometer.quantile(.005))]

df.boxplot('price')
print("$", "{:,}".format(df.price.max()))
df.boxplot('odometer')
print("{:,}".format(df.odometer.max()))

data_outliers[['price','odometer','cylinders', 'text_len']].hist()
df.isnull().sum()/data_outliers.shape[0]

data_outliers.dropna(subset=['manufacturer','manufacturer','fuel','transmission', 'title_status','year'], inplace = True)
data_outliers.isnull().sum()/data_outliers.shape[0]

data_outliers.cylinders.fillna(data_outliers.cylinders.median(), inplace = True)
data_outliers.isnull().sum()/data_outliers.shape[0]

data_outliers[['condition','VIN','drive','type','paint_color']]= data_outliers[['condition','VIN','drive','type','paint_color']].fillna('n/a')
data_outliers.isnull().sum()/data_outliers.shape[0]

data_outliers.VIN = data_outliers.VIN.apply(lambda x: 'has_vin' if x != 'n/a' else 'no_vin' )

data_final = data_outliers.drop(['id','region_url','url','region','size','description','lat','long','image_url','model','county','posting_date'], axis = 1)
#data_final['constant'] = 1
data_final['age'] = 2022 - data_final.year
data_final.isnull().any()


numeric = data_final._get_numeric_data()

import seaborn as sns

corrdata = numeric

corr = corrdata.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

#set variables need to be in specific format 
X1 = data_final.odometer.values.reshape(-1,1)
y1 = data_final.price.values.reshape(-1,1)


X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.3, random_state=0)


reg = LinearRegression().fit(X_train1, y_train1)
reg.score(X_train1, y_train1)
reg.coef_
y_hat1 = reg.predict(X_train1)

y_hat_test1 = reg.predict(X_test1)
plt.scatter(X_test1, y_test1)
plt.scatter(X_test1, y_hat_test1)
plt.show()