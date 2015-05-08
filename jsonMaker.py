import os
import time
import nltk
import math
import pylab

cluster_names = {}

def readClusterNames():
 global cluster_names
 fl = open("ClusterNames.csv","r")
 fields = []
 for line in fl :
  fields = line.split(",")
  cluster_names[fields[0]] = fields[1][0:len(fields[1])-1]



def makeJson():
 fl = open("Hierarchies.csv","r")
 fields = [] 
 x = []
 json_string = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
 for line in fl :
  fields =  line.split(",")
  x=fields[1].split(" ")[0:-1]
  json_string = json_string + "{\n\"name\": " + "\"" + fields[0] + "\",\n"
  json_string = json_string + "\"children\": [\n"
  for cluster in x :
    if x.index(cluster) != (len(x)-1) :
     json_string = json_string + "{\"name\": " + "\""+cluster_names[cluster] +"\" , " + "\"size\": " + " 3000 },\n" 
    else :
     json_string = json_string + "{\"name\": " + "\""+cluster_names[cluster] +"\" , " + "\"size\": " + " 3000 }\n]\n},\n"
 json_string = json_string[0:-2] + "\n]\n}\n" 
 print json_string
 fl = open("newjson.json","w")
 fl.write(json_string)
 fl.close()

readClusterNames()
print cluster_names
makeJson()

 
