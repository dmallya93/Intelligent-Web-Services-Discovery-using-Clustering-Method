import os
import nltk
import re
import time
import math
import process_wsdl as pw

def seeFiles():
 f=object()
 path = '/home/kaushik/Desktop/web services project/wsdl dataset'
 for fl in  os.listdir('/home/kaushik/Desktop/web services project/wsdl dataset'):
   filename = path+ "/" + fl
   pw.getDetails(filename)



seeFiles() 
