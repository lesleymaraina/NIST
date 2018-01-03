########################################
# Date : January 3 2017
'''
Description
-----------
- 10X tsv files have different names than original tsv files b/c BAM files from OAK directory were used.
- Need to switch back to old file names in order for R script to run
- Run code in python 3.6 env - virtualenv py2


Resources
---------
https://www.youtube.com/watch?v=0PlSnr0Tj4o
Pauls Problem
https://www.youtube.com/watch?v=mKk16T6IExU
'''
########################################

import os 
import codecs

texttofind = 'HG002_10X_86x_'
texttoreplace = 'NA24385_GRCh37_'
sourcepath = os.listdir('InputFiles/')
for file in sourcepath:
	inputfile = 'InputFiles/' + file
	print('Conversion is ongoing for:' +inputfile)
	with codecs.open(inputfile, 'r',encoding='utf-8', errors='ignore') as inputfile:
	# with open(inputfile, 'r') as inputfile:
		filedata = inputfile.read()
		freq = 0
		freq = filedata.count(texttofind)
	destinationpath = 'OutputFiles/' + file
	filedata = filedata.replace(texttofind, texttoreplace)
	with open(destinationpath, 'w') as file:
		file.write(filedata)
	print ('Total %d Records Replaced' %freq)
files_in_dir = os.listdir('./')
print (files_in_dir)
files_in_dir.remove('.DS_Store')

texttofind = 'HG003_10X_36x_'
texttoreplace = 'NA24149_GRCh37_'
sourcepath = os.listdir('OutputFiles/')
for file in sourcepath:
	inputfile = 'OutputFiles/' + file
	print('Conversion is ongoing for:' +inputfile)
	with codecs.open(inputfile, 'r',encoding='utf-8', errors='ignore') as inputfile:
	# with open(inputfile, 'r') as inputfile:
		filedata = inputfile.read()
		freq = 0
		freq = filedata.count(texttofind)
	destinationpath = 'OutputFile2/' + file
	filedata = filedata.replace(texttofind, texttoreplace)
	with open(destinationpath, 'w') as file:
		file.write(filedata)
	print ('Total %d Records Replaced' %freq)


texttofind = 'HG004_PB_30x_RG_HP10XPASS_'
texttoreplace = 'NA24143_GRCh37_'
sourcepath = os.listdir('OutputFile2/')
for file in sourcepath:
	inputfile = 'OutputFile2/' + file
	print('Conversion is ongoing for:' +inputfile)
	with codecs.open(inputfile, 'r',encoding='utf-8', errors='ignore') as inputfile:
	# with open(inputfile, 'r') as inputfile:
		filedata = inputfile.read()
		freq = 0
		freq = filedata.count(texttofind)
	destinationpath = 'OutputFileFinal/' + file
	filedata = filedata.replace(texttofind, texttoreplace)
	with open(destinationpath, 'w') as file:
		file.write(filedata)
	print ('Total %d Records Replaced' %freq)