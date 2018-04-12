####################################################################################
# About
# Date: April 12, 2018
# Notes
'''
Code that renames a list of files in a directory
MUST Run in Python 3 environment!

Use os to list names of files --> store names in a list --> put in a pandas file
Print List of names that are the same in multiple files
'''

'''
Resources
---------
Pandas: strip character and number - https://stackoverflow.com/questions/13682044/pandas-dataframe-remove-unwanted-parts-from-strings-in-a-column
rstrip: strip everything to the right - https://www.youtube.com/watch?v=S1rO8ikU7YM
'''

####################################################################################

'''
1- MP
'''
import os
import pandas as pd
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/IllMPDEL'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/IllMPDEL')

lst_folders = []
for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	lst_folders.append(file_name)

files_MP = pd.DataFrame()
files_MP['A'] = lst_folders
# files_MP['MP'] = files_MP['MP'].map(lambda x: x.rstrip('123456789').lstrip(' '))


'''
2- 300x
'''
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/Ill300DEL'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/Ill300DEL')

lst_folders = []
for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	lst_folders.append(file_name)

files_300x = pd.DataFrame()
files_300x['A'] = lst_folders
files_300x['A'] = files_300x['A'].map(lambda x: x.rstrip('123456789').lstrip(' '))


'''
3- 250bp
'''
path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/Ill250DEL'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/Ill250DEL')

lst_folders = []
for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	lst_folders.append(file_name)

files_250bp = pd.DataFrame()
files_250bp['A'] = lst_folders
files_250bp['A'] = files_250bp['A'].map(lambda x: x.rstrip('123456789').lstrip(' '))


'''
4 - 10X
'''

path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/10XDEL'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/10XDEL')

lst_folders = []
for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	lst_folders.append(file_name)

files_10X = pd.DataFrame()
files_10X['A'] = lst_folders
# files_10X['10X'] = files_10X['10X'].map(lambda x: x.rstrip('123456789').lstrip(' '))


'''
5 - PB
'''

path2 = '/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/PBDEL'
os.chdir('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/PBDEL')

lst_folders = []
for f in os.listdir():
	file_name, file_ext = os.path.splitext(f)
	lst_folders.append(file_name)

files_PB = pd.DataFrame()
files_PB['A'] = lst_folders
# files_PB['PB'] = files_PB['PB'].map(lambda x: x.rstrip('123456789').lstrip(' '))

compare1 = pd.DataFrame()
compare1 = pd.merge(files_250bp, files_10X, on=['A'], how='left')
compare1 = compare1.drop_duplicates()
compare2 = pd.merge(compare1, files_PB, on=['A'], how='left')
compare2 = compare2.drop_duplicates()
compare3 = pd.merge(compare2, files_300x, on=['A'], how='left')
compare3 = compare3.drop_duplicates()
compare4 = pd.merge(compare3, files_MP, on=['A'], how='left')
compare4 = compare4.drop_duplicates()
compare5 = pd.merge(compare1, compare4, on=['A'], how='left')
compare5 = compare5.drop_duplicates()
print(compare4)

# all_files = pd.concat([files_PB, files_MP, files_10X, files_300x, files_250bp], axis=1)
compare4.to_csv('/Volumes/lesleydata/manual_Curation_app/images/svviz_JMZook/1000_Rand_Samp_INS_DEL_2/app_images/compare4.csv', index=False)


