# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 23:15:43 2022

@author: Matt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
#Webscrape Continent groups and additional country data
table_Continents = pd.read_html("https://statisticstimes.com/geography/countries-by-continents.php", match = "Countries or Areas")
df_Continents = pd.DataFrame(table_Continents[0])
#Change Country or area to country
df_Continents.rename(columns = {'Country or Area' : 'Country'}, inplace = True)
#print(df_Continents)
df_Final = df.merge(df_Continents, on='Country', how='left')

#Create a dataframe that only has USA data, we use the field 'Country Code' to 
df_USA = df_Final[df_Final.Country == 'United States of America']
df_Europe = df_Final[df_Final.Continent == 'Europe']

#Format the date field 'Date_reported' to a Y-M Format
df_Final['Date_reported'] =  pd.to_datetime(df_Final['Date_reported'], format='%Y-%m')
df_Final['New_cases_Mov_avg'] = df_Final['New_cases'].rolling(7).sum()

df_Final.to_csv("df_Final_Output.csv",encoding='utf-8')

"""
-----------------------------------------------------------------------------------------------------------------
DATA VISUALIZATION PROCESS
-----------------------------------------------------------------------------------------------------------------
"""

finalPlot = sns.relplot(kind='line', data=df_Final, x='Date_reported', y='New_cases_Mov_avg',
                        hue='Continent', linewidth=1, ci=None, figsize=(18,6))
#Determine the size of the plot I'm generating, since I'm using a landscape mode I went with 18 by 6

#print(df_Final)





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
