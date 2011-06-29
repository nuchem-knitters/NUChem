########################################################################################
#sortFor2D.py
#
# Description - this script is intended to take data from a series of different simulations exploring
#	parameter space and format them for GNUPlot graphing.
#	The script presumes that the pertinent values (FWHM, power, basis size, etc.) from each
#	simulation are all logged in some central file (e.g. DataLog.log).
#	The script reads in all of the lines, pulls out the values you want and into a 3D array
#	which it then sorts twice.
#
# Parameters - none, yet.
#
# Output - a file called 'graphOutput.dat' containing the data formatted for GNUPlot's 3D graphing
#
########################################################################################

from decimal import * #use the decimal class, b/c otherwise python reads in decimal numbers funny (e.g. 1.5 = 1.49999999999)
dataArray = []

inp = open ("DataLog.log",'r')  #open the file with the data

firstline=0 #used to skip the first line
for line in inp.readlines(): #step through each line
	inputLine = line.split() #split each line by whitespace
	if (firstline==1): #skip the first line
		#pull out the values you want into x, y, and z
		x = Decimal(inputLine[2]) #intensity
		y = Decimal(inputLine[5]) #tau
		z = Decimal(inputLine[19]) #alignment fwhm
		dataArray.append((x,y,z)) #add it to the array
	firstline=1	#skips the 1st line
	

	
sortedList = sorted(dataArray, key=lambda dataElement: dataElement[1]) #sort the list by y (dataElement[1])

outFile = open ("graphOutput.dat", 'w')

hOld=0 #GNUPlot needs a carriage return after each X value (e.g. X=0 Y=0-4, \n X=1 Y=0-4)

for h in  sorted(sortedList, key=lambda dataElement: dataElement[0]): #sort the list by x. Python is smart enough to keep the ordering from the earlier sort (y) when the x values are identical

	if not (hOld==0): #don't put a return at the beginning of the file
		if not (hOld==h[0]): #if the x coord has changed then we need a return
			outFile.write('\n')
	hOld=h[0] #set hOld to the new x coord
	
	print h[0],h[1],h[2] #print the values to the screen (mostly for error checking)
	outFile.write(str(h[0])+" "+str(h[1])+ " "+str(h[2]) + '\n') #write the numbers to the file - GNUPlot does NOT want tabs
	
	
outFile.close