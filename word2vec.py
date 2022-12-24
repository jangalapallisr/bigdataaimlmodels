#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## BOW & TFIDF are not stored the semantic information, 
## order of the word in sentence is very important in predictive ML world, the order of word actually indicates relationship of 2/3 words
## And it gives importance to uncommon words
## There is chance of OF(Over Fitting) by BOW & TFIDF
##### so to overcome all these problems word2vec, that's why we have w2v

## in BOW, or in TFIDF each word is representing 1/0 or 0.4/0.8 (between 0 &1) - log values
##**** where as in W2V, each word representing as a vector of 32 or more dimension instead of a single number
##*** Semantic information & relation between different words is also preserved

##Steps to create W2V  --- and W2V is for special designed huge amount of text processing (whole wiki pages can able to process)
#1.Tokenization of Senetences
#2.Create Histograms
#3.Take most frequent words
#4.Create a matrix with all the unique words. It also represent the occurance relation between the words

import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re

paragraph = """Dr. APJ Abdul Kalam is a famous name in the whole world. He is counted among the greatest scientists of the 21st century. Even more, he becomes the 11th president of India and served his country. He was the most valued person of the country as his contribution as a scientist and as a president is beyond compare. Apart from that, his contribution to the ISRO (Indian Space Research Organization) is remarkable. He headed many projects that contributed to the society also he was the one who helped in the development of Agni and Prithvi missiles. For his involvement in the Nuclear power in India, he was known as “Missile Man of India”. And due to his contribution to the country, the government awarded him with the highest civilian award.

Career and Contribution of APJ Abdul Kalam
APJ Abdul Kalam was born in Tamil Nadu. At that time the financial condition of his family was poor so from an early age he started supporting his family financially. But he never gave up education. Along with supporting his family he continued his studies and completed graduation. Above all, he was a member of the Pokhran nuclear test conducted in 1998.

There is a countless contribution of Dr.APJ Abdul Kalam to the country but he was most famous for his greatest contribution that is the development of missiles that goes by the name Agni and Prithvi."""

## Data preprocessing
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+', ' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+', ' ',text)

sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in set(stopwords.words('english')) ]

##Training the Word2Vec Model
model = Word2Vec(sentences,min_count=1)

words = model.wv.vocab

#Finding the particular word vector
vector = model.wv['due']
#Find most simlar words
similar = model.wv.most_similar('also')