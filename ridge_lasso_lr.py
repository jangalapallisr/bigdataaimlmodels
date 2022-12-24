#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston

df = load_boston()

dataset = pd.DataFrame(df.data)
dataset.columns = df.feature_names
head = dataset.head()

no_of_rows = df.target.shape

dataset["Price"] = df.target
hhead = dataset.head()
### divid whole dataset into independent features(x)  and dependent fetaurs (y)
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

##Basic LR model implementation
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lr = LinearRegression()
mse = cross_val_score(lr,x,y,scoring='neg_mean_squared_error',cv=7)

mean_mse=np.mean(mse)

##Ridge Regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge=Ridge()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}

ridge_regressor=GridSearchCV(ridge,parameters,scoring='neg_mean_squared_error',cv=5)
rr=ridge_regressor.fit(x,y)
best_rr_param=ridge_regressor.best_params_
best_rr_score=ridge_regressor.best_score_

##LASSO Regression
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

lasso = Lasso()
##use same parameter from Ridge
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
lasso_regressor = GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)
lr =lasso_regressor.fit(x,y)
best_lr_param = lasso_regressor.best_params_
best_lr_score = lasso_regressor.best_score_

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
pred_lasso = lasso_regressor.predict(x_test)
pred_ridge = ridge_regressor.predict(x_test)

import seaborn as sns
sns.distplot(y_test-pred_lasso)
sns.distplot(y_test-pred_ridge)



