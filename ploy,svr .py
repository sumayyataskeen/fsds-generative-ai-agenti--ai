# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 15:13:14 2025

@author: IPL4
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
emp_set = pd.read_csv(r'C:\Users\IPL4\Downloads\emp_sal.csv')
x = emp_set.iloc[:,1:2].values
y = emp_set.iloc[:,2].values
lin_reg = LinearRegression()
lin_reg.fit(x,y)
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x),color = 'blue')
plt.title("LinearRegression graph")
plt.xlabel("Position Level")
plt.ylabel("Salary")
#Poly-model comparision
poly_reg = PolynomialFeatures(degree = 5)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)
plt.scatter(x,y,color = 'red')
plt.plot(x,lin_reg.predict(x),color = 'blue')
plt.title("Truth bluff")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()
lin_reg_pred = lin_reg.predict([[6.5]])
print("LienarRegression",lin_reg_pred)
poly_reg_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print("Polynomial Regression",poly_reg_pred)
svr_model = SVR()
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("svr_model",svr_model_pred)
#with sigmoid
svr_model = SVR(kernel='sigmoid',degree=3,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("Sigmoid",svr_model_pred)
#sigmoid with degree 4
svr_model = SVR(kernel='sigmoid',degree=4,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])

print("Sigmoid4",svr_model_pred)
#Sigmoid with degree 5
svr_model = SVR(kernel='sigmoid',degree=5,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("Sigmoid5",svr_model_pred)
#Poly with 2
svr_model = SVR(kernel='poly',degree=2,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("Poly2",svr_model_pred)
#Poly4
svr_model = SVR(kernel='poly',degree=4,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("poly4",svr_model_pred) #175705 right prediction
#Rbf 3
svr_model = SVR(kernel='rbf',degree=3,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("Rbf3",svr_model_pred)
#rbf 4
svr_model = SVR(kernel='rbf',degree=4,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("rbf 4",svr_model_pred)
#rbf 5
svr_model = SVR(kernel='rbf',degree=5,gamma='auto',C=10.0)
svr_model.fit(x,y)
svr_model_pred = svr_model.predict([[6.5]])
print("rbf5",svr_model_pred)
plt.scatter(x,y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color ="blue")
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()