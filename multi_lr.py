#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('/Users/s0j01ys/Desktop/01292021/GCP/100-Days-Of-ML-Code-master/datasets/50_Startups.csv')
head=dataset.head()
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

##conver the column into categorical columns into one-hot encoding; here drop_first removes the first column
states = pd.get_dummies(x['State'], drop_first=True)

## Droping the String/Cataegorical feature 'State' column from list if independent features
xx=x.drop('State', axis=1)

##concat the dummy variable trap (Categorical variables/columns those get converted into one-hot encoding)
X=pd.concat([xx,states],axis=1)

##Split the data set into train & test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)

#Fitting Multiple Linear Regression to the Training set;  simple LR & Multiple LR same lib LinearRegression only
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

#Predicting the test set results
y_pred = lr.predict(x_test)

##Accuracy check
from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)
print (score)