import os
import nltk
import re
import time
import math
import pylab
import wsdl_attributes as wa
import equation2 as e2

#wa.iterate()
cluster_centres  = [] 
cluster_centre_message_names = {}
cluster_centre_message_types = {} 
cluster_centre_types_used = {} 


def refine():
 global cluster_centres
 global cluster_centre_message_names 
 global cluster_centre_message_types
 global cluster_centre_types_used 
 filename = ''
 x=[]
 j=0
 scores = []
 score = 0
 mn = [] #Message names
 mt = [] #Message types
 tu = [] #types used
 bmn = [] #base Message names
 bmt = [] #base Message types
 btu = [] #base types used
 path = '/home/kaushik/Desktop/web services project/'
 command = ""
 f=object()
 for fl in os.listdir("/home/kaushik/Desktop/web services project/Clusters"):
    f=open("Clusters/"+fl,"r")
    x = f.readlines()    
    if len(x) == 1:
       command = "rm "
       #print x
       filename = x[0]
       filename = filename[0:len(filename)-1]
       mn = cluster_centre_message_names[path+"wsdl dataset/" + filename]    
       mt = cluster_centre_message_types[path+"wsdl dataset/" +filename]    
       tu = cluster_centre_types_used[path+"wsdl dataset/" +filename] 
       scores = []
       for centre in cluster_centres :
         bmn = cluster_centre_message_names[centre]    
         bmt = cluster_centre_message_types[centre]
         btu = cluster_centre_types_used[centre]
         score = 2.5*e2.eqn2(bmn,mn) + e2.eqn2(bmt,mt) + 0.5*e2.eqn2(btu,tu) 
         scores = scores + [score]       
       j = scores.index(max(scores))
       f=open("Clusters/cluster"+str(j)+".txt","a")
       f.write(filename+"\n")
       command = command +  "Clusters/" + fl
       print "Removing :" , fl
       os.system(command)


def cluster():
 global cluster_centres
 global cluster_centre_message_names 
 global cluster_centre_message_types
 global cluster_centre_types_used 
 f=object()
 filename = ''
 counter = 0
 score = 0
 i=0
 bmn = [] #base Message names
 bmt = [] #base Message types
 btu = [] #base types used
 bns = []
 mn = [] #Message names
 mt = [] #Message types
 tu = [] #types used
 ns = []
 scores = []
 path = '/home/kaushik/Desktop/web services project/wsdl dataset'
 for fl in  os.listdir('/home/kaushik/Desktop/web services project/wsdl dataset'):
   filename = path+ "/" + fl
   counter = counter + 1 
   #if re.search('str',str(type(wa.findName(filename)))):
   print counter , " : " ,  len(cluster_centres)
   if counter == 1:
       cluster_centres = cluster_centres + [filename] 
       cluster_centre_message_names[filename]=wa.findMessageNames(filename)  
       cluster_centre_message_types[filename]=wa.findMessageTypes(filename)  
       cluster_centre_types_used[filename]=wa.getTypes(filename)     
       f=open("Clusters/cluster"+str(len(cluster_centres))+".txt","a")
       f.write(fl+"\n") 
   else :
       mn = wa.findMessageNames(filename)
       mt = wa.findMessageTypes(filename)    
       tu = wa.getTypes(filename) 
       #ns = wa.breakName(wa.findName(filename))
       i=0
       scores = []
       for centre in cluster_centres :
        
         if filename in cluster_centres :
            break
         bmn = cluster_centre_message_names[centre]    
         bmt = cluster_centre_message_types[centre]
         btu = cluster_centre_types_used[centre]
         #bns = wa.breakName(wa.findName(centre))
         score = 2.5*e2.eqn2(bmn,mn) + e2.eqn2(bmt,mt) + 0.5*e2.eqn2(btu,tu) 
         #print score
         scores = scores + [score]
       if len(scores) > 0 and max(scores) > 1.1 :
         i=scores.index(max(scores))         
         f=open("Clusters/cluster"+str(i)+".txt","a")
         f.write(fl+"\n")                            
       else :            
            cluster_centres = cluster_centres + [filename] 
            cluster_centre_message_names[filename]=wa.findMessageNames(filename)  
            cluster_centre_message_types[filename]=wa.findMessageTypes(filename)  
            cluster_centre_types_used[filename]=wa.getTypes(filename)     
            f=open("Clusters/cluster"+str(len(cluster_centres))+".txt","a")
            f.write(fl+"\n")  
  
 
 print len(cluster_centres)

cluster()
refine()
