import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime 









"""
-----------------------------------------------------------------------------------------------------------------
DATA EXPLORATION PROCESS
-----------------------------------------------------------------------------------------------------------------
"""


#Read in the csv file to a data frame
df = pd.read_csv("uber.csv")
df.info()
df.head()

#Only grab tweets that are in english
df = df[df.language == 'en']
df.head()

#Drop fields not needed for analysis
df = df.drop(['user_id','username','name','link', 'urls','photos', 'video', 'thumbnail','trans_dest','trans_src', 'translate', 'reply_to', 'user_rt','user_rt_id', 'source', 'geo', 'near','search','quote_url','retweet_id','user_id_str','timezone','place'], axis = 1)
df.head()

date_input = df.date
datetimeobject = datetime.strptime(date_input,'%Y%m%d')
df.date = datetimeobject.strftime('%m-%d-%Y')
print(df.date(5))


"""
-----------------------------------------------------------------------------------------------------------------
DATA ANALYSIS PROCESS
-----------------------------------------------------------------------------------------------------------------
"""


