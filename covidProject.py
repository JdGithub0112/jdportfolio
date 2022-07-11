# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 23:15:43 2022

@author: Matt
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import urllib
from selenium import webdriver

"""
-----------------------------------------------------------------------------------------------------------------
DATA EXPLORATION PROCESS
-----------------------------------------------------------------------------------------------------------------
"""
driver = webdriver.Chrome(executable_path=r'C:/Users/Matt/Desktop/Portfolio/chromedriver.exe')
#Connecting to the live data source on the WHO Website
url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"

file_path = os.path.join("data", "covid")

os.makedirs(file_path, exist_ok=True)

csv_path = os.path.join(file_path,"WHO-COVID-19-global-data.csv")
#URL Lib Module
urllib.request.urlretrieve(url,csv_path)
#Use Pandas to read the csv into a dataframe for analysis
df = pd.read_csv(csv_path)

#url_CountryCodes
table_countryCodes = pd.read_html("https://www.iban.com/country-codes")
table_countryCodes[0].dtypes
df_CountryCodes = pd.DataFrame(table_countryCodes)
print(df_CountryCodes)


driver.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")
html = driver.page_source
table_GDP = pd.read_html(html)
data = table_GDP[1]
driver.close()
df_table_GDP = pd.DataFrame(table_GDP)
print(df_table_GDP)

"""
Here are some data exploration statements using the pandas library to obtain a better
understanding of the data that I'm analyzing
"""
#Print out some basic data explorations functions from Pandas
#print(df.info())
#Print out the first five rows (records 0-4) to get an understanding of data structure
#print(df.head(5))
#Understanding the 'Country_code' field so that I can sort or group countries as need be
#print(df['Country_code'].unique())
#print(df df['Country'].unique())

#Create a dataframe that only has USA data, we use the field 'Country Code' to 
df_USA = df[df["Country_code"] == 'US'].copy()
df_Brazil = df[df["Country"] == 'Brazil'].copy()

#Format the date field 'Date_reported' to a Y-M Format
df['Date_reported'] =  pd.to_datetime(df['Date_reported'], format='%Y-%m-%d')
#Determine the size of the plot I'm generating, since I'm using a landscape mode I went with 18 by 6
plt.figure(figsize=(18,6))
#Lineplots leveraging the dataframes that I created for both the USA and China
#Date_reported field as th x-axis, New_cases field as the y-axis, color coordinating both lines respectively
sns.lineplot(data=df_USA, x =df['Date_reported'], y=df_USA['New_cases'], color = 'blue')
sns.lineplot(data=df, x =df['Date_reported'], y=df_Brazil['New_cases'], color = 'green')



#Titling the plot that I am generating
plt.title('New COVID-19 Cases in the USA and Brazil')
plt.xticks(rotation=45)


"""
for col in df:
    print("")
    print([col])
    print(df[col].unique())
"""


#df.info()
#print(df.head(5))
#print(df.describe())

#df['year'] = pd.DatetimeIndex(df['Date_reported']).year
#df['month'] = pd.DatetimeIndex(df['Date_reported']).month

#df['DATE'] = pd.to_datetime(df[['year', 'month']].assign(DAY=1))

#print(df[df.Country == 'United States of America'])
#df_cols = df.columns
#df_index = df.index
#print(df.dtypes)
#print(df_index)
#print(df_cols)
"""
plt.plot(df.Date_reported,df.New_cases, df.Country == 'United States of America')
plt.title('New Covid Cases over Time')
plt.xlabel('Date Reported')
plt.ylabel('New Cases Count')
#fig, ax = plt.subplots()
#ax.plot([datetime.date(2020,12,31), datetime.date(2023,12,31)])
plt.show()
"""