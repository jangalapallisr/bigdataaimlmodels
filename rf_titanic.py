#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##Importing necessary packages
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#from pyspark.sql.functions import sum

dataset = pd.read_csv('/Users/s0j01ys/Desktop/GCP/100-Days-Of-ML-Code-master/datasets/train.csv')

##Checking for missing data  ####SUM function is not wokring............

##NAs = pd.concat([dataset.isnull.sum()],axis=1,keys=["Train"])
##NAs[NAs.sum(axis=1) >0]

##Aforesaid works will ssee AGE/177, Cabin/687, & Embarked/2

##Filling missing Age values with mean - Average
dataset["Age"] = dataset["Age"].fillna(dataset["Age"].mean())
##Filling missing Embarked values with most common values - mode
dataset["Embarked"] = dataset["Embarked"].fillna(dataset["Embarked"].mode()[0])
##Filling missing Cabin values with most common values - mode
dataset["Cabin"] = dataset["Cabin"].fillna(dataset["Cabin"].mode()[0])


##Converting variable to String
dataset["Pclass"] = dataset["Pclass"].apply(str)

##Getting Dummies from all other categorical vars
for col in dataset.dtypes[dataset.dtypes == "object"].index:
    for_dummy = dataset.pop(col)
    dataset = pd.concat([dataset, pd.get_dummies(for_dummy,prefix=col)],axis=1)

target = dataset.pop("Survived")

#Split data for train & test 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(dataset,target,test_size=0.25)

## Create RF model & fit the data to train
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)

##Accuracy Metrics
from sklearn.metrics import roc_curve, auc
false_postive_rate, true_positive_rate, thresholds = roc_curve(y_test,y_pred)
roc_auc = auc(false_postive_rate,true_positive_rate)

###how to set & find the optimal parameters/tuning model to imporve the Accuracy

n_estimators =[1,2,4,8,16,32,64,100,200]
train_results=[]
test_results=[]

for estimator in n_estimators:
    rf = RandomForestClassifier(n_estimators=estimator,n_jobs=-1)
    rf.fit(X_train,y_train)
    train_pred = rf.predict(X_train)
    
    false_postive_rate, true_positive_rate, thresholds = roc_curve(y_train,train_pred)
    roc_auc = auc(false_postive_rate,true_positive_rate)
    train_results.append(roc_auc)
    
    y_pred = rf.predict(X_test)
    false_postive_rate, true_positive_rate, thresholds = roc_curve(y_test,y_pred)
    roc_auc = auc(false_postive_rate,true_positive_rate)
    test_results.append(roc_auc)
    
from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(n_estimators,train_results, "b", lable="Train AUC")
line2, = plt.plot(n_estimators,test_results,"r", label="Test AUC")
plt.legend(handler_map={line1: HandlerLine2D(numpoints-2)})

plt.ylabel("AUC Score")
plt.xlabel("n_Estimators")
plt.show()
    
    