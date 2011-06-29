########################################################################################
#convergenceTest.py
#
# Description - Let's say you're running a series of simulations, trying to find the smallest basis size
# that gives you the correct answer. This script scans a directory for files with a certain prefix you give it
# (e.g. restRunBasisSize), and then looks at the characters (presumably numbers) between the end of the
# prefix and the file extension. It then finds the one with the biggest number (which is presumably the most accurate,
# though you could easily modify the script to make the lowest number the best) and proceeds to subtract each file
# from this master file, and sums up the square of the difference for each point (in time, in my case). It then
# lists all of the simulations that satisfy my convergence criteria ( <0.001, but you can change it ). 
#
# Parameters - input data file prefix - the code assumes that all of the simulations have the same name
#	except for some suffix, which is the parameter in question (e.g. restRunBasisSizeXXX.dat)
#
# Output - prints the files that converge, along with their squared residues, to STDOUT
#
########################################################################################


#!/usr/bin/python
import sys,re, os

baseName = sys.argv[1] #the name of the simulation, minus the unique part, e.g. dcbBasis for dcbBasis(50-100)
nameLength=len(baseName) #get the length of the name

path = os.getcwd() #get working directory
files = os.listdir(path) #make a list of all files in the directory
maxValue=0 #initialize
suffixList = [] #build a list of suffixes for later
for a in files:
	z = os.path.splitext(a) #get the extension on each file
	if z[1]==".dat": #if it's a .dat file then scan it
		if (a[:nameLength]==baseName):
			fileLength=len(a) #get the length of the full file we're looking at
			fileLength=fileLength-4 #get the length of the full file minus the extension (.dat)
			variable= a[nameLength:fileLength] #this finds whatever comes between the end of the base name and the extension (i.e. the variable)
			suffixList.append(int(variable))
			if int(variable) > maxValue:
				maxValue = int(variable)
			
print "Max Value:", maxValue			

maxName= baseName+str(maxValue)+".dat" #reconstruct the file name of the file with the maximum parameter			
maxFile = open (maxName,'r') 

maxFileValue = [] #read the maxFile values into an array
for line in maxFile.readlines(): #step through each line
	inputLine = line.split() #split each line by whitespace
	maxFileValue.append(float(inputLine[1]))
maxFile.close

#okay, now that we have the benchmark to compare to, let's start loading the files
suffixList.sort() #sort the list 
residues = [] #make an array of residues
for i in suffixList:
	if not (i==int(maxValue)): #make sure we don't read in the benchmark again
		compareFileName=baseName+str(i)+".dat"
		compareFile= open (compareFileName,'r')
		residueSum = 0
		for n,line in enumerate(compareFile.readlines()): #step through each line
			inputLine = line.split() #split each line by whitespace
			residueSum = residueSum + pow(float(inputLine[1])-maxFileValue[n],2)
		residues.append((i, residueSum))	
	
for i in residues:
	print i
	if i[1] < .001:
		print "Converges at:",i[0]
		
	
#del a[:]
