# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 19:49:12 2025

@author: IPL4
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\IPL4\Downloads/logit classification.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into Training and Test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc =StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)"""
# decisiontree
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion="gini", splitter="best", max_depth=20,  min_samples_leaf=8, )
classifier.fit(X_train,y_train)
#predicting test set result
y_pred=classifier.predict(X_test)
# Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Accuracy
ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

# Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Bias and Variance
bias = classifier.score(X_train, y_train)
variance = classifier.score(X_test, y_test)
print("Bias (Training Accuracy):", bias)
print("Variance (Testing Accuracy):", variance)
#next furure