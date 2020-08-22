#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()
data = pd.read_csv("data.csv")
data.head(7)

#number of rows and columns
data.shape

data = data.dropna(axis=1)
data["diagnosis"].value_counts()

sns.countplot(data["diagnosis"], label="count")

from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
data.iloc[:,1] = labelencoder_Y.fit_transform(data.iloc[:,1].values)

#Creating pairplot
sns.pairplot(data.iloc[:, 1:5], hue="diagnosis")

#Getting correlation
data.iloc[:,1:12].corr()

#Visualizing correlation
sns.heatmap(data.iloc[:,1:12].corr(), annot = True)
plt.figure(figsize = (10,10))

#splitting into independent and dependent data
X = data.iloc[:,2:31].values
Y = data.iloc[:,1].values

#splitting into training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#creating a function for the models
def models(X_train, Y_train):

  #logistic regression
  from sklearn.linear_model import LogisticRegression
  log = LogisticRegression(random_state = 0)
  log.fit(X_train, Y_train)

  #decision tree
  from sklearn.tree import DecisionTreeClassifier
  tree = DecisionTreeClassifier(criterion = "entropy", random_state = 0)
  tree.fit(X_train, Y_train)
  
#Getting models
models = models(X_train, Y_train)

#testing accuracy on confusion matrix
from sklearn.metrics import confusion_matrix
for i in range(len(models)):
  print("Model: ",i)
  cm = confusion_matrix(Y_test, models[i].predict(X_test))

  TP = cm[0][0]
  TN = cm[1][1]
  FN = cm[1][0]
  FP = cm[0][1]

  print(cm)
  print("Training Accuracy: ", (TP + TN)/ (TP + TN + FP + FN))
  print()
  
#forest classifier has highest accuracy
#printing forest classifier prediction

pred = models[2].predict(X_test)
print("Model Predicted: \n",pred)
print()
print("Real diagnosis results: \n",Y_test)

  #random forest classifier
  from sklearn.ensemble import RandomForestClassifier
  forest = RandomForestClassifier(n_estimators = 10, criterion = "entropy", random_state = 0)
  forest.fit(X_train, Y_train)

  #printing accuracy model
  print("[0]Logistic Regression Training Accuracy: ",log.score(X_train, Y_train))
  print("[1]Decision Tree Classifier Training Accuracy: ",tree.score(X_train, Y_train))
  print("[2]Random Forest Classifier Training Accuracy: ",forest.score(X_train, Y_train))

  return log, tree, forest
