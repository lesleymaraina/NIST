####################################################################################
# About
# Date: April 10, 2018
# Notes
'''
Code that renames a list of files in a directory
MUST Run in Python 3 environment!
'''

'''
Resources
---------
https://gist.github.com/seanh/93666
https://www.youtube.com/watch?v=ve2pmm5JqmI
https://www.youtube.com/watch?v=WQVisBzJGLw
'''

####################################################################################

import os
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/genosv20a110Xunion171212rand1000INSMQ20'
# files = os.listdir(path)
i = 1

os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/genosv20a110Xunion171212rand1000INSMQ20')

for f in os.listdir(path2):

	path = os.path.join(path2, f)
	print (path)
	file_name, file_ext = os.path.splitext(f)
	file_name = file_name.replace('.SequenceDefinedVariant', '')
	unique_ID, chr_start = file_name.split('.')
	print (file_name)
	print (unique_ID)
	# new_name=
	os.rename(os.path.join(path2, f), os.path.join(path2, unique_ID + '.pdf'))

