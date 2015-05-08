import os
import nltk
import math 
import time
import networkx as nx
import re
from networkx.readwrite import json_graph
import pylab
import wsdl_attributes as wa
from nltk.corpus import stopwords as sw

wsdl_stopwords = ['get','post','request','result','service','port','output','in','out','input','update','delete','create','parameter','=',':']


def generate_list(list_of_files):
 str1 = open("list_of_files1.txt","r").read()
 for item in list_of_files :
     str1 = str1 + "<li>" + item + "</li>\n"
 str1 = str1 + open("list_of_files2.txt","r").read()  
 fl = open("list_of_files.html","w")
 fl.write(str1)
 fl.close()
 return str1
   

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



def getRelevantTags(lst):
 path = os.getcwd() + "/wsdl dataset/"
 rel_tags = []
 for item in lst :
   rel_tags = rel_tags + splitCamelCase(wa.findOperationNames(path+item))
   print rel_tags
 fdist = nltk.FreqDist(rel_tags)
 return fdist.keys()[:20]
   

def searchTerm(query):
 fl = open("Cluster_Names.csv","r")
 x=[]
 fx=object()
 g=nx.DiGraph()
 list_of_graphs = []
 list_of_graph_node_lengths = []
 cluster_name = ''
 #query = " " + query + " "
 #cluster_names = []
 file_name = ''
 for line in fl :
  x=line.split(",")
  cluster_name = x[1]
  #cluster_names = cluster_names + [cluster_name]
  file_name = x[0]
  if cluster_name.find(query) != -1:
   fx=open(os.getcwd()+"/Clusters/"+file_name,"r")
   g=nx.DiGraph()
   g.add_node(cluster_name,size=2000)
   for ln in fx:
     g.add_node(ln.strip("\n"),size=2000)
     g.add_edge(cluster_name,ln.strip("\n"))
   list_of_graphs = list_of_graphs + [g]
   list_of_graph_node_lengths = list_of_graph_node_lengths + [len(g.nodes())]
 
 
 i=list_of_graph_node_lengths.index(max(list_of_graph_node_lengths))
 print "Here : " , list_of_graph_node_lengths[i]
 g=list_of_graphs[i]
 x=g.out_degree().values()
 i=x.index(max(x))
 nx.draw(g)
 pylab.show()
 t=json_graph.tree_data(g,root=g.out_degree().keys()[i])
 x1=g.nodes()
 x1.remove(g.out_degree().keys()[i])
 p=generate_list(x1)
 relevant_tags = getRelevantTags(x1) 
 x=str(t)
 x=re.sub("\'id\'","\'name\'",x)
 x=re.sub("\'","\"",x)
 print x
 print relevant_tags
 str1 = open("file1.txt","r").read() + str(relevant_tags) + open("file2.txt","r").read()
 print str1
 #fl=open("static/js/examples/simple.html","w")
 #fl.write(str1)
 #fl.close() 
 print str1
 print p
 #fl = open("static/js/graph.json","w")
 #fl.write(x)
 #fl.close()



query=raw_input("\nEnter your query\n")
searchTerm(query)    
