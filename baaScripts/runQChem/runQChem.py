#!/usr/bin/python

#this script scans a directory for .in files (QChem input files) and then makes a bash script
#containing the syntax to sumbit them all to radon, either on all.q or SMP

import os, sys

path = os.getcwd() #get working directory
files = os.listdir(path) #make a list of all files in the directory

runFile=open ("runQChemJobs.bash", 'w') #preps the bash file to run the jobs
runFile.write("#!/bin/bash\n")

queue=""
if (len(sys.argv)>1): #lets you choose to submit to SMP
	if (sys.argv[1]=="SMP"):
		queue="-q SMP "
		print "Jobs formatted for SMP queue."

for a in files:
	z = os.path.splitext(a) #get the extension on each file
	if z[1]==".in": #if it's a .in file then scan it
		fileLength=len(a) #get the length of the full file we're looking at
		fileLength=fileLength-3 #get the length of the full file minus the extension (.dat)
		fileName= a[:fileLength] #get the fileName minus extensions
		
		if not (os.path.isfile(fileName+".out")): #if the outfile exits (i.e. if the job is running or finished) then we don't want it
			runFile.write("/opt/local/share/qchem/qchem.csh -l "+fileName+".out" + " -p 8 " +queue+a+"\n") #set the job for 8 processor run

