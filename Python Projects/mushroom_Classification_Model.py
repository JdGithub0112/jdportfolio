import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# load the dataset
df = pd.read_csv('mushrooms.csv')

# drop 'veil-type' column
df = df.drop('veil-type', axis=1)

# label encode the features and target variables
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

# split the data into training and testing sets
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# create a KNN classifier with k=5
knn = KNeighborsClassifier(n_neighbors=3)

# train the model on the training data
knn.fit(X_train, y_train)

# make predictions on the testing data
y_pred = knn.predict(X_test)

# calculate the accuracy score of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
#KNN of 3 produces a 99.7% accuracy to predict the edible class of a mushroom based
#off its features characteristics
