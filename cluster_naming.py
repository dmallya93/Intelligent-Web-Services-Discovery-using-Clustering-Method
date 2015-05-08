import os
import nltk
import time
import math
import wsdl_attributes as wa
import equation2 as e2
import networkx as nx
import pylab
import re
from networkx.readwrite import json_graph

wsdl_stopwords = ['get','post','request','result','service','port','output','in','out','input','update','delete','create','parameter','=',':','search']


cluster_names={}
cluster_features = {}
node_sizes = {}

def hierarchical_clustering(): # does hierarchical clustering
 g=nx.DiGraph() 
 list_of_nodes = os.listdir(os.getcwd() + "/Clusters")
 no_of_hier_nodes = 0
 score = 0 
 g.add_node("Entire Dataset",size=2000)
 for items in list_of_nodes :
   
   g.add_node(str(no_of_hier_nodes),size=2000)
   g.add_edge("Entire Dataset",str(no_of_hier_nodes))
   node_sizes["Entire Dataset"] = 2000
   if items not in g.nodes() :
       g.add_node(cluster_names[items],size=2000)  
       node_sizes[cluster_names[items]] = 2000
       g.add_edge(str(no_of_hier_nodes),cluster_names[items])
       
   for node in list_of_nodes :
      if node != items and node not in g.nodes():
         score = e2.eqn2(cluster_features[items],cluster_features[node])
         if score > 0.3 :
            g.add_node(cluster_names[node],size=2000) 
            node_sizes[cluster_names[node]] = 2000
            g.add_edge(str(no_of_hier_nodes),cluster_names[node])
            list_of_nodes.remove(node)
       
   list_of_nodes.remove(items)
   no_of_hier_nodes = no_of_hier_nodes + 1
 T=nx.bfs_tree(g,source="Entire Dataset")
 nx.draw(g)

 pylab.show()
 g=T
 nx.set_node_attributes(g,"size",node_sizes)
 t=json_graph.tree_data(T,root="Entire Dataset")
 x=str(t)
 x=re.sub("\'id\'","\'name\'",x)
 x=re.sub("\'","\"",x)
 #x=re.sub("\'","\"",x)
 #x=re.sub("\"name\"[\:] \"(.)*\"","\"name\"[:] \"(.)*\" \"size\": 2000",x)
 fl = open("graph.json","w")
 fl.write(x)
 fl.close()
 print x
 
  


def splitCamelCase(list_of_op_names):
 
 splitter = ""
 new_list = []
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
         splitter=splitter.replace('\'','')
         splitter=splitter.replace("\"","")
         new_list = new_list + [splitter]
         splitter = character.lower()
 return new_list

  

def nameClusters():
 path =  os.getcwd()
 wsdlfilename = ''
 clusterOpNames = []
 fdist = object()
 f=object()
 fx=open("Cluster_Names.csv","w")
 counter =  0
 x=0
 t=0
 p=[]
 name = ''
 for files in os.listdir(path+"/Clusters") :
    
    fl = open(path + "/Clusters/" +   files,"r")
    f=open(path + "/Clusters/" +   files,"r")
    x=len(f.readlines())
    
    #print "No of files : ", x
    t=0
    for line in fl :
      #print "Adding :", t
      t=t+1
      if t > 2000 :
        break
      wsdlfilename =  path + "/wsdl dataset/" + line[0:len(line)-1] 
      clusterOpNames = clusterOpNames + wa.findOperationNames(wsdlfilename)
    fdist = nltk.FreqDist(splitCamelCase(clusterOpNames))
    p=fdist.keys()
    for items in wsdl_stopwords:
       for it in p :
          if re.search(items,it):
            p.remove(it)
    if 'get' in p :
     p.remove('get')
    if 'parameter' in p:
     p.remove('parameter')
    if '' in p :
     p.remove('')
    if '\"' in p :
     p.remove('\"')
    name = ''
    for items in p[:4]:
      name = name + items + " "
    fx.write(files+","+name+"\n")
    cluster_names[files] = name
    cluster_features[files] = p
    print  "Cluster - " , str(counter) , " : " , p[:4]
    counter = counter + 1
    clusterOpNames = []
    

nameClusters()
hierarchical_clustering()      
 
