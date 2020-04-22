# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:20:09 2020

@author: hp
"""

import nltk
import urllib2
import bs4 as bs
import re
import requests     
from nltk.corpus import stopwords
nltk.download('stopwords')

source = urllib2.urlopen('https://en.wikipedia.org/wiki/Machine_learning').read()

#Parsing the dataset using beutiful oup object
soup=bs.BeautifulSoup(source,'lxml' )

#fetching the data  

# Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]  
