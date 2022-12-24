#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = datasets.load_iris()
X=iris.data
y=iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

abc = AdaBoostClassifier(n_estimators=50,learning_rate=1)
model=abc.fit(X_train,y_train)
y_pred=model.predict(X_test)

Accuracy = metrics.accuracy_score(y_test,y_pred)


####USE DIfferent BASE LEARNER
##SVC - SUPPORT VECTOR CLASSIFIER

from sklearn.svm import SVC

svc = SVC(probability=True, kernel='linear')
svc_abc=AdaBoostClassifier(n_estimators=50,base_estimator=svc,learning_rate=1)
svc_model = svc_abc.fit(X_train,y_train)
svc_y_pred=svc_model.predict(X_test)

svc_accuracy = metrics.accuracy_score(y_test,svc_y_pred)




