import nltk
import os
import time
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn

def splitIntoWords(singleword):
 j=0
 for i in range(1,len(singleword)):
    
    if wn.synsets(singleword[j:i]):
       print singleword[j:i]
       j=i+1  


splitIntoWords('sayhello')
 
 

