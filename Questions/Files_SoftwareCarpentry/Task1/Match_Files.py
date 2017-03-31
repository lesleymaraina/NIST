############################################################
# About
# Date: March 31 2017

############################################################



############################################################
# Imports
############################################################
import pandas as pd
import os


############################################################
# Load Data
############################################################


'''
1. Load in dataframe that contains the list of names we'd like to match
2. Ideally, find matches listed in 'start' and 'chrom' columns
'''

crowdVar = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/Data2.csv')

os.chdir('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/crowdVar.lesley_svviz/PDFs')

print (os.path.exists('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/crowdVar.lesley_svviz/PDFs'))
#Print file names in directory
for f in os.listdir():
	print(f)

for f in os.listdir():
	# Split filename and file extension
	file_name, file_ext = os.path.splitext(f)
	print file_name
	# Split filenames based on _ 
	var, chrom, start = file_name.split('_')
	# Chrom number and Start site are stored in the following
	print chrom
	print start

#OS Error
'''
Traceback (most recent call last):
  File "Match_Files.py", line 30, in <module>
    for f in os.listdir():
TypeError: listdir() takes exactly 1 argument (0 given)
'''


'''
1. Find matches between values listed in crowdVar dataframe
2. Ideally, find matches listed in 'start' and 'chrom' columns
'''

# Values from dataframe
crowdVar['chrom']
crowdVar['start']