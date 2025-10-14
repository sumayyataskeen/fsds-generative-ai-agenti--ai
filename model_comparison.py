# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 15:50:51 2025

@author: IPL4
"""



import pandas as pd

# Data from your table
data = {
    "Model_Parameters": [
        "lin_reg_2 = LinearRegression()",
        "poly_reg = PolynomialFeatures(degree = 5)",
        "svr_model = SVR()",
        "rf_model = RandomForestRegressor()",
        "knn_model = KNeighborsRegressor()",
        "dt_model = DecisionTreeRegressor()",

        "svr_model = SVR(kernel='sigmoid',degree=3,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='sigmoid',degree=4,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='sigmoid',degree=5,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='poly',degree=2,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='poly',degree=4,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='rbf',degree=3,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='rbf',degree=4,gamma='auto',C=10.0)",
        "svr_model = SVR(kernel='rbf',degree=5,gamma='auto',C=10.0)",

        "knn_model = KNeighborsRegressor(n_neighbors=1,weights='distance',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=1,weights='distance',algorithm='brute',p=2)",
        "knn_model = KNeighborsRegressor(n_neighbors=2,weights='distance',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=2,weights='distance',algorithm='brute',p=2)",
        "knn_model = KNeighborsRegressor(n_neighbors=2,weights='distance',algorithm='auto',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=2,weights='distance',algorithm='ball_tree',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=3,weights='distance',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=3,weights='distance',algorithm='brute',p=2)",
        "knn_model = KNeighborsRegressor(n_neighbors=3,weights='distance',algorithm='ball_tree',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=3,weights='distance',algorithm='ball_tree',p=2)",
        "knn_model = KNeighborsRegressor(n_neighbors=4,weights='distance',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=4,weights='distance',algorithm='ball_tree',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=5,weights='distance',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=5,weights='uniform',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=5,weights='uniform',algorithm='brute',p=2)",
        "knn_model = KNeighborsRegressor(n_neighbors=5,weights='uniform',algorithm='ball_tree',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=4,weights='uniform',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=4,weights='uniform',algorithm='brute',p=2)",
        "knn_model = KNeighborsRegressor(n_neighbors=4,weights='uniform',algorithm='kd_tree',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=4,weights='uniform',algorithm='ball_tree',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=3,weights='uniform',algorithm='brute',p=1)",
        "knn_model = KNeighborsRegressor(n_neighbors=2,weights='uniform',algorithm='brute',p=1)",

        "rf_model = RandomForestRegressor(n_estimators = 100,criterion='squared_error',max_features='sqrt',max_depth=10,min_samples_split=5,min_samples_leaf=2,bootstrap = True,random_state=0)",
        "rf_model = RandomForestRegressor(n_estimators = 100,criterion='absolute_error',max_features='sqrt',max_depth=10,min_samples_split=5,min_samples_leaf=2,bootstrap = True,random_state=0)",
        "rf_model = RandomForestRegressor(n_estimators = 150,criterion='absolute_error',max_features='sqrt',max_depth=10,min_samples_split=5,min_samples_leaf=2,bootstrap = True,random_state=0)",
        "rf_model = RandomForestRegressor(n_estimators = 150,criterion='squared_error',max_features='sqrt',max_depth=10,min_samples_split=5,min_samples_leaf=2,bootstrap = True,random_state=0)",
        "rf_model = RandomForestRegressor(n_estimators = 250,criterion='squared_error',max_features='sqrt',max_depth=10,min_samples_split=5,min_samples_leaf=2,bootstrap = True,random_state=0)",
        "rf_model = RandomForestRegressor(n_estimators = 250,criterion='absolute_error',max_features='sqrt',max_depth=10,min_samples_split=5,min_samples_leaf=2,bootstrap = True,random_state=0)"
    ],

    "Predicted_Salary_for_6.5yrs": [
        330378.78787879, 174878.07765173, 130001.82883924, 160900.0, 168000.0, 150000.0,
        129999.99952992, 129999.99952992, 129999.99952992, 162812.5, 175705.60452113,
        130015.57601565, 130015.57601565, 130015.57601565,
        200000.0, 200000.0, 175000.0, 175000.0, 175000.0, 175000.0,
        192857.14285714, 192857.14285714, 165714.28571429, 165714.28571429,
        182500.0, 182500.0, 175348.8372093, 168000.0, 168000.0, 168000.0,
        190000.0, 190000.0, 190000.0, 190000.0, 216666.66666667, 175000.0,
        167728.86904762, 160150.0, 169000.0, 173226.38888889, 176701.78571429, 168260.0
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("model_salary_predictions.xlsx", index=False)

print("✅ Excel file 'model_salary_predictions.xlsx' created successfully!")
