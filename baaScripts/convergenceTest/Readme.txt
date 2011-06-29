BAA 6/29/11

This script compares various files looking to see when they converge with some reference file. See the comments in the script for details. Example data files are included ("dcbSearchbasisXX.dat").

To run example: python convergenceTest.py dcbSearchBasis


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
