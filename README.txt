Dependecies required to be installed for the module to run :

  1) Python( version 2.7.6 or above)
       Packages requires to be installed in python :
          a) numpy
          b) matplotlib
          c) networkx
          d) Flask
          e) nltk
          
  2) Web dependencies that are used are :
        a) d3 - collapsible  force layout
        b) amcharts

 To install the above mentioned python packages, a wise choice would be to install anaconda in the working
 environment, which entails the presence of all the mentioned python packages. In the absence of anaconda, the
 python packages can be installed using pip install or easy_install on the terminal with superuser permission

 The book for nltk can be downloaded and installed from the python terrminal using the command nltk.download()
 and chssing the book corpus in the graphical user interface that apperas after the execution of the above mentioned
 command
		
 The procedure for running the software is :
 
 1) The wsdl files that are required to be clustered are placed in wsdl dataset folder, and
    a an empty folder called Clusters is to be created in thee same folder as expt.py, if already existnig then
    it is to be emptied
 2) The file expt.py is run on the terminal which will generate the clusters in the Clusters folder
 3) The file cluster_naming to py is to be run on the terminal which will name all the clusters, the names stored
    in a file called Cluster_Names.csv 
 4) If cluster sizes are required to be found out a file called cluster_sizes.py is to be run on the terminal which 
    will also show the output on the terminal
 5) To compute and visulaize as to how far the clusters are a file named the file called cluster_distances.py is to  
    be run which will display a python graph on the terminal about the cluster distances


  
 
