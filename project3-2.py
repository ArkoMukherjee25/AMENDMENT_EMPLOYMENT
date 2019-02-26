#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
import numpy as np
import re

from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ne_chunk
from nltk.probability import FreqDist

import random
import glob, os

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


# In[3]:


input_directory = r"C:/Users/arkom/Desktop/document-analytics-master/employment contracts/"


# In[4]:


os.chdir(input_directory)

amend_location, employ_location = [], []

for file in os.listdir(input_directory):
    try:
        if file.endswith(".txt"):
            if bool(re.search("AMEND", file)) == True:
                amend_location.append(os.path.join(input_directory, file))
            elif bool(re.search("AMEND", file)) == False:
                employ_location.append(os.path.join(input_directory, file))
    except OSError:
        continue


# In[5]:


categories = [amend_location, employ_location]

stop_words = stopwords.words('English')

document = []
word_tokenized=[]
noun = []
wrd=[]


# In[6]:


for cat in categories:
    if cat == amend_location:
        c = 0
    else:
        c = 1
    for file in cat:
        f = open(file, "rt", encoding="utf8")
        text = f.read()
        text = re.sub(' +', ' ', text)
        text = re.sub(r'\n+', '\n', text).strip()
        f.close()
        
        sent_tokens = sent_tokenize(text)
        postags = nltk.pos_tag(word_tokenize(sent))
        for k,v in postags.items():
            if v == 'NN':
                noun.append(k)
        
        for sent in sent_tokens:
            tokens = word_tokenize(sent)
            words = [word for word in tokens if word.isalpha()]
            words = [w for w in words if not w in stop_words]
            words = [w for w in words if not w in noun]
            
            word_tokenized.append(words)
        for w in word_tokenized:
            wrd.append(w)
        document.append([wrd, c])


# In[8]:


random.shuffle(document)


# In[9]:


all_words = []
for d in document:
    words = d[0]
    for w in words:
        all_words.append(w)


# In[158]:


all_words = nltk.FreqDist(all_words)
most_frequent = all_words.most_common(10000)

word_most_frequent = [word[0] for word in most_frequent]


# In[159]:


def feature_set(list_of_words):
    features = {}
    word_list = set(list_of_words)
    for word in word_most_frequent:
        features[word] = word in word_list
    return features


# In[160]:


features = []
tuples = ()
for d in document:
    tuples = (feature_set(d[0]), d[1])
    features.append(tuples)


# In[161]:


len(features)


# In[163]:


train_set = features[:2500]
test_set = features[2500:]

my_classifier = nltk.NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.accuracy(my_classifier, test_set)


# In[164]:


print(accuracy)


# In[157]:


my_classifier.show_most_informative_features(30)


# In[ ]:


#-------------------------------------Feature Extraction-------------------------------#





for file in categories[1]:
    for file in cat:
        f = open(file, "rt", encoding="utf8")
        text = f.read()
        text = re.sub(' +', ' ', text)#extra spaces
        text = re.sub(r'\n+', '\n', text).strip()#extra newline
        f.close()
        sent_tokens = sent_tokenize(text)
        for sent in sent_tokens:
            tokens = word_tokenize(sent)
            words = [word for word in tokens if word.isalpha()]
            words = [w for w in words if not w in stop_words]
            word_tokenized.append(words)
        for w in word_tokenized:
            wrd.append(w)

for w in wrd:
    all_words.append(w)


# In[11]:


#Feature extraction

salary = re.findall(r'\$?[0-9]+\,?[0-9]+', str(all_words))

dates1 = re.findall(r'^([A-Z][a-z]{3,8})\s[0-9]{2}\,?\s[0-9]{4}', str(all_words))
dates2 = re.findall(r'[0-9]{2}\/[0-9]{2}\/[0-9]{2,4}', str(all_words))



