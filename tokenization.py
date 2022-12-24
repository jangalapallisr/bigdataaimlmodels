#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
##nltk.download()

paragraph = """Dr. APJ Abdul Kalam is a famous name in the whole world. He is counted among the greatest scientists of the 21st century. Even more, he becomes the 11th president of India and served his country. He was the most valued person of the country as his contribution as a scientist and as a president is beyond compare. Apart from that, his contribution to the ISRO (Indian Space Research Organization) is remarkable. He headed many projects that contributed to the society also he was the one who helped in the development of Agni and Prithvi missiles. For his involvement in the Nuclear power in India, he was known as “Missile Man of India”. And due to his contribution to the country, the government awarded him with the highest civilian award.

Career and Contribution of APJ Abdul Kalam
APJ Abdul Kalam was born in Tamil Nadu. At that time the financial condition of his family was poor so from an early age he started supporting his family financially. But he never gave up education. Along with supporting his family he continued his studies and completed graduation. Above all, he was a member of the Pokhran nuclear test conducted in 1998.

There is a countless contribution of Dr.APJ Abdul Kalam to the country but he was most famous for his greatest contribution that is the development of missiles that goes by the name Agni and Prithvi."""

##Eaither we can use tokennization at sentence level or word level
##Tokenizing Sentences
sentences_us=nltk.sent_tokenize(paragraph)
sentences_fr=nltk.sent_tokenize(paragraph,language='french')
sentences_gr=nltk.sent_tokenize(paragraph,language='german')

##Tokeninzing Words
words_us = nltk.word_tokenize(paragraph,language='english',preserve_line=False)

word_len = len(words_us)
sum=0
for w in words_us:
    sum +=len(w)

print(sum)
print(sum/word_len)
## FAlse 257
## True 245
##import socket
import ipaddress
addr ="10.345.67.98"
try:
    ip = ipaddress.ip_address("10.345.67.98")
    print("Valid IP address:" %(ip, ip.version))
except:
    print("Invalid Ip Address")

## STEMMING AND LEMMATIZATION
#STEMMING: Process of Reducing infected words to their word STEM
#Ex: history & historicel ==>histori;  finally,final, & finalized ==>fina; going, goes, &gone ==>go

#LEMMATIZATION: it forms into meaningful word.
#Ex: history & historicel ==>history;  finally,final, & finalized ==>final; going, goes, &gone ==>go
