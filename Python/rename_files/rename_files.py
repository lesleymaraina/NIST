####################################################################################
# About
# Date: April 19, 2017
# Notes
'''
Code that renames a list of files in a directory
MUST Run in Python 3 environment!
'''
####################################################################################
import os
path = '/Users/lmc2/Desktop/NIST/Projects/GIAB_SampledData/Sampled_Set/rename_files/svvizPacBioAJTrio'
files = os.listdir(path)
i = 1

os.chdir('/Users/lmc2/Desktop/NIST/Projects/GIAB_SampledData/Sampled_Set/rename_files/svvizPacBioAJTrio')
for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	print (file_name)
	os.rename(os.path.join(path, f), os.path.join(path, 'svvizPacBioAJTrio_' + file_name + '.pdf'))

# for file in files:
#     os.rename(os.path.join(path, file), os.path.join(path, 'summary' + str(i) + '.tsv'))
#     i = i+1