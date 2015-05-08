import os
import nltk
import time
import pylab
import networkx
import re
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn

def getWords(text):
 words = text.split(" ")
 newlist=[]
 for word in words :
  if word in sw.words():# removal of stopwords
    words.remove(word)    
  newlist=newlist + [word.lower()]
 #stemming
 porter = nltk.PorterStemmer()
 after_stemming = [porter.stem(t) for t in words]
 #print 'Words after stemming:'
 #print after_stemming
 return newlist #not returning words after stemming
  
 

def getText(text):
 words=getWords(text)
 return words



def SimDesc(wsi,wsj):
 print wsi
 print wsj
 simdesc=0
 p=0
 syn1=object()
 syn2=object()
 x=object()
 try :
  for word1 in wsi:
   print word1
   syn1=wn.synsets(word1.strip("\\n"))
   if len(syn1) > 0: 
    syn1=syn1[0]
    for word2 in wsj:
     syn2=wn.synsets(word2.strip("\\n"))
     if len(syn2) > 0 :  
      syn2=syn2[0] 
      x=str(type(syn1.path_similarity(syn2))).split(" ")[1]
      if re.search("None",x):
       p=0
      else :
       p=syn1.path_similarity(syn2)    
      simdesc=simdesc+p
   
 except Exception,e:
  #print 'Here'
  print str(e)
 simdesc = simdesc/(len(wsi)*len(wsj) + 0.0)
 print simdesc



SimDesc("I am loved by everyone","Everyone loves me") 
