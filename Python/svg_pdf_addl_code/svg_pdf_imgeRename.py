####################################################################################
# About
# Date: May 31, 2018

####################################################################################

import os
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/INS/10XINS_HapSep/svg_files_forPDFconversion'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/INS/10XINS_HapSep/svg_files_forPDFconversion')

for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	file_name = file_name.replace('.svg,pdf', '')
	file_name = file_name.replace('.svg', '')
	# unique_ID, dotplot = file_name.split('.')
	# print(unique_ID)
	os.rename(os.path.join(path2, f), os.path.join(path2, file_name + '.pdf'))