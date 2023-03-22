
<h1>Python Projects Detail</h1>

### Welcome to my GitHub Python Project Portfolio! This repository showcases my skills in data exploration and analysis using Python.

#### Mushroom Project

.py files:

[Exploratory Analysis](https://github.com/JdGithub0112/Jordan-Davis-Python-Portfolio/blob/main/Python%20Projects/mushroom_Classification_ExploratoryAnalysis.py)

[K Nearest Neighbor Classification Model](https://github.com/JdGithub0112/Jordan-Davis-Python-Portfolio/blob/main/Python%20Projects/mushroom_Classification_Model.py)

### Exploring and Preparing our Data for Analysis
Label encoding is a technique for converting categorical data into numerical data by assigning a unique numerical value to each category. This is often done in machine learning tasks to prepare the data for modeling and is useful for correlation plots as seen below.

#### Understand correlations, if any - present in the dataset
By calculating the correlation between various physical attributes, such as cap size, stalk length, or gill spacing, and the mushroom's edibility or toxicity, we can determine which attributes are most strongly predictive of whether or not a mushroom is safe to eat. This information can be used to develop a classification model that accurately predicts a mushroom's edibility based on its physical characteristics.

#### Building Classification model using KNN begins with creating a training and testing split (70,30)

In order to test our model we'll have to split our dataset into a training (70% of the dataset) and testing (30% of the dataset) portions. This trains our model to obtain a better understanding of which mushrooms are edible or poisonous based off of the features associated. Then we 'test' our model on the remaining 30% of the unseen test data to access how accurate it can make its prediction of a mushroom being edible or not.

#### Final Result and Model Performance

When using a K-value of 5, the accuracy percentage output was 99.5%. Substituting the K-value to 3 yielded an accuracy percentage of **99.7%**

In general, a good classification model should have an accuracy that is significantly higher than the random chance level. For example, if there are two classes and the data is evenly distributed, the random chance level is 50%. In this case, a model that achieves an accuracy of 70% or higher would be considered good. In regards to mycology classification, 99.7% may not be sufficient - but for a basic classification model it is quite accurate.

---


#### Covid-19 Project
covid_data_exploration.py: This script explores the COVID-19 dataset, which contains information about the number of cases and deaths in various countries. The script uses the Pandas library to load and clean the data, and then creates visualizations to help understand the data.

.py files:

[Exploratory Analysis](https://github.com/JdGithub0112/Jordan-Davis-Python-Portfolio/blob/main/Python%20Projects/Covid-19_CaseData.py)
