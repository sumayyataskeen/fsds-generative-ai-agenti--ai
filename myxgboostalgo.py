# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 19:31:50 2025

@author: IPL4
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv(r"C:\Users\IPL4\Downloads\Churn_Modelling.csv")
X = dataset.iloc[:,3:-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)
#encoding categorical data
#label encoding the gender column
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X[:,2]=le.fit_transform(X[:,2])
print(X)
# one hot encoding "geography column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
X=np.array(ct.fit_transform(X))
#splitting the datset into the training set an dtest set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
#training xgboost on the training set
from xgboost import XGBClassifier
classifier=XGBClassifier(n_estimators=30)
classifier.fit(X_train,y_train)
# Predicting Test set results
y_pred = classifier.predict(X_test)

# Confusion Matrix and Accuracy
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

print("Classification Report:\n", classification_report(y_test, y_pred))

# Bias and Variance
bias = classifier.score(X_train, y_train)
variance = classifier.score(X_test, y_test)
print("Bias (Training Accuracy):", bias)
print("Variance (Testing Accuracy):", variance)
# applying k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies=cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=20)
print("Accuracy:{:2f}%".format(accuracies.mean()*100))

