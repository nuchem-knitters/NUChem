########################################################################################
#fwhmALL.py
#
# Description - this script is intended to find the FWHM of a curve from a data file.
#	More specifically for me (BAA), this finds the FWHM of the alignment of a molecule
#	in response to a laser pulse. It also finds the difference in between the death of the
#	laser pulse and: the left Half-Max of the alignment curve, the peak of the alignment curve
#
#
# Parameters - input data file name - this script expects that the 
#	- output data file name - the file where you want the numbers placed.
#
# Output - writes the 3 numbers (FWHM, delta from death to left HM, delta from death to peak)
#	into a file specified by the user. In my case (BAA) it's done without much formatting/ceremony,
#	b/c it writes to a temp file used by runRings.plx that then takes those numbers and formats them
#	nicely in DataLog.log
#
########################################################################################


import sys,re

###open file###
import sys
inp = open (sys.argv[1],'r') #open the file specified by the user
expectation = [] #declare arrays
pulseStrength = []
#read lines into array 
for line in inp.readlines(): #step through each line
	inputLine = line.split() #split each line by whitespace
	expectation.append(float(inputLine[1])) #get the alignment expectation value
	pulseStrength.append(float(inputLine[4])) #get the laser pulse strength

###look for peak of alignment###
maxAlign = expectation[0] #initialize values
maxAlignTime=0
for i, value in enumerate(expectation): #step through the expectation values
	if value > maxAlign: #if this is bigger than the last one
		maxAlign=value #set max alignment
		maxAlignTime=i+1 #set the time max alignment occurred
maxAlignTime=maxAlignTime/100. #the enumerate fxn gives the times in integers, while my timestep is in 100ths of integers (my timesteps are 10 fs, and I want answers in ps), so I divide by 100		


###look for peak of the pulse###
maxPulse=0
maxPulseTime=0
for i, value in enumerate(pulseStrength): #find max
	if value > maxPulse:
		maxPulse=value
		maxPulseTime=i+1
		

###look for death of the pulse###
pulseDeathTime=0
for i, value in enumerate(pulseStrength): 
	if i > maxPulseTime: #make sure we're on the down slope
		if pulseDeathTime == 0: #make sure we only do this next step once
			if value < 10: #arbitrarily calling less than 10% "death"
				pulseDeathTime=i+1 

###convert times to ps for comparison###
maxPulseTime=maxPulseTime/100.
pulseDeathTime=pulseDeathTime/100.


###find left & right bounds###
#we have found the peak alignment, now find the FWHM of the peak#
halfMax=(maxAlign+expectation[0])/2.
leftHM, rightHM=0, 0
for i, value in enumerate(expectation):
	if leftHM==0: #we're still looking for the left bound
		if value > halfMax: #we've passed halfMax, so whatever we just passed must be it!
			leftHM=i/100. #this is the left bound
	elif rightHM==0: #we've found the left, let's look for the right, but make sure that once we find it we don't do it again (sometimes later in the simulation the pulse comes back up to FWHM levels	
		if value < halfMax: #we've passed halfMax going the other way, so we found it
			rightHM=i/100.

###find delta T's###
FWHM=rightHM-leftHM
deltaLeftPulseTime=leftHM-pulseDeathTime
deltaPulseTime=maxAlignTime-pulseDeathTime

outFile = open (sys.argv[2], 'a')
outFile.write(str(FWHM) + '\n')
outFile.write(str(deltaLeftPulseTime) + '\n')
outFile.write(str(deltaPulseTime) + '\n')
outFile.close


print  "FWHM of Alignment:",FWHM, "   LeftDelta:", deltaLeftPulseTime, "   Delta:", deltaPulseTime



