#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

messages = pd.read_csv("/Users/s0j01ys/Desktop/GCP/smsspamcollection/SMSSpamCollection", sep="\t", names=["label","message"])
##messages.head()


## Data cleaning & preprocessing
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

corpus = []
ps = PorterStemmer()
wl = WordNetLemmatizer()

for i in range(0,len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    reviwe = review.lower()
    review = review.split()
    
    ##STEMMER OR LEMMATIZER
    ##review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = [wl.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    
    review = ' '.join(review)
    corpus.append(review)


###########Creating  a model - Bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
#cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()

y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values

#####Train test Split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20, random_state=0)

####Train model using Navie Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()
spam_detect_model=nb.fit(x_train,y_train)

y_pred=spam_detect_model.predict(x_test)

##y_test & y_pred are huge list - how to Validate & compare for accuracy -- CONFUSION MATRIX

from sklearn.metrics import confusion_matrix
conf_m = confusion_matrix(y_test,y_pred)

##check Accuracy
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test, y_pred)