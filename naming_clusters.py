import os
import nltk
import time
import math
import pylab
import wsdl_attributes as wa
import equation2 as e2
import networkx as nx


cluster_features = {} # a dictionary data structure to maintain the features of the clusters

def returnName(list_of_name_words): # returns the name of a cluster based on the frequncy of the words found in the names of all services in the cluster
 fdist = nltk.FreqDist(list_of_name_words)
 return fdist

def nameClusters(): # performs the clustering of services based on the files present in the Clusters folder
 global cluster_features
 g=nx.Graph() 
 g.add_node("Entire Dataset")
 filenames = []
 f=object() 
 if "ClusterNames.csv" in os.listdir('.') :
   os.system("rm ClusterNames.csv")
 clusternames=open("ClusterNames.csv","a")
 fdist=object()
 list_of_name_words = []
 name = ''
 path = '/home/kaushik/Desktop/web services project/wsdl dataset/'
 for fl in os.listdir('/home/kaushik/Desktop/web services project/Clusters') :
   f=open("Clusters/"+fl,"r")
   filenames =  f.readlines()
   list_of_name_words = []
   name = ''
   for fls in filenames :
     list_of_name_words = list_of_name_words + wa.breakName(wa.findName(path+fls[0:len(fls)-1]))
   fdist=returnName(list_of_name_words)
   cluster_features[fl] = fdist.keys()
   print fdist.keys()[:3]
   for item in fdist.keys()[:3]:
     name = name + " " +  item
   clusternames.write(fl+","+name+"\n")
   g.add_node(name)
   g.add_edge("Entire Dataset",name)
 nx.draw(g)
 pylab.show() 


def findIntersectingEntities(list1,list2):
 new_list = list1 + list2
 fdist = nltk.FreqDist(new_list)
 return fdist[:3]
 


def hierarchical_clustering(): # does hierarchical clustering
 g=nx.Graph() 
 g1=nx.Graph()
 g.add_node("Entire Dataset")
 if "Hierarchies.csv" in os.listdir('.') :
   os.system("rm Hierarchies.csv")
 hierarchies = open("Hierarchies.csv","a")
 list_of_clusters = os.listdir('/home/kaushik/Desktop/web services project/Clusters')   
 similar_clusters = []
 name = ''
 all_clusters = ''
 fdist = object()
 no_of_hier = 0
 for x in list_of_clusters:
   similar_clusters = []
   similar_clusters = similar_clusters + [x]
   list_of_clusters.remove(x)
   name = ''
   all_clusters = '' 
   if len(list_of_clusters)!=0: 
    for y in list_of_clusters :
      if e2.eqn2(cluster_features[x],cluster_features[y]) > 0.3:
          similar_clusters = similar_clusters + [y]
          list_of_clusters.remove(y)
    no_of_hier = no_of_hier + 1
   g.add_nodes_from(similar_clusters) 
   g.add_node(no_of_hier)
   
   for node in similar_clusters :
    g.add_edge(no_of_hier,node)
    all_clusters = all_clusters + node + " "
   hierarchies.write(str(no_of_hier)+","+ all_clusters + "\n")
   g.add_edge(no_of_hier,"Entire Dataset")  
   #list_of_clusters.remove(x)     
   
   print similar_clusters
 nx.draw(g)
 pylab.show()
        
   

try :
 nameClusters()
 hierarchical_clustering()
except Exception,e:
 print str(e) 
