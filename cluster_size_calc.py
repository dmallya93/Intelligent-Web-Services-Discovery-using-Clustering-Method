import os
import nltk
import time
import math

def compare(value,upper_limit,lower_limit):
  if value >= lower_limit and value <upper_limit :
     return 1
  else :
    return 0


def countClusterSizes():
 path = os.getcwd() + "/Clusters/"
 f=object()
 cluster_size=0
 lower_limit=0
 upper_limit=0 
 cluster_sizes = []
 j=0
 lst = {}
 fdist = object()
    
 i=0
 for cluster in os.listdir(path):
  print i 
  i=i+1
  f=open(path+cluster,"r")
  limit = 0
  cluster_size=len(f.readlines())
  cluster_sizes =  cluster_sizes + [cluster_size]     
  
 fdist = nltk.FreqDist(cluster_sizes)
 lst["0-50"] = 0
 lst["50-100"] = 0
 lst["100-150"] = 0
 lst["150-200"] = 0
 lst["200-250"] = 0
 lst["250-300"] = 0
 lst["Above 300"] = 0
 for i in range(len(fdist.keys())):
   if fdist.keys()[i] < 50 :
     lst["0-50"] = lst["0-50"] + fdist.values()[i]
   elif fdist.keys()[i] >= 50 and fdist.keys()[i] < 100 :
     lst["50-100"] = lst["50-100"] + fdist.values()[i]
   elif fdist.keys()[i] >= 100 and fdist.keys()[i] < 150 :
     lst["100-150"] = lst["100-150"] + fdist.values()[i]
   elif fdist.keys()[i] >= 150 and fdist.keys()[i] < 200 :
     lst["150-200"] = lst["150-200"] + fdist.values()[i]
   elif fdist.keys()[i] >= 200 and fdist.keys()[i] < 250 :
     lst["200-250"] = lst["200-250"] + fdist.values()[i]
   elif fdist.keys()[i] >= 250 and fdist.keys()[i] < 300 :
     lst["250-300"] = lst["250-300"] + fdist.values()[i]
   else :
     lst["Above 300"] = lst["Above 300"] + fdist.values()[i]

 print lst
  
   


countClusterSizes() 
