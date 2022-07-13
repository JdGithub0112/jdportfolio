# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 23:15:43 2022

@author: Matt
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
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
#Covid data is typically reported in a weekly basis where the weekend reporting numbers affect the line shape
#This makes it difficult to read the line graph, therefore the line below will create a new numeric field and store it as the rolling 7 day sum
df_Final['New_cases_Mov_avg'] = df_Final['New_cases'].rolling(7).sum()

#Printing out the final Dataframe to a CSV file for optional Tableau Dashboard Visualization
df_Final.to_csv("df_Final_Output.csv",encoding='utf-8')

"""
-----------------------------------------------------------------------------------------------------------------
DATA VISUALIZATION PROCESS
-----------------------------------------------------------------------------------------------------------------
"""
#Overall Plot that shows New Cases Moving Average over Time (Date_reported) field
df_Final.plot.line(x='Date_reported', y='New_cases_Mov_avg', xlabel='Date Reported', ylabel='New Cases (Moving Average)')

#Detailed plot that shows Year-to-date New Cases Moving Average over Time (using the Date_reported) field

#Create the figure size, since this is a time series I'd like a landscape like shape and went with 15x8
fig, ax = plt.subplots(figsize=(15,8))
#Creating the plot itself using Seaborn, x-axis is the 'Date_reported' field, y-axis is the 'New_cases_Mov_avg' field
sns.lineplot(data=df_Final, x='Date_reported', y='New_cases_Mov_avg',
#hue='Continent' groups the lines by the 'Continent' field, linewidth established, no confidence interval
                        hue='Continent', linewidth=2, ci=None, ax=ax)

#Some formatting changes with the appearance
sns.set_style("white")
sns.set_style('ticks')
#Setting labels and title
ax.set_title("New COVID-19 Cases (Moving Avg.) by Continent")
ax.set_xlabel("Date Reported")
ax.set_ylabel("New Cases (Moving Average)")
#Making the plot YTD by establishing the xlim to Jan 1 2022
ax.set_xlim(datetime.date(2022, 1, 1))
#Formart to the date axis range
fig.autofmt_xdate()

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
