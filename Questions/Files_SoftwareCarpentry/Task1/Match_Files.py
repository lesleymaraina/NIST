############################################################
# About
# Date: March 31 2017
############################################################

############################################################
# Class Code
############################################################
import glob
import pandas as pd
import os
import shutil
import fnmatch


crowdVar = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/Data2.csv')
for x in crowdVar['start']:
	print '/Users/lmc2/Desktop/PDFs/*{0}.pdf'.format(x)
matches = glob.glob('/Users/lmc2/Desktop/PDFs/*.pdf')
for match in matches:
	print match

def gen_find(filepat,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

# Example use
# Option 1: Moving files
shutil.copy('*.pdf', '/Users/lmc2/Desktop/PDFs/Two')


if __name__ == '__main__':
    src = '/Users/lmc2/Desktop/PDFs' # input
    dst = '/Users/lmc2/Desktop/PDFs/Two' # desired     location

    filesToMove = gen_find("*.pdf",src)
    for name in filesToMove:
        shutil.move(name, dst)	

# file_name = []
# for filename in glob.iglob('/Users/lmc2/Desktop/PDFs/del_*_*.pdf'):
#     print(filename)
    # store the filenames in a list?
    # compare values listed in crowdVar['start'] to the filenames listed in file_name array






# ############################################################
# # Imports
# ############################################################
# import pandas as pd
# import os


# ############################################################
# # Load Data
# ############################################################


# '''
# 1. Load in dataframe that contains the list of names we'd like to match
# 2. Ideally, find matches listed in 'start' and 'chrom' columns
# '''

# crowdVar = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/Data2.csv')

# os.chdir('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/crowdVar.lesley_svviz/PDFs')

# print (os.path.exists('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/crowdVar.lesley_svviz/PDFs'))
# #Print file names in directory
# for f in os.listdir():
# 	print(f)

# for f in os.listdir():
# 	# Split filename and file extension
# 	file_name, file_ext = os.path.splitext(f)
# 	print file_name
# 	# Split filenames based on _ 
# 	var, chrom, start = file_name.split('_')
# 	# Chrom number and Start site are stored in the following
# 	print chrom
# 	print start


# '''
# #OS Error
# Traceback (most recent call last):
#   File "Match_Files.py", line 30, in <module>
#     for f in os.listdir():
# TypeError: listdir() takes exactly 1 argument (0 given)
# '''


# '''
# Find matches between values listed in crowdVar dataframe and the file names listedin the PDFs directory

# '''

# # Values from dataframe
# crowdVar['chrom']
# crowdVar['start']



