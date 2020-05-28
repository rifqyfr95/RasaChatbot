import nltk
import numpy as np
import random
import string

import bs4 as bs
import urllib.request
import re
import heapq

import pandas as pd


datas = pd.read_csv('datacrawler.csv')
s = datas['Feature'].unique()
list_text_per_feature = []
um_text = ""
wb_text = ""
ac_text = ""
vc_text = ""
ss_text = ""
cb_text = ""
ls_text = ""

# print(datas['Feature'][3])
#
# print(datas['Desc'][5])
for a,b,c,d in zip(datas['Feature'],datas['Desc'],datas['Sub Features'],datas['Sub Desc']):
    if a == s[0]:
        um_text = um_text + " " + a + " " + b + " " + c +  " " + d
    if a == s[1]:
        ls_text = ls_text + " " + a + " " + b + " " + c +  " " + d
    if a == s[2]:
        vc_text = vc_text + " " + a + " " + b + " " + c +  " " + d
    if a == s[3]:
        ac_text = ac_text + " " + a + " " + b + " " + c +  " " + d
    if a == s[4]:
        cb_text = cb_text + " " + a + " " + b + " " + c +  " " + d
    if a == s[5]:
        ss_text = ss_text + " " + a + " " + b + " " + c +  " " + d
    if a == s[6]:
        wb_text = wb_text + " " + a + " " + b + " " + c +  " " + d


#
list_text_per_feature.append(um_text)
list_text_per_feature.append(ac_text)
list_text_per_feature.append(vc_text)
list_text_per_feature.append(wb_text)
list_text_per_feature.append(ss_text)
list_text_per_feature.append(ls_text)
list_text_per_feature.append(cb_text)
#
#
#
list_corpus = []
for a in list_text_per_feature:
    corpus = nltk.sent_tokenize(a)
    for i in range(len(corpus)):
        corpus[i] = corpus[i].lower()
        corpus[i] = re.sub(r'\W', ' ', corpus[i])
        corpus[i] = re.sub(r'\s+', ' ', corpus[i])
    list_corpus.append(corpus)

wordfreq = {}
for corpus in list_corpus:
    for sentence in corpus:
        tokens = nltk.word_tokenize(sentence)
        for token in tokens:
            if token not in wordfreq.keys():
                wordfreq[token] = 1
            else:
                wordfreq[token] += 1
# print(wordfreq)


most_freq = heapq.nlargest(200, wordfreq, key=wordfreq.get)
# print(most_freq)

sentence_vectors = []

for corpus in list_corpus:
    for sentence in corpus:
        sentence_tokens = nltk.word_tokenize(sentence)
        sent_vec = []
        for token in most_freq:
            if token in sentence_tokens:
                sent_vec.append(1)
            else:
                sent_vec.append(0)
        sentence_vectors.append(sent_vec)

sentence_vectors = np.asarray(sentence_vectors)


print(sentence_vectors)