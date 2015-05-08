import os
import time
import math
import wsdl_attributes as wa 
#from cluster_visualization import splitCamelCase
from nltk.corpus import stopwords as sw
import equation2 as e2
import matplotlib.pyplot as plt

cluster_features = {}
wsdl_stopwords = ['get','post','request','result','service','port','output','in','out','input','update','delete','create','parameter','=',':']



def computeDistances(clustername):
 path = os.getcwd() +  "/Clusters"
 f=object()
 size=0
 print 'Distances for ' , clustername
 counter = 0
 distance = 0
 circle = plt.Circle((0, 0), radius=3, fc='y')
 plt.gca().add_patch(circle)
 for files in os.listdir(path):   
   counter = counter + 1
   f=open(path+"/"+files,"r")
   size=len(f.readlines())
   distance=e2.eqn2(cluster_features[files],cluster_features[clustername])
   if counter%2 == 0 :
    circle = plt.Circle((counter*10, distance*100), radius=4, fc='r')  
   else :
    circle = plt.Circle((counter, -distance*100), radius=4, fc='g')   
   plt.gca().add_patch(circle)
   #plt.annotate(files,(counter, -distance*100))
   plt.axis([-10,400,-100,100])
   plt.ylabel('Distances from ' + clustername)
   plt.xlabel("cluster number")
   plt.title("Intercluster distances")
   plt.pause(0.1)
 plt.show()
   
 



def splitCamelCase(list_of_op_names):
 
 splitter = ""
 stop_words = sw.words('english')
 new_list = []
 t=''
 for name in list_of_op_names :
    splitter = ""
    for i in range(len(name)) :
      if name[i].isdigit() == True:
        continue
      character = name[i]
      if character != name[i].upper():
         splitter = splitter +  character
      else :
         #print 'Splitter is ' , splitter
         t=splitter.strip("\"") 
         if t not in stop_words + wsdl_stopwords :
          new_list = new_list + [t]
         splitter = character.lower()
 return new_list




def initializeClusterFeatures():
 global cluster_features 
 path = os.getcwd() + "/Clusters"
 for files in os.listdir(path) :
  cluster_features[files] = []

def getFeatures():
 initializeClusterFeatures()
 path = os.getcwd() + "/Clusters"
 fl= object()
 for files in os.listdir(path) :
  fl=open(path+"/"+files,"r")
  for line in fl:
   cluster_features[files] = cluster_features[files] + splitCamelCase(wa.findOperationNames(os.getcwd()+"/wsdl dataset/" + line.strip("\n")))
  print cluster_features[files]




getFeatures()
clustername = raw_input("\nEnter the name of the cluster\n")
computeDistances(clustername) 
 
  
