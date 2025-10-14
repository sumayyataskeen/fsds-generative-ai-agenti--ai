# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 15:59:16 2025

@author: IPL4
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 9, 2025
@author: Sumayya
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# -----------------------------------
# Title and Description
# -----------------------------------
st.title("💼 Salary Prediction using Different Regression Models")
st.write("This app predicts employee salary based on position level using multiple regression algorithms.")

# -----------------------------------
# Upload Dataset
# -----------------------------------
uploaded_file = st.file_uploader("📁 Upload your CSV file (Position, Level, Salary)", type=["csv"])

if uploaded_file is not None:
    dataset = pd.read_csv(uploaded_file)
    st.subheader("📊 Dataset Preview")
    st.write(dataset.head())

    # Extract independent & dependent variables
    x = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, 2].values

    # Input for prediction
    level = st.number_input("Enter Position Level for Salary Prediction:", min_value=float(x.min()), max_value=float(x.max()), value=6.5, step=0.1)

    # -----------------------------------
    # Linear Regression
    # -----------------------------------
    lin_reg = LinearRegression()
    lin_reg.fit(x, y)
    lin_pred = lin_reg.predict([[level]])[0]

    # -----------------------------------
    # Polynomial Regression
    # -----------------------------------
    poly_reg = PolynomialFeatures(degree=4)
    x_poly = poly_reg.fit_transform(x)
    lin_reg2 = LinearRegression()
    lin_reg2.fit(x_poly, y)
    poly_pred = lin_reg2.predict(poly_reg.fit_transform([[level]]))[0]

    # -----------------------------------
    # SVR
    # -----------------------------------
    svr_model = SVR(kernel='poly', degree=4, gamma='auto', C=10.0)
    svr_model.fit(x, y)
    svr_pred = svr_model.predict([[level]])[0]

    # -----------------------------------
    # KNN
    # -----------------------------------
    knn_model = KNeighborsRegressor(n_neighbors=5, weights='distance', algorithm='brute', p=1)
    knn_model.fit(x, y)
    knn_pred = knn_model.predict([[level]])[0]

    # -----------------------------------
    # Decision Tree
    # -----------------------------------
    dt_model = DecisionTreeRegressor()
    dt_model.fit(x, y)
    dt_pred = dt_model.predict([[level]])[0]

    # -----------------------------------
    # Random Forest
    # -----------------------------------
    rf_model = RandomForestRegressor(n_estimators=30, random_state=0)
    rf_model.fit(x, y)
    rf_pred = rf_model.predict([[level]])[0]

    # -----------------------------------
    # Show Predictions
    # -----------------------------------
    st.subheader("📈 Model Predictions for Level = {:.1f}".format(level))
    results = {
        "Linear Regression": lin_pred,
        "Polynomial Regression (deg=4)": poly_pred,
        "SVR (poly kernel)": svr_pred,
        "KNN Regressor": knn_pred,
        "Decision Tree": dt_pred,
        "Random Forest": rf_pred,
    }
    st.write(pd.DataFrame(results.items(), columns=["Model", "Predicted Salary (₹)"]))

    # -----------------------------------
    # Plotting
    # -----------------------------------
    st.subheader("📉 Regression Visualizations")
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(x, y, color='red', label='Actual Data')
    ax.plot(x, lin_reg.predict(x), color='blue', label='Linear Regression')
    ax.plot(x, lin_reg2.predict(x_poly), color='green', label='Polynomial Regression (deg=4)')
    ax.legend()
    ax.set_xlabel("Position Level")
    ax.set_ylabel("Salary")
    st.pyplot(fig)

else:
    st.info("👆 Please upload your CSV file to start.")

