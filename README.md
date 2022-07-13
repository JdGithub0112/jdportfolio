# Jordan Davis' Python Portfolio
Please find below all of my Python projects. I cover five aspects of data analysis and data science. Explaratory Data Analysis (cleaning & wrangling, Data Visuazliation, something something something
<br>
* [LinkedIn](https://www.linkedin.com/in/jordandavis0112/)
* [Resume](https://github.com/JdGithub0112/Jordan-Davis---Portfolio/blob/main/JordanDavis_Resume_2022.pdf)


### Pandas Project
#### *Wrangling, joining, and cleaning World Health Organization Data for analysis and visualization*
In this project I wanted to demonstrate my contempency on using Pandas for organizing and cleaning my data to end up with a dataframe for analysis. In this scenario, I wanted to learn how to scrape data from the web to have up-to-date information for my plots. The data in question comes from the World Health Organization and displays Covid cases/deaths data since early 2020 (cadence for update is everyday).

I began my explaratory data analysis by web scraping data from The [World Health Organization's website](https://covid19.who.int/data). I used the urllib library to pass through the csv data hosted on the WHO site to a csv file in my current file path where my Python script lived. I also web scraped data from the [Statistics Times Website](https://statisticstimes.com/geography/countries-by-continents.php) for country data so that I could add Continent data to my dataframe.

In oder to merge the two tables, I performed a left join on the 'Country' field alongside some general formatting to prep for the data visualization process.

*Excerpt from Code (pandasProject_CovidCaseData.py)*

`df_Continents.rename(columns = {'Country or Area' : 'Country'}, inplace = True)`

`df_Final = df.merge(df_Continents, on='Country', how='left')`


![Image Detail](images/Project1_fig1.png)
something

### Project 1: Craigslist Cars - a linear regression approach
Question/Problem Statement:

*In statistics, linear regression is a linear approach for modelling the relationship between a scalar response and one or more explanatory variables (also known as dependent and independent variables). - wikipedia*
