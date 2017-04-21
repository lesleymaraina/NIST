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
path = '/Volumes/lesleydata/FinalProject/Data/Data2/svvizPacBioAJTrio/TSV2'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'summary' + str(i) + '.tsv'))
    i = i+1