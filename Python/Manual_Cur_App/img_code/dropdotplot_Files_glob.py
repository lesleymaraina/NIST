####################################################################################
# About
# Date: April 10, 2018
# Notes
'''
Remove all files that do not contain dotplots
Delete specific files from a directory
'''

'''
Resources
---------
https://www.youtube.com/watch?v=JJaNqB43Mrs
'''

####################################################################################

import glob
import os
directory = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/Dotplots/DEL/All'
os.chdir(directory)
# files=glob.glob('*.zoomed4000.pdf')
files=glob.glob('*2.jpeg')
for filename in files:
	os.unlink(filename)