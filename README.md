Jordan Davis Python & R Portfolio
Project 1 -
Project 2 - 
Project 3 - 
Project 4 - 



# Project 1
Build and design our analytical products starting with group-based interviews to understand the business need, then leveraging SQL and Python for data exploration and manipulation into readable forms. Visualizing the data into automated Tableau Server dashboards to be continuously leveraged by customers. 

Maintained and documented metadata for over 50 unique metrics and measurements across our analytic products. The data stems from eight different business lines and over 35 points of contact within areas including but not limited to Federal Reserve Operations, Cybersecurity, and Customer Satisfaction.
Perform qualitative sentiment analysis on Incident and Change descriptions to better equip leadership with context to why certain incidents occur, and how we can best avoid them as a business moving forward.

'
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
'
(   https://github.com/JdGithub0112/Jordan-Davis---Portfolio/blob/main/project1_DataInfo.png)
