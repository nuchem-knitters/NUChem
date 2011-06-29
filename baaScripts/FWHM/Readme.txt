BAA 6/29/11

This python script calculates FWHM from a text file of data. Included are two sample data files ("RegularBiphenylPower50.dat") ("heavyBiphenylPower50.dat").

To run example: python fwhmALL.py RegularBiphenylPower50.dat test

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
