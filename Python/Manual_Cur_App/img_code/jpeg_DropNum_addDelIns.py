####################################################################################
# About
# Date: April 12, 2018
# Notes
'''
Code that renames a list of files in a directory
MUST Run in Python 3 environment!

jpeg Drop extra number at the end of unique ID
add DEL or INS based on variant type
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
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/DEL/PBDEL'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/DEL/PBDEL')

for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	file_name = file_name.replace('_DEL', '')
	# file_name = file_name.replace(' 1', '')
	# file_name = file_name.replace(' 2', '')
	# file_name = file_name.replace(' 3', '')
	# file_name = file_name.replace(' 4', '')
	# file_name = file_name.replace(' 5', '')
	# file_name = file_name.replace(' 6', '')
	# file_name = file_name.replace(' 7', '')
	# file_name = file_name.replace(' 8', '')
	# file_name = file_name.replace(' 9', '')
	# file_name = file_name.replace(' 10', '')
	# file_name = file_name.replace(' 11', '')
	# file_name = file_name.replace(' 12', '')
	os.rename(os.path.join(path2, f), os.path.join(path2, file_name + '.jpeg'))

