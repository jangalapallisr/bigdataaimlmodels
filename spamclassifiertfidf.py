#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
messages=pd.read_csv("/Users/s0j01ys/Desktop/GCP/smsspamcollection/SMSSpamCollection",sep='\t', names=['label','message'])

##IMPORTS LIBS

import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
wl=WordNetLemmatizer()
corpus=[]

##DATA PREPROCESSING
for i in range(0,len(messages['message'])):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    ##Lemmatizing....
    review = [wl.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
 
###CREATING TF IDF model
from sklearn.feature_extraction.text import TfidfVectorizer
#tv=TfidfVectorizer()
tv=TfidfVectorizer(max_features=1500)
x=tv.fit_transform(corpus).toarray()

##select one categorical varaible instead of two - its dummy trap
y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values

####TRAIN & TEST SPLIT
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20, random_state=0)

### TRAIN MODEL USING NAIVE BAYES Classifier 
from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()
spam_detect_model=nb.fit(x_train,y_train)

y_pred = spam_detect_model.predict(x_test)

##Compare y_test & y_pred, its huge list so compare by using confusion matrix
from sklearn.metrics import confusion_matrix
conf_m = confusion_matrix(y_test,y_pred)

## find Accuracy Level
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)