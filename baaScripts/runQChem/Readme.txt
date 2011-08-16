BAA 8/16/11

runQChem.py

Scans files in your current directory and finds ones ending in ".in" (QChem input extension), and then makes a bash script to submit all the jobs. Is able to submit to SMP based on user input, and is smart enough not to try to submit jobs that have .out files in the same directory (wouldn't cause any harm if it did, as QChem will just refuse to run, but this is slightly faster). Currently set to use 8 processors, but could be changed easily (or made an input parameter).

Included are sample input files. To run, do:
python runQChem.py 

or, for SMP run:

python runQChem.py SMP

then ./runQChemJobs.bash to submit the jobs