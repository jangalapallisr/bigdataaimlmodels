#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings("ignore")
import nltk

paragraph = """Dr. APJ Abdul Kalam is a famous name in the whole world. He is counted among the greatest scientists of the 21st century. Even more, he becomes the 11th president of India and served his country. He was the most valued person of the country as his contribution as a scientist and as a president is beyond compare. Apart from that, his contribution to the ISRO (Indian Space Research Organization) is remarkable. He headed many projects that contributed to the society also he was the one who helped in the development of Agni and Prithvi missiles. For his involvement in the Nuclear power in India, he was known as “Missile Man of India”. And due to his contribution to the country, the government awarded him with the highest civilian award.

Career and Contribution of APJ Abdul Kalam
APJ Abdul Kalam was born in Tamil Nadu. At that time the financial condition of his family was poor so from an early age he started supporting his family financially. But he never gave up education. Along with supporting his family he continued his studies and completed graduation. Above all, he was a member of the Pokhran nuclear test conducted in 1998.

There is a countless contribution of Dr.APJ Abdul Kalam to the country but he was most famous for his greatest contribution that is the development of missiles that goes by the name Agni and Prithvi."""

##cleaing the text & imports
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer 

ps = PorterStemmer()
wnl = WordNetLemmatizer()

sentences = nltk.sent_tokenize(paragraph)
corpuslist =[]

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()   ##split is get list of words
    #review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = [wnl.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpuslist.append(review)
    
#Creating bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x =cv.fit_transform(corpuslist).toarray()
