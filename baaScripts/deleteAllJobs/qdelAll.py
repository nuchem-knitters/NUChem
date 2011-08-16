#!/usr/bin/python
import os, sys

#qdel's all jobs

response = raw_input("Are you sure you want to delete all jobs? (y/n):")

if (response == "y" or response == "yes"):
	getJobName="qj | grep '^[0-9]' | awk '{print $1}' > temp.tmp" #get lines that begin with numbers from the qj script
	jobName=os.system(getJobName) 
	
	numberFile= open ("temp.tmp",'r')
	
	numbers=[]
	for line in numberFile.readlines(): #step through each line
		numbers.append(line)
	
	for IDs in numbers:
		os.system("qdel "+IDs) #delete jobs
	
	numberFile.close
	
	print "All jobs scheduled for deletion."
	os.remove("temp.tmp")
else:
	print "Phew, dodged a bullet there!"