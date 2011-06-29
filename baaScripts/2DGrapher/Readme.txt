BAA 6/29/11

This python script takes data from a log file and formats it for a GNUPlot 3D graph. Included is a sample log file (Datalog.log) as well as the syntax  I use to make the 3D graph (sortMatrixGnuplot). 

To run example: python sortFor2D.py


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
# Parameters - none, yet. Could easily be modified to take a command line argument as the input and/or output file
#
# Output - a file called 'graphOutput.dat' containing the data formatted for GNUPlot's 3D graphing
#
########################################################################################