############################################################
# About
# Date: March 31 2017

'''
Add High Confidence crowdVar Labels and percent certainty to original dataframe
'''
############################################################

############################################################
# Imports
############################################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as p
import sklearn as sol

############################################################
# Load Data
############################################################

# all_data_DEL = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.DEL.csv")
all_data_DEL = pd.read_csv("/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar.csv")
# print all_data_DEL.head(3)
# print all_data_INS.head(3)

'''
Store Data in Dataframes
'''

# new_df_DEL = pd.concat([DEL_250bp, DEL_10x, DEL_300x,DEL_MP,DEL_PacBio], axis=0)
# new_df_DEL['Counts'] = new_df_DEL.groupby(['start'])['end'].transform('count')
# new_df_DEL['Count_2'] = new_df_DEL.groupby(['id'])['start'].transform('count')
# new_df_DEL['AllRefCount'] = np.where((new_df_DEL['HG002'] == 0) & (new_df_DEL['HG003'] == 0) & (new_df_DEL['HG004'] == 0), '0', '')
# new_df_DEL.to_csv('mend_Del.csv', index=False)
mend_DEL = pd.read_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar_HiConf_labeled.csv')
print mend_DEL.head(3)
# print all_data_DEL.head(3)


'''
Find matches between 2 dataframes and create a new column with corresponding label
'''

all_data_DEL['Label'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = all_data_DEL.loc[i, 'end']
	end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'Label'] = np.median(mend_DEL.loc[index, 'label2'])
	# print(all_data_DEL.loc[i])


all_data_DEL['CN0_prob'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = all_data_DEL.loc[i, 'end']
	end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'CN0_prob'] = np.median(mend_DEL.loc[index, 'CN0_prob'])


all_data_DEL['CN1_prob'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = all_data_DEL.loc[i, 'end']
	end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'CN1_prob'] = np.median(mend_DEL.loc[index, 'CN1_prob'])


all_data_DEL['CN2_prob'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = all_data_DEL.loc[i, 'end']
	end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'CN2_prob'] = np.median(mend_DEL.loc[index, 'CN2_prob'])

print(all_data_DEL.head(10))
all_data_DEL.to_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar.Train.csv', index=False)
all_data_DEL.to_csv('/Users/lmc2/Desktop/NIHFAES/FinalProject/Train/CrowdVar.Train.bed', index=False)



"""
Extra Code 

all_data_DEL['MendConsist'] = np.where((mend_DEL['start'] == all_data_DEL['start']) & (mend_DEL['end'] == all_data_DEL['end']), mend_DEL['Counts'], '0')
all_data_DEL.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.DEL_mend.csv', index=False)
new_df_INS = pd.concat([INS_250bp,INS_300x,INS_10x,INS_MP,INS_PacBio], axis=0)

# print new_df_DEL.head()
new_df_DEL.columns = ['index2', 'chrom.mend', 'start.mend', 'end.mend','id.mend', 'SVtype.mend', 'HG002.mend', 'HG003.mend', 'HG004.mend', 'tech.mend'] 
# print new_df_DEL.head()

# print new_df_DEL.head()
# print new_df_DEL.shape

# print new_df_INS.head()
# print new_df_INS.shape

# ne_stacked = (all_data_DEL != new_df_DEL).stack()
# print ne_stacked.head()

# pd.concat([df,df1], ignore_index=True, axis=1)

# def random(row):
# 	return new_df_DEL['size']
# 	else '1'

# all_data_DEL['new'] = all_data_DEL.apply(func = random, axis = 1)
# print all_data_DEL.head(3)

all_data_DEL['MendConsist'] = np.where((all_data_DEL[['start']].isin(['3262328', '3816054', '3816054', '9168051'])), '1', '0')

print all_data_DEL.head()

df = pd.concat([all_data_DEL,new_df_DEL])
# df['MendConsist'] = np.where((df['start'].isin(df['start.mend']), '1', '0'))
print df.head(3)
df.to_csv('all.csv')

# merged = all_data_DEL.merge(new_df_DEL, on='chrom')
# print merged.head(3)

# merged.to_csv('all.csv')
# merged['MendConsist'] = np.where((merged[['start_x']] == new_df_DEL[['start_y']]), '1', '0')

# all_data_DEL['MendConsist'] = np.where((all_data_DEL[['start']].isin([]) == new_df_DEL[['start']]), '1', '0')
# us_mq_airlines_index = data['unique_carrier'].isin(['US','MQ'])
# # all_data_DEL['MendConsist'] = np.where((all_data_DEL[['start']] == new_df_DEL[['start']]), '1', '0')
# s2[s2.isin(s1)]
"""

