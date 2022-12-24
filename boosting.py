#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

dataset = pd.read_csv('/Users/s0j01ys/Desktop/GCP/100-Days-Of-ML-Code-master/datasets/mushroom_csv.csv')
dataset =dataset.sample(frac=1)
##frac??
#dfcol = dataset.columns
#dataset.columns=['target','cap-shape', 'cap-surface', 'cap-color', 'bruises%3F', 'odor',
#       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
 ##     'stalk-surface-below-ring', 'stalk-color-above-ring',
   #    'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
    #   'ring-type', 'spore-print-color', 'population', 'habitat']

for label in dataset.columns:
    dataset[label] = LabelEncoder().fit(dataset[label]).transform(dataset[label])
    
##dataset.info()
X=dataset.drop(['target'],axis=1)
y=dataset['traget']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
DTC= DecisionTreeClassifier(criterion=entropy, max_depth=1)

abc = AdaBoostClassifier(base_estimator=DTC,n_estimators=400, learning_rate=1)
model = abc.fit(X_train,y_train)

y_pred=model.predict(x_test)

Accuracy = metrics.accuracy_score(y_test,y_pred)


