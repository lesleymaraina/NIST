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
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/genosv20a1ILLMPbpunion171212rand1000INSMQ20'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/genosv20a1ILLMPbpunion171212rand1000INSMQ20')

for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	print(file_name)
	# file_name = file_name.replace('Variant.', 'Variant.del_')
	# file_name = file_name.replace('.SequenceDefinedVariant', '')
	# unique_ID, number = file_name.split('.')
	# print (unique_ID)
	# file_name = file_name.replace(' ', '-')
	# unique_ID, chr_start, dotplot_end = file_name.split('.')
	# dp, number = dotplot_end.split('-')
	# new_name = '{}{}{}'.format(unique_ID, number, file_ext)
	# os.rename(f, new_name)
	# os.path.join(path2, unique_ID + number + '.jpeg')
	# os.rename(os.path.join(path2, f), os.path.join(path2, unique_ID + '_INS' + '.pdf'))
	# os.rename(os.path.join(path2, f), os.path.join(path2, file_name + '.pdf'))
